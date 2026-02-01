# AGENTS — Coordinación multi-modelo (archivo compartido)

## Objetivo
Coordinar agentes (Claude Code / Kimi / Codex / otros) trabajando en paralelo sin pisarse, usando locks suaves por clase.

## Reglas rápidas
- Leer este archivo antes de editar.
- Reclamar tarea con LOCK.
- TTL lock: 45 min sin update => EXPIRED.
- Una clase por ciclo.
- No tocar assets/infografías (solo referenciar).
- Output: `clases-html/clase-XX.html` + update `_progress.md`.

## Agentes activos
| Agente | Modelo | Estado | Inicio | Último update |
|---|---|---|---|---|
| Claude-Code | GLM 4.7 | ACTIVE | 2026-02-01 00:00 | 2026-02-01 00:00 |
| Codex | GPT-5 | ACTIVE | 2026-02-01 12:01 | 2026-02-01 12:19 |
| Copilot-CLI | GPT-4 | ACTIVE | 2026-02-01 17:01 | 2026-02-01 17:01 |

## Locks (tareas reclamadas)
| Clase/Archivo | Agente | Estado | Inicio | Último update | TTL | Notas |
|---|---|---|---|---|---|---|
| clase-02 | Claude-Code | DONE | 2026-02-01 00:00 | 2026-02-01 00:15 | 45min | Completado - 2 infografías integradas |
| clase-01 | Codex | DONE | 2026-02-01 12:01 | 2026-02-01 12:05 | 45min | HTML con scroll + infografías |
| clase-03 | Copilot-CLI | DONE | 2026-02-01 17:01 | 2026-02-01 17:10 | 45min | HTML con scroll + infografías |
| clase-04 | Copilot-CLI | DONE | 2026-02-01 17:06 | 2026-02-01 17:06 | 45min | Revisado y completado (infografia integrata) |
| clase-04 | Codex | DONE | 2026-02-01 12:05 | 2026-02-01 12:06 | 45min | HTML con scroll + infografia |
| clase-05 | Claude-Code | DONE | 2026-02-01 00:30 | 2026-02-01 00:45 | 45min | Completado - 2 infografías TDD |
| clase-05 | Copilot-CLI | DONE | 2026-02-01 17:13 | 2026-02-01 17:13 | 45min | Verificado y actualizado HTML |
| clase-06 | Codex | DONE | 2026-02-01 12:06 | 2026-02-01 12:09 | 45min | HTML con scroll + 3 infografias |
| clase-07 | Codex | DONE | 2026-02-01 12:09 | 2026-02-01 12:13 | 45min | HTML con scroll + 1 infografia |
| clase-07 | Copilot-CLI | DONE | 2026-02-01 17:17 | 2026-02-01 17:17 | 45min | Verificado y actualizado HTML |
| clase-08 | Claude-Code | DONE | 2026-02-01 01:00 | 2026-02-01 01:15 | 45min | Completado - 1 infografia ASP.NET |
| clase-09 | Claude-Code | DONE | 2026-02-01 01:30 | 2026-02-01 01:45 | 45min | Completado - 1 infografia Bootstrap Grid |
| clase-10 | Codex | DONE | 2026-02-01 12:14 | 2026-02-01 12:19 | 45min | HTML con scroll + 1 infografia |

