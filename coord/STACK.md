# IF0100 - Stack objetivo (conversión sobre HTML)

Artefacto fuente (golden): HTML ya validado visualmente.
- SOURCE: clases-html-old/**/*.html  (solo lectura)
- TARGET: clases-html/**/*.html      (edición)

Backend (conceptos y ejemplos):
- Python 3.11+ (POO, excepciones, typing opcional, dataclasses cuando aplique)
- APIs (para ejemplos puntuales): FastAPI (solo lo necesario)

Testing:
- TDD: pytest
- BDD (opcional): behave o pytest-bdd

Frontend:
- Angular (componentes, servicios, routing, formularios reactivos, validación)
- Bootstrap puede mantenerse solo como CSS framework (opcional), pero el framework web es Angular

Datos:
- DB: SQL Server (se mantiene por coherencia con el curso original)
- Acceso desde Python: elegir UNO (pyodbc recomendado por rapidez) y ser consistente

Equivalencia “ADO.NET / DataSet / DataAdapter / datos desconectados”:
- No se elimina el tema; se reemplaza por equivalencia conceptual:
  - Repositorios/servicios + DTOs serializables (JSON)
  - Estado/caché local en frontend + sincronización (offline-first o sync)
  - Explicar la analogía explícitamente en clases 12–16

Git (entregables):
- Por clase/lab: rama feature/<tema>-clase-XX
- Mínimo 3 commits (setup, implementación, pruebas/docs)
- Entrega por tag: clase-XX-v1
