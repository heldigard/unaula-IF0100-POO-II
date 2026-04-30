from __future__ import annotations

import json
import random
import threading
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent
QUESTIONS_PATH = BASE_DIR / "questions.json"
ROOM_CODE_CHARS = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
ROOM_CODE_LENGTH = 4
MAX_QUESTIONS_PER_MATCH = 12
DEFAULT_QUESTIONS_PER_MATCH = 10
DEFAULT_QUESTION_TIME = 30
REVEAL_SECONDS = 5
ROOM_TTL_SECONDS = 60 * 60


class Question(BaseModel):
    q: str
    options: List[str]
    correct: int
    explain: Optional[str] = None


class CreateRoomRequest(BaseModel):
    unit: str
    question_time: int = DEFAULT_QUESTION_TIME
    questions_per_match: int = DEFAULT_QUESTIONS_PER_MATCH


class JoinRequest(BaseModel):
    player_name: str


class AnswerRequest(BaseModel):
    player_id: str
    selected_option: int


class PlayerState:
    def __init__(self, player_id: str, name: str) -> None:
        self.id = player_id
        self.name = name.strip() or "Anónimo"
        self.score = 0
        self.joined_at = time.time()


class Room:
    def __init__(
        self,
        code: str,
        unit: str,
        question_bank: List[Question],
        question_time: int,
        questions_per_match: int,
    ) -> None:
        self.code = code
        self.unit = unit
        self.question_time = max(5, int(question_time))
        self.questions_per_match = max(
            1,
            min(int(questions_per_match), len(question_bank), MAX_QUESTIONS_PER_MATCH),
        )
        self.questions = [
            shuffle_question_options(question)
            for question in random.sample(question_bank, k=self.questions_per_match)
        ]
        self.created_at = time.time()
        self.current_index = 0
        self.status = "waiting"
        self.question_started_at: Optional[float] = None
        self.reveal_started_at: Optional[float] = None
        self.players: Dict[str, PlayerState] = {}
        self.current_answers: Dict[str, int] = {}
        self.current_answer_times: Dict[str, float] = {}
        self.current_counts = [0, 0, 0, 0]
        self.finished_at: Optional[float] = None

    def current_question(self) -> Optional[Question]:
        if self.current_index >= len(self.questions):
            return None
        return self.questions[self.current_index]

    def time_left(self, now: Optional[float] = None) -> int:
        if self.status != "active" or self.question_started_at is None:
            return 0
        now = now if now is not None else time.time()
        remaining = int(self.question_time - (now - self.question_started_at))
        return max(0, remaining)

    def add_player(self, name: str) -> str:
        player_id = uuid4().hex[:12]
        self.players[player_id] = PlayerState(player_id, name)
        return player_id


def shuffle_question_options(question: Question) -> Question:
    indexed_options = list(enumerate(question.options))
    random.shuffle(indexed_options)
    options = [option for _, option in indexed_options]
    correct = next(
        idx
        for idx, (original_idx, _) in enumerate(indexed_options)
        if original_idx == question.correct
    )
    return Question(
        q=question.q,
        options=options,
        correct=correct,
        explain=question.explain,
    )


class State:
    def __init__(self) -> None:
        self.rooms: Dict[str, Room] = {}
        self.lock = threading.Lock()

    def cleanup_old_rooms(self, now: Optional[float] = None) -> None:
        now = now if now is not None else time.time()
        expired = [
            code
            for code, room in self.rooms.items()
            if now - room.created_at > ROOM_TTL_SECONDS
        ]
        for code in expired:
            self.rooms.pop(code, None)