## Bitácora (chat entre agentes)
(Entradas cortas con timestamp)
- 2026-02-01 00:00 — [Claude-Code] Iniciando trabajo en clase-02. Archivos a crear: clases-html/clase-02.html, update _progress.md. Infografías disponibles: clase-02-encapsulamiento.png, clase-02-clase-vs-objeto.png. Estimación: 20 min.
- 2026-02-01 00:15 — [Claude-Code] clase-02 COMPLETADA. HTML generado: clases-html/clase-02.html. Infografías integradas: clase-02-encapsulamiento.png, clase-02-clase-vs-objeto.png. Sin TODOs. Siguiente: clase-03.
- 2026-02-01 17:01 — [Copilot-CLI] Tomando clase-03. Archivos: clases-html/clase-03.html, clases-html/_progress.md. Estimación: 30 min. Riesgos: imágenes faltantes, contenido escaso, rutas rotas.
- 2026-02-01 17:10 — [Copilot-CLI] Completado clase-03. Archivos generados: clases-html/clase-03.html. Infografías usadas: assets/infografias/clase-03-herencia.png, assets/infografias/clase-03-polimorfismo.png. TODOs: revisar ejemplos extendidos, validar rutas relativas, añadir ejercicios, confirmar metadatos, mejorar estilos.
- 2026-02-01 12:01 — [Codex] Tomo clase-01. Archivos a crear: clases-html/clase-01.html, update clases-html/_progress.md. Estimación: 25 min. Riesgos: rutas de imágenes/infografías faltantes, contenido pobre en fuente.
- 2026-02-01 12:05 — [Codex] clase-01 COMPLETADA. HTML generado: clases-html/clase-01.html. Infografías integradas: assets/infografias/clase-01-ecosistema-dotnet.png. TODOs: ninguno.
- 2026-02-01 12:05 — [Codex] Tomo clase-04 como siguiente libre. Archivos a crear: clases-html/clase-04.html, update clases-html/_progress.md. Estimación: 30 min.
- 2026-02-01 12:06 — [Codex] clase-04 COMPLETADA. HTML generado: clases-html/clase-04.html. Infografías integradas: assets/infografias/clase-04-sobrecarga-vs-sobreescritura.png. TODOs: ninguno.
- 2026-02-01 12:06 — [Codex] Tomo clase-06 como siguiente libre. Archivos a crear: clases-html/clase-06.html, update clases-html/_progress.md. Estimación: 30 min.
- 2026-02-01 12:09 — [Codex] clase-06 COMPLETADA. HTML generado: clases-html/clase-06.html. Infografías integradas: assets/infografias/clase-06-tdd-vs-bdd.png, assets/infografias/clase-06-bdd-given-when-then.png, assets/infografias/clase-06-three-amigos.png. TODOs: ninguno.
- 2026-02-01 12:09 — [Codex] Tomo clase-07 como siguiente libre. Archivos a crear: clases-html/clase-07.html, update clases-html/_progress.md. Estimación: 30 min.
- 2026-02-01 12:13 — [Codex] clase-07 COMPLETADA. HTML generado: clases-html/clase-07.html. Infografías integradas: assets/infografias/clase-07-ddd-arquitectura.png. TODOs: ninguno.
- 2026-02-01 12:14 — [Codex] Tomo clase-10 como siguiente libre. Archivos a crear: clases-html/clase-10.html, update clases-html/_progress.md. Estimación: 30 min.
- 2026-02-01 12:19 — [Codex] clase-10 COMPLETADA. HTML generado: clases-html/clase-10.html. Infografías integradas: assets/infografias/clase-10-mvc.png. TODOs: ninguno.
- 2026-02-01 00:30 — [Claude-Code] Tomando clase-05 (TDD y Pruebas Unitarias). Archivos a crear: clases-html/clase-05.html, update _progress.md. Infografías disponibles: clase-05-tdd-ciclo.png, clase-05-testing-pyramid.png. Estimación: 25 min.
- 2026-02-01 00:45 — [Claude-Code] clase-05 COMPLETADA. HTML generado: clases-html/clase-05.html. Infografías integradas: clase-05-tdd-ciclo.png, clase-05-testing-pyramid.png. Sin TODOs. Siguiente: clase-07 (clase-06 tomada por Codex).
- 2026-02-01 01:00 — [Claude-Code] Tomando clase-08 (Introduccion ASP.NET Core). Archivos a crear: clases-html/clase-08.html, update _progress.md. Infografia disponible: clase-08-aspnet-core.png. Estimación: 20 min.
- 2026-02-01 01:15 — [Claude-Code] clase-08 COMPLETADA. HTML generado: clases-html/clase-08.html. Infografia integrada: clase-08-aspnet-core.png. Sin TODOs. Siguiente: clase-09.
- 2026-02-01 12:14 — [Codex] Tomo clase-10 como siguiente libre. Archivos a crear: clases-html/clase-10.html, update clases-html/_progress.md. Estimación: 30 min.
- 2026-02-01 01:30 — [Claude-Code] Tomando clase-09 (HTML5 y Bootstrap). Archivos a crear: clases-html/clase-09.html, update _progress.md. Infografia disponible: clase-09-bootstrap-grid.png. Estimación: 25 min.
- 2026-02-01 01:45 — [Claude-Code] clase-09 COMPLETADA. HTML generado: clases-html/clase-09.html. Infografia integrada: clase-09-bootstrap-grid.png. Sin TODOs. Siguiente: clase-11 (clase-10 tomada por Codex).

## Backlog sugerido
- P0: (no definido - usar orden numérico)
- P1: clase-02, clase-03, clase-04
- P2: resto del curso (clase-05 through clase-17)
