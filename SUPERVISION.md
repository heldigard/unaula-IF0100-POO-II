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
| IF0100 | clase-02 | R1 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R1 - agregadas secciones practica y ejercicios |
| IF0100 | clase-03 | R1 | GitHub Copilot | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R1 - tiempos, checklist, pasos Windows agregados |
| IF0100 | clase-01 | R2 | GitHub Copilot | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R2 - pulido de claridad, ejemplos y checklists |
| IF0100 | clase-02 | R2 | GitHub Copilot | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R2 - pulido de captions y ortografía |
| IF0100 | clase-03 | R2 | GitHub Copilot | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R2 - pulido de ejercicios y ejemplos |
| IF0100 | clase-01 | R3 | GitHub Copilot | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R3 - QA final aprobado |

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
- R2: ✅ PASS - Corregida tilde en "años"; mejorados captions de infografías con más detalle; agregado ejemplo de LINQ en sección ejemplos; checklists agregados a ejercicios para mayor claridad. Factibilidad Windows: sin cambios, ya verificada. Infografías: existentes. TODOs: ninguno.
- R3: ✅ PASS - Verificados anchors y navegación funcional; ortografía y tildes corregidas; coherencia en terminología C#; listo para dictar en aula con Windows. Factibilidad Windows: confirmada. Infografías: ok. TODOs: ninguno.
### clase-02
- R1: ✅ PASS - Agregadas secciones "Practica / Laboratorio" (ejercicio guiado de Libro con checklist y solucion completa) y "Ejercicios" (3 ejercicios: CuentaAhorros, Estudiante, Producto; + tarea Pelicula); navegacion actualizada con nuevos anchors. Factibilidad Windows: ejercicios usan Visual Studio, validaciones standard, dependencias minimas. Infografias: clase-vs-objeto y encapsulamiento (ambas existentes). TODOs: considerar reemplazar ASCII art de pilares/memoria/constructores con infografias en R2.
- R2: ✅ PASS - Mejorados captions de infografías con descripciones más detalladas; corregidas tildes en "Programación", "Ingeniería", etc. para consistencia ortográfica. Factibilidad Windows: sin cambios, ya verificada. Infografías: existentes. TODOs: considerar crear infografías para reemplazar ASCII art de constructores en R3 si necesario.
- R3:
### clase-03
- R1: ✅ PASS - Agregados tiempos estimados a práctica (30 min) y ejercicios (20/30/40 min); checklist de 5 pasos en práctica; pasos detallados para ejecutar en Windows con Visual Studio; motivación expandida con ejemplo de empleados; prerrequisitos actualizados a Windows 10/11. Factibilidad Windows: pasos paso a paso para VS en Windows, dependencias mínimas (.NET). Infografías: clase-03-herencia.png, clase-03-polimorfismo.png (ambas existentes). TODOs: ninguno.
- R2: ✅ PASS - Agregados checklists detallados a cada ejercicio; mejorados captions de infografías con descripciones más específicas; agregado ejemplo de herencia con interfaces para ilustrar polimorfismo múltiple. Factibilidad Windows: sin cambios. Infografías: existentes. TODOs: ninguno.
- R3:

---

# Inicio
1) Regístrate.
2) Toma el primer lock libre (P0 > P1 > P2).
3) Revisa + aplica cambios en la clase.
4) Actualiza SUPERVISION.md y los logs.
