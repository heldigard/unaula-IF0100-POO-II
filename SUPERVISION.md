---
# SUPERVISION — Revisiones paralelas con cambios (máx 3 rondas)

## Reglas
- Lock por (clase, ronda). No editar misma clase en paralelo.
- Máx 3 rondas por clase: R1, R2, R3.
- TTL lock: 45 min sin update => EXPIRED.
- No borrar/mover assets.
- Output: `clases-html/clase-XX.html` + logs `_progress.md` y `_audit.md`.

## Supervisores activos
| Supervisor | Modelo | Estado | Inicio | Último update |
|---|---|---|---|---|
| Codex | GPT-5 | ACTIVE | 2026-02-01 19:35 | 2026-02-01 19:35 |
| GitHub Copilot | Grok Code Fast 1 | ACTIVE | 2026-02-01 | 2026-02-01 |
| Supervisor-03 | claude-opus-4.5 | ACTIVE | 2026-02-01 | 2026-02-01 |

## Locks
| Curso | Clase | Ronda | Supervisor | Estado | Inicio | Último update | TTL | Notas |
|---|---|---|---|---|---|---|---|---|
| IF0100 | clase-01 | R1 | GitHub Copilot | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R1 - infografía agregada, tiempos estimados |
| IF0100 | clase-02 | R1 | Supervisor-03 | ACTIVE | 2026-02-01 | 2026-02-01 | 45min | Revisión inicial iniciada |
| IF0100 | clase-03 | R1 | GitHub Copilot | ACTIVE | 2026-02-01 | 2026-02-01 | 45min | Iniciando revisión |

## Backlog por prioridad
### P0 (mañana)
- [ ] clase-01 (R1/R2/R3)
- [ ] clase-02 (R1/R2/R3)
### P1 (esta semana)
- [ ] clase-03 ...
### P2 (resto)
- [ ] ...

## Registro por clase
### clase-01
- R1: ✅ PASS - Agregada infografía clase-01-value-vs-reference.png para tipos value vs reference; tiempos estimados a prácticas (30/15/10 min) y ejercicios (20/30/60 min); prerrequisito actualizado a Windows 10/11. Factibilidad Windows: instalación VS nativa, ejercicios consola. Infografías: ecosistema (existente), value-vs-reference (creada). TODOs: ninguno.
- R2:
- R3:
### clase-02
- R1:
- R2:
- R3:

---

# Inicio
1) Regístrate.
2) Toma el primer lock libre (P0 > P1 > P2).
3) Revisa + aplica cambios en la clase.
4) Actualiza SUPERVISION.md y los logs.
