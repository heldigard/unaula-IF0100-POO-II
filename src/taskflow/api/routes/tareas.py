"""
Rutas de tareas - TaskFlow API
Unidad: 3.5 - CRUD completo con FastAPI
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from ...models import Usuario
from ...schemas import (
    TareaCreate,
    TareaUpdate,
    TareaResponse,
    TareaListResponse,
)
from ...services import TareaService
from ...repositories import TareaRepository
from ..dependencies import get_current_active_user


router = APIRouter()

# Repo y service
_tarea_repo = TareaRepository()
_tarea_service = TareaService(_tarea_repo)


def get_tarea_service():
    """Obtiene el service de tareas."""
    return _tarea_service


@router.post("/", response_model=TareaResponse, status_code=status.HTTP_201_CREATED)
def crear_tarea(
    data: TareaCreate,
    current_user: Usuario = Depends(get_current_active_user),
    service: TareaService = Depends(get_tarea_service),
):
    """
    Crea una nueva tarea.

    La tarea se asocia al usuario autenticado como creador.
    """
    try:
        tarea = service.crear_tarea(data, current_user.id)
        return TareaResponse(
            id=tarea.id,
            titulo=tarea.titulo,
            descripcion=tarea.descripcion,
            estado=tarea.estado,
            prioridad=tarea.prioridad,
            proyecto_id=tarea.proyecto_id,
            asignado_a=tarea.asignado_a,
            creada_por=tarea.creada_por,
            fecha_limite=tarea.fecha_limite,
            completada_en=tarea.completada_en,
            creada_en=tarea.creada_en,
            actualizada_en=tarea.actualizada_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/", response_model=List[TareaListResponse])
def listar_tareas(
    current_user: Usuario = Depends(get_current_active_user),
    service: TareaService = Depends(get_tarea_service),
):
    """
    Lista las tareas del usuario (filtradas por permisos).
    """
    tareas = service.listar_tareas()
    # TODO: Filtrar por permisos del usuario
    return [
        TareaListResponse(
            id=t.id,
            titulo=t.titulo,
            estado=t.estado,
            prioridad=t.prioridad,
            proyecto_id=t.proyecto_id,
            fecha_limite=t.fecha_limite,
        )
        for t in tareas
    ]


@router.get("/{tarea_id}", response_model=TareaResponse)
def obtener_tarea(
    tarea_id: int,
    service: TareaService = Depends(get_tarea_service),
):
    """Obtiene una tarea por ID."""
    try:
        tarea = service.obtener_tarea(tarea_id)
        return TareaResponse(
            id=tarea.id,
            titulo=tarea.titulo,
            descripcion=tarea.descripcion,
            estado=tarea.estado,
            prioridad=tarea.prioridad,
            proyecto_id=tarea.proyecto_id,
            asignado_a=tarea.asignado_a,
            creada_por=tarea.creada_por,
            fecha_limite=tarea.fecha_limite,
            completada_en=tarea.completada_en,
            creada_en=tarea.creada_en,
            actualizada_en=tarea.actualizada_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.patch("/{tarea_id}", response_model=TareaResponse)
def actualizar_tarea(
    tarea_id: int,
    data: TareaUpdate,
    service: TareaService = Depends(get_tarea_service),
):
    """Actualiza una tarea."""
    try:
        tarea = service.actualizar_tarea(tarea_id, data)
        return TareaResponse(
            id=tarea.id,
            titulo=tarea.titulo,
            descripcion=tarea.descripcion,
            estado=tarea.estado,
            prioridad=tarea.prioridad,
            proyecto_id=tarea.proyecto_id,
            asignado_a=tarea.asignado_a,
            creada_por=tarea.creada_por,
            fecha_limite=tarea.fecha_limite,
            completada_en=tarea.completada_en,
            creada_en=tarea.creada_en,
            actualizada_en=tarea.actualizada_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.post("/{tarea_id}/completar", response_model=TareaResponse)
def marcar_completada(
    tarea_id: int,
    service: TareaService = Depends(get_tarea_service),
):
    """Marca una tarea como completada."""
    try:
        tarea = service.marcar_completada(tarea_id)
        return TareaResponse(
            id=tarea.id,
            titulo=tarea.titulo,
            descripcion=tarea.descripcion,
            estado=tarea.estado,
            prioridad=tarea.prioridad,
            proyecto_id=tarea.proyecto_id,
            asignado_a=tarea.asignado_a,
            creada_por=tarea.creada_por,
            fecha_limite=tarea.fecha_limite,
            completada_en=tarea.completada_en,
            creada_en=tarea.creada_en,
            actualizada_en=tarea.actualizada_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.get("/vencidas", response_model=List[TareaListResponse])
def listar_vencidas(
    service: TareaService = Depends(get_tarea_service),
):
    """Lista tareas vencidas (no completadas y fecha límite pasada)."""
    tareas = service.listar_vencidas()
    return [
        TareaListResponse(
            id=t.id,
            titulo=t.titulo,
            estado=t.estado,
            prioridad=t.prioridad,
            proyecto_id=t.proyecto_id,
            fecha_limite=t.fecha_limite,
        )
        for t in tareas
    ]


@router.get("/por-vencer", response_model=List[TareaListResponse])
def listar_por_vencer(
    dias: int = 7,
    service: TareaService = Depends(get_tarea_service),
):
    """Lista tareas por vencer en los próximos N días."""
    tareas = service.listar_por_vencer(dias)
    return [
        TareaListResponse(
            id=t.id,
            titulo=t.titulo,
            estado=t.estado,
            prioridad=t.prioridad,
            proyecto_id=t.proyecto_id,
            fecha_limite=t.fecha_limite,
        )
        for t in tareas
    ]
