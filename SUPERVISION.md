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
| Codex | GPT-5 | ACTIVE | 2026-02-01 19:35 | 2026-02-01 20:35 |
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
| IF0100 | clase-02 | R3 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | QA final aprobado - clase lista para dictar |
| IF0100 | clase-03 | R3 | Codex | DONE | 2026-02-01 20:05 | 2026-02-01 20:10 | 45min | QA final completado |
| IF0100 | clase-04 | R1 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R1 - agregados tiempos, checklist, detalles ejercicios |
| IF0100 | clase-05 | R1 | Codex | DONE | 2026-02-01 20:20 | 2026-02-01 20:35 | 45min | Completado R1 - práctica y checklist añadidos |
| IF0100 | clase-04 | R2 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R2 - caption infografia mejorado |
| IF0100 | clase-04 | R3 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | QA final aprobado - clase lista para dictar |
| IF0100 | clase-06 | R1 | Codex | DONE | 2026-02-01 20:50 | 2026-02-01 21:05 | 45min | R1 completada |
| IF0100 | clase-05 | R2 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R2 - captions mejorados, ortografía corregida |
| IF0100 | clase-05 | R3 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | QA final aprobado - clase lista para dictar |
| IF0100 | clase-06 | R2 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R2 - captions mejorados, ortografía corregida |
| IF0100 | clase-06 | R3 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | QA final aprobado - clase lista para dictar |
| IF0100 | clase-07 | R1 | Codex | DONE | 2026-02-01 21:15 | 2026-02-01 21:35 | 45min | R1 completada |
| IF0100 | clase-07 | R2 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R2 - caption mejorado, ortografía corregida (arquitectura, explícitas) |
| IF0100 | clase-07 | R3 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | QA final aprobado - clase lista para dictar |
| IF0100 | clase-08 | R1 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R1 - práctica añadida, ortografía corregida, tiempos y checklists agregados |
| IF0100 | clase-08 | R2 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R2 - caption mejorado, ortografía corregida (numéricos, Solicitud, básica) |
| IF0100 | clase-08 | R3 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | QA final aprobado - clase lista para dictar |
| IF0100 | clase-09 | R1 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R1 - corrupción HTML corregida, práctica añadida, tiempos/checklists agregados |
| IF0100 | clase-09 | R2 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R2 - caption mejorado, ortografía corregida (código, Sistema, breakpoints, Corazón, diseño) |
| IF0100 | clase-09 | R3 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | QA final aprobado - clase lista para dictar |
| IF0100 | clase-10 | R1 | Supervisor-03 | DONE | 2026-02-01 | 2026-02-01 | 45min | Completado R1 - ortografía corregida, práctica mejorada con pasos VS 2022, tiempos/checklists agregados |

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
- R3: ✅ PASS - Verificados todos los anchors (15 enlaces, todos funcionales); confirmada ortografía y consistencia de tildes; revisada coherencia terminológica en C# (class vs struct, static, properties, constructors); validado flujo pedagógico completo (teoria -> ejemplos -> practica -> ejercicios -> resumen); clase lista para dictar en aula Windows. Factibilidad Windows: confirmada - Visual Studio 2022, validaciones standard C#, sin dependencias externas. Infografías: clase-vs-objeto y encapsulamiento (ambas con captions mejorados). TODOs: ninguno.
### clase-03
- R1: ✅ PASS - Agregados tiempos estimados a práctica (30 min) y ejercicios (20/30/40 min); checklist de 5 pasos en práctica; pasos detallados para ejecutar en Windows con Visual Studio; motivación expandida con ejemplo de empleados; prerrequisitos actualizados a Windows 10/11. Factibilidad Windows: pasos paso a paso para VS en Windows, dependencias mínimas (.NET). Infografías: clase-03-herencia.png, clase-03-polimorfismo.png (ambas existentes). TODOs: ninguno.
- R2: ✅ PASS - Agregados checklists detallados a cada ejercicio; mejorados captions de infografías con descripciones más específicas; agregado ejemplo de herencia con interfaces para ilustrar polimorfismo múltiple. Factibilidad Windows: sin cambios. Infografías: existentes. TODOs: ninguno.
- R3: ✅ PASS - QA final: corregido "sobreescritura" en objetivos; actualizado ".NET" en pasos de laboratorio; anchors verificados. Factibilidad Windows: sin cambios, pasos VS 2022 confirmados. Infografías: existentes. TODOs: ninguno.
### clase-04
- R1: ✅ PASS - Agregados tiempos estimados a practica (30 min calculadora + 15 min constructores + 20 min modelado ER) y ejercicios (30/25/40 min); checklist de 6 pasos en practica con solucion completa de Calculadora; tabla de entidades de biblioteca con PK/FK/cardinalidad; ejercicios completados con requisitos, soluciones esperadas, checklists y tarea Vector2D. Factibilidad Windows: ejercicios usan Visual Studio, sobrecarga standard C#, modelado ER teorico. Infografías: clase-04-sobrecarga-vs-sobreescritura.png (existente). TODOs: considerar mejorar caption de infografia en R2.
- R2: ✅ PASS - Mejorado caption de infografia con descripcion detallada y pedagogica: explica diferencia clave entre sobrecarga (misma clase, firma diferente, resolucion estatica) y sobreescritura (herencia, misma firma, resolucion dinamica con virtual/override). Factibilidad Windows: sin cambios, ya verificada en R1. Infografías: clase-04-sobrecarga-vs-sobreescritura.png (existente). TODOs: ninguno.
- R3: ✅ PASS - Verificados todos los anchors (5 enlaces, todos funcionales: #teoria, #ejemplos, #practica, #ejercicios, #referencias); confirmada ortografía y tildes; revisada coherencia terminológica en C# (sobrecarga, sobreescritura, operadores, modelado ER); validado flujo pedagógico completo (teoria -> ejemplos -> practica -> ejercicios -> referencias); clase lista para dictar en aula con Windows. Factibilidad Windows: confirmada - Visual Studio 2022, sobrecarga standard C#, modelado ER teorico. Infografías: clase-04-sobrecarga-vs-sobreescritura.png (con caption mejorado). TODOs: ninguno.
### clase-05
- R1: ✅ PASS - Correcciones de acentos/ortografía; añadida práctica/laboratorio con pasos Windows y checklist; tiempos y checklists en ejercicios; tabla de Test Doubles corregida y ejemplo FakeRepo genérico. Factibilidad Windows: verificada con Visual Studio 2022 y xUnit. Infografías: clase-05-tdd-ciclo.png, clase-05-testing-pyramid.png. TODOs: ninguno.
- R2: ✅ PASS - Mejorados captions de ambas infografías con descripciones pedagógicas detalladas (Ciclo TDD Red-Green-Refactor con explicación de flujo iterativo; Pirámide de Testing con estrategia de estratificación y balance cobertura/velocidad/costo); corregidos acentos en "código", "Pirámide", "Más", "integración", "Método", "Operación". Factibilidad Windows: sin cambios, ya verificada en R1. Infografías: existentes. TODOs: ninguno.
- R3: ✅ PASS - Verificados todos los anchors (10 enlaces, todos funcionales: #objetivos, #que-es-tdd, #ciclo-tdd, #xunit, #patron-aaa, #test-doubles, #ejemplos, #practica, #ejercicios, #resumen); corregido bug HTML (duplicado section id="ejercicios" eliminado); confirmada ortografía y tildes ("Mínimo", "mayúscula", "parámetros", "patrón", "Descripción", "Próximos"); revisada coherencia terminológica en C# y xUnit (TDD, AAA, Test Doubles, Fact/Theory/InlineData); validado flujo pedagógico completo (teoria -> ejemplos -> practica -> ejercicios -> resumen); clase lista para dictar en aula con Windows. Factibilidad Windows: confirmada - Visual Studio 2022 y xUnit. Infografías: clase-05-tdd-ciclo.png y clase-05-testing-pyramid.png (ambas con captions mejorados). TODOs: ninguno.
### clase-06
- R1: ✅ PASS - Correcciones de acentos/ortografía; prerrequisitos Windows 10/11; práctica con pasos VS 2022 + checklist; tiempos y checklists en ejercicios; mejoras en Gherkin/captions. Factibilidad Windows verificada. Infografías: clase-06-tdd-vs-bdd.png, clase-06-bdd-given-when-then.png, clase-06-three-amigos.png. TODOs: ninguno.
- R2: ✅ PASS - Mejorados captions de las 3 infografías con descripciones pedagógicas detalladas (TDD vs BDD con enfoque técnico vs negocio; Given-When-Then con estructura de contexto-acción-resultado; Three Amigos con colaboración negocio-dev-QA); corregidos acentos en "Característica", "Cuándo", "Acción", "Característica" (en código Gherkin), "documentación", "Prácticas". Factibilidad Windows: sin cambios, ya verificada en R1. Infografías: clase-06-tdd-vs-bdd.png, clase-06-bdd-given-when-then.png, clase-06-three-amigos.png (existentes). TODOs: ninguno.
- R3: ✅ PASS - Verificados todos los anchors (5 enlaces, todos funcionales: #teoria, #ejemplos, #practica, #ejercicios, #referencias); corregidos acentos en "básicos", "código" (en parámetro de Step Definition); confirmada ortografía y consistencia de tildes; revisada coherencia terminológica en BDD (Gherkin, SpecFlow, Given-When-Then, Three Amigos); validado flujo pedagógico completo (teoria -> ejemplos -> practica -> ejercicios -> referencias); clase lista para dictar en aula con Windows. Factibilidad Windows: confirmada - Visual Studio 2022 o CLI .NET 8 SDK. Infografías: clase-06-tdd-vs-bdd.png, clase-06-bdd-given-when-then.png, clase-06-three-amigos.png (existentes, captions mejorados). TODOs: ninguno.
### clase-07
- R1: ✅ PASS - Correcciones de acentos/ortografía; prerrequisitos Windows 10/11; práctica con pasos VS 2022 + checklist; tiempos y checklists en ejercicios; notas en lenguaje ubicuo. Factibilidad Windows verificada. Infografías: clase-07-ddd-arquitectura.png. TODOs: ninguno.
- R2: ✅ PASS - Mejorado caption de infografía con descripción pedagógica detallada de las 4 capas DDD; corregidos acentos en "arquitectura" y "explícitas". Factibilidad Windows: sin cambios, ya verificada en R1. Infografías: clase-07-ddd-arquitectura.png (existente, caption mejorado). TODOs: ninguno.
- R3: ✅ PASS - Verificados todos los anchors (5 enlaces, todos funcionales: #teoria, #ejemplos, #practica, #ejercicios, #referencias); corregido "solo" → "sólo" para consistencia ortográfica; confirmada ortografía y tildes; revisada coherencia terminológica en DDD (Entities, Value Objects, Aggregates, Repository, Domain Services, Bounded Contexts); validado flujo pedagógico completo (teoria → ejemplos → practica → ejercicios → referencias); clase lista para dictar en aula con Windows. Factibilidad Windows: confirmada - Visual Studio 2022 y .NET 8 SDK. Infografías: clase-07-ddd-arquitectura.png (caption mejorado). TODOs: ninguno.
### clase-08
- R1: ✅ PASS - Corregidas ortografía y tildes múltiples (Introducción, Programación, Ingeniería, Duración, qué, Definición, Características, Descripción, arquitectura, típico, básico, opción, páginas, página, código, Prácticos, validación); corregido error HTML "Endpo</strong>int" → "Endpoint"; corregida estructura de tabla (td duplicados); añadida sección "Práctica / Laboratorio" con pasos VS 2022 y checklists; añadidos prerrequisitos en header; añadidos tiempos a ejercicios (20/15/25 min) y checklists. Factibilidad Windows: verificada - Visual Studio 2022 con .NET 8 SDK. Infografías: clase-08-aspnet-core.png (existente). TODOs: ninguno.
- R2: ✅ PASS - Mejorado caption de infografía con descripción pedagógica detallada de Middleware Pipeline, Kestrel y opciones de desarrollo (Razor Pages, MVC, Web API, Blazor); corregidos acentos en "numéricos", "Solicitud", "básica". Factibilidad Windows: sin cambios, ya verificada en R1. Infografías: clase-08-aspnet-core.png (existente, caption mejorado). TODOs: ninguno.
- R3: ✅ PASS - Verificados todos los anchors (10 enlaces, todos funcionales: #objetivos, #que-es, #arquitectura, #middleware, #crear-proyecto, #razor-pages, #middleware-custom, #practica, #ejercicios, #resumen, #inicio); corregidos acentos restantes en "método", "válida", "validación"; confirmada ortografía y consistencia de tildes; revisada coherencia terminológica en ASP.NET Core (Middleware Pipeline, Kestrel, Razor Pages, PageModel, Dependency Injection, MVC, Web API, Blazor, cross-platform); validado flujo pedagógico completo (objetivos → que es → arquitectura → middleware → crear proyecto → razor pages → middleware custom → práctica → ejercicios → resumen); clase lista para dictar en aula con Windows. Factibilidad Windows: confirmada - Visual Studio 2022 con .NET 8 SDK. Infografías: clase-08-aspnet-core.png (caption mejorado). TODOs: ninguno.
### clase-09
- R1: ✅ PASS - Corregida corrupción HTML masiva (meta tags, title, CSS properties, etiquetas HTML rotas); corregida ortografía (Programación, Ingeniería, Informática, Duración, Validación, Operación, etc.); añadida sección "Práctica / Laboratorio" con 30 min, pasos VS 2022 y estructura HTML/Bootstrap básica; añadidos prerrequisitos en header; añadidos tiempos a ejercicios (20/25/30 min) y 3 checklists; actualizada navegación con enlace a práctica. Factibilidad Windows: verificada - Visual Studio 2022 con Bootstrap 5 CDN. Infografías: clase-09-html5-bootstrap.png (existente). TODOs: ninguno.
- R2: ✅ PASS - Mejorado caption de infografía con descripción pedagógica detallada de sistema de grillas Bootstrap (grid de 12 columnas, breakpoints xs/sm/md/lg/xl/xxl, layouts responsive mobile-first); corregidos acentos en "código", "Sistema", "breakpoints", "Corazón", "diseño". Factibilidad Windows: sin cambios, ya verificada en R1. Infografías: clase-09-Bootstrap-grid.png (existente, caption mejorado). TODOs: ninguno.
- R3: ✅ PASS - Verificados todos los anchors (12 enlaces, todos funcionales: #objetivos, #agenda, #html5, #formularios, #Bootstrap, #grid, #componentes, #aspnet, #practica, #ejercicios, #referencias); corregida ortografía restante (footer, estado, estad, Contacto, pública, numérica, login, checkbox, dropdown, offcanvas); confirmada ortografía y consistencia de tildes; revisada coherencia terminológica en HTML5/Bootstrap (etiquetas semánticas, formularios HTML5, sistema de grillas, componentes Bootstrap, breakpoints responsive); validado flujo pedagógico completo (objetivos → agenda → HTML5 → formularios → Bootstrap → grid → componentes → ASP.NET → práctica → ejercicios → referencias); clase lista para dictar en aula con Windows. Factibilidad Windows: confirmada - Visual Studio 2022 con Bootstrap 5 CDN. Infografías: clase-09-Bootstrap-grid.png (caption mejorado). TODOs: ninguno.

---

# Inicio
1) Regístrate.
2) Toma el primer lock libre (P0 > P1 > P2).
3) Revisa + aplica cambios en la clase.
4) Actualiza SUPERVISION.md y los logs.