app = FastAPI(title="IF0100 Kaboom Quiz API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


try:
    with QUESTIONS_PATH.open("r", encoding="utf-8") as f:
        _raw_questions = json.load(f)
except Exception as exc:  # pragma: no cover
    raise RuntimeError(f"No se pudo cargar questions.json desde {QUESTIONS_PATH}") from exc

QUESTION_BANK: Dict[str, List[Question]] = {
    key: [Question(**q) for q in questions]
    for key, questions in _raw_questions.items()
}

STATE = State()


def generate_room_code() -> str:
    while True:
        code = "".join(random.choice(ROOM_CODE_CHARS) for _ in range(ROOM_CODE_LENGTH))
        if code not in STATE.rooms:
            return code


def get_room(code: str) -> Room:
    room = STATE.rooms.get(code.upper())
    if not room:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    return room


def compute_score_delta(selected: Optional[int], question: Question, answered_at: float, room: Room) -> int:
    if selected is None:
        return -10
    if selected == question.correct:
        raw_left = max(0.0, room.question_time - (answered_at - (room.question_started_at or time.time())))
        bonus = int(raw_left) * 4
        return 80 + bonus
    return -15


def clear_current_answers(room: Room) -> None:
    room.current_answers = {}
    room.current_answer_times = {}
    room.current_counts = [0, 0, 0, 0]


def all_students_answered(room: Room) -> bool:
    return len(room.current_answers) >= len(room.players)


def finalize_question(room: Room, now: Optional[float] = None) -> None:
    now = now if now is not None else time.time()
    question = room.current_question()
    if question is None:
        room.status = "finished"
        room.finished_at = now
        return
    if room.status != "active":
        return

    for player in room.players.values():
        selected = room.current_answers.get(player.id)
        answered_at = room.current_answer_times.get(player.id, now)
        player.score = max(0, player.score + compute_score_delta(selected, question, answered_at, room))

    room.status = "reveal"
    room.reveal_started_at = now


def move_to_next_question(room: Room, now: Optional[float] = None) -> None:
    now = now if now is not None else time.time()
    room.current_index += 1
    if room.current_index >= len(room.questions):
        room.status = "finished"
        room.finished_at = now
        room.reveal_started_at = None
        room.question_started_at = None
        return

    room.status = "active"
    room.question_started_at = now
    room.reveal_started_at = None
    clear_current_answers(room)


def advance_if_needed(room: Room, now: Optional[float] = None) -> None:
    now = now if now is not None else time.time()

    if room.status == "active":
        if room.time_left(now) <= 0:
            finalize_question(room, now)
    elif room.status == "reveal":
        if room.reveal_started_at is not None and now - room.reveal_started_at >= REVEAL_SECONDS:
            move_to_next_question(room, now)


def room_state_payload(room: Room, player_id: Optional[str] = None) -> Dict[str, Any]:
    now = time.time()
    advance_if_needed(room, now)

    question = room.current_question()
    current_question_payload = None
    if question is not None and room.status in {"active", "reveal"}:
        current_question_payload = {
            "index": room.current_index,
            "text": question.q,
            "options": question.options,
            "correct": question.correct if room.status in {"reveal", "finished"} else None,
            "explain": question.explain if room.status in {"reveal", "finished"} else None,
        }

    ranking = sorted(room.players.values(), key=lambda p: p.score, reverse=True)
    leaderboard = [
        {"id": p.id, "name": p.name, "score": p.score}
        for p in ranking
    ]

    player_entry = room.players.get(player_id) if player_id else None
    my_score = player_entry.score if player_entry else 0

    return {
        "code": room.code,
        "unit": room.unit,
        "status": room.status,
        "question_index": room.current_index,
        "total_questions": len(room.questions),
        "question_time": room.question_time,
        "time_left": room.time_left(now),
        "question": current_question_payload,
        "answer_counts": room.current_counts.copy(),
        "my_answer": room.current_answers.get(player_id) if player_id else None,
        "my_score": my_score,
        "has_answered": player_id in room.current_answers if player_id else False,
        "leaderboard": leaderboard,
        "finished_at": room.finished_at,
        "started": room.status != "waiting",
        "player_count": len(room.players),
    }


def validate_unit(unit: str) -> None:
    if unit not in QUESTION_BANK:
        raise HTTPException(status_code=404, detail="Unidad no encontrada")
    if not QUESTION_BANK[unit]:
        raise HTTPException(status_code=400, detail="Unidad sin preguntas")


async def parse_request_model(request: Request, model: type[BaseModel]) -> BaseModel:
    try:
        return model(**await request.json())
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Payload inválido") from exc


def create_room_payload(payload: CreateRoomRequest) -> Dict[str, Any]:
    validate_unit(payload.unit)

    with STATE.lock:
        STATE.cleanup_old_rooms()
        pool = QUESTION_BANK[payload.unit]
        room = Room(
            code=generate_room_code(),
            unit=payload.unit,
            question_bank=pool,
            question_time=payload.question_time,
            questions_per_match=payload.questions_per_match,
        )
        STATE.rooms[room.code] = room
        payload_state = room_state_payload(room)

    return payload_state


def join_room_payload(code: str, payload: JoinRequest) -> Dict[str, Any]:
    if not payload.player_name.strip():
        raise HTTPException(status_code=400, detail="Nombre requerido")

    code = code.upper()
    with STATE.lock:
        room = get_room(code)
        player_id = room.add_player(payload.player_name)
        if room.status == "waiting":
            response = room_state_payload(room, player_id)
        else:
            response = room_state_payload(room, player_id)

    return {"player_id": player_id, **response}


def start_room_payload(code: str) -> Dict[str, Any]:
    code = code.upper()
    with STATE.lock:
        room = get_room(code)
        if room.status == "waiting":
            room.status = "active"
            room.question_started_at = time.time()
        response = room_state_payload(room)
    return response


def submit_answer_payload(code: str, payload: AnswerRequest) -> Dict[str, Any]:
    code = code.upper()
    selected = payload.selected_option

    with STATE.lock:
        room = get_room(code)
        if room.status != "active":
            raise HTTPException(status_code=409, detail="La pregunta no está activa")

        if payload.player_id not in room.players:
            raise HTTPException(status_code=404, detail="Jugador no encontrado")

        question = room.current_question()
        if question is None:
            raise HTTPException(status_code=400, detail="No hay pregunta activa")

        if selected < 0 or selected >= len(question.options):
            raise HTTPException(status_code=400, detail="Opción inválida")

        if payload.player_id not in room.current_answers:
            room.current_answers[payload.player_id] = selected
            room.current_answer_times[payload.player_id] = time.time()
            if 0 <= selected < len(room.current_counts):
                room.current_counts[selected] += 1

        if all_students_answered(room):
            finalize_question(room)

        response = room_state_payload(room, payload.player_id)
        advance_if_needed(room)

    return response


@app.post("/api/rooms")
async def create_room(request: Request) -> Dict[str, Any]:
    payload = await parse_request_model(request, CreateRoomRequest)
    return create_room_payload(payload)


@app.get("/api/live/create")
def create_room_live(
    unit: str,
    question_time: int = DEFAULT_QUESTION_TIME,
    questions_per_match: int = DEFAULT_QUESTIONS_PER_MATCH,
) -> Dict[str, Any]:
    return create_room_payload(CreateRoomRequest(
        unit=unit,
        question_time=question_time,
        questions_per_match=questions_per_match,
    ))


@app.post("/api/rooms/{code}/join")
async def join_room(code: str, request: Request) -> Dict[str, Any]:
    payload = await parse_request_model(request, JoinRequest)
    return join_room_payload(code, payload)


@app.get("/api/live/{code}/join")
def join_room_live(code: str, player_name: str) -> Dict[str, Any]:
    return join_room_payload(code, JoinRequest(player_name=player_name))


@app.post("/api/rooms/{code}/start")
def start_room(code: str) -> Dict[str, Any]:
    return start_room_payload(code)


@app.get("/api/live/{code}/start")
def start_room_live(code: str) -> Dict[str, Any]:
    return start_room_payload(code)


@app.get("/api/live/{code}/begin")
def begin_room_live(code: str) -> Dict[str, Any]:
    return start_room_payload(code)


@app.post("/api/rooms/{code}/answer")
async def submit_answer(code: str, request: Request) -> Dict[str, Any]:
    payload = await parse_request_model(request, AnswerRequest)
    return submit_answer_payload(code, payload)


@app.get("/api/live/{code}/answer")
def submit_answer_live(code: str, player_id: str, selected_option: int) -> Dict[str, Any]:
    return submit_answer_payload(
        code,
        AnswerRequest(player_id=player_id, selected_option=selected_option),
    )


@app.get("/api/rooms/{code}")
def get_room_state(code: str, player_id: Optional[str] = None) -> Dict[str, Any]:
    code = code.upper()
    with STATE.lock:
        room = get_room(code)
        return room_state_payload(room, player_id)


@app.get("/api/rooms/{code}/leaderboard")
def room_leaderboard(code: str) -> Dict[str, Any]:
    code = code.upper()
    with STATE.lock:
        room = get_room(code)
        ranking = sorted(room.players.values(), key=lambda p: p.score, reverse=True)
        return {
            "code": room.code,
            "unit": room.unit,
            "leaderboard": [
                {"id": p.id, "name": p.name, "score": p.score}
                for p in ranking
            ],
            "status": room.status,
            "question_index": room.current_index,
            "total_questions": len(room.questions),
        }


@app.get("/api/units")
def list_units() -> List[str]:
    return sorted(QUESTION_BANK.keys())


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}
