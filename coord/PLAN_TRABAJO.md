# PLAN DE TRABAJO - REDISEÑO CURSO IF0100

**Versión:** 1.0
**Fecha:** 2026-02-07
**Coordinador:** AGENTE_COORDINADOR
**Estado:** PENDIENTE EJECUCIÓN
**Fecha estimada finalización:** 2026-02-10

---

## 1. RESUMEN EJECUTIVO

**Objetivo:** Transformar el curso IF0100 desde un enfoque teórico C#/ASP.NET a un formato práctico Python/FastAPI/PostgreSQL con proyecto integrador TaskFlow.

**Alcance:**
- Crear 6 unidades rediseñadas (0-5)
- Desarrollar proyecto integrador TaskFlow completo
- Crear 17+ clases HTML actualizadas
- Crear 9+ notebooks Jupyter interactivos
- Implementar suite de pruebas completa
- Documentar todo el sistema

**Recursos:** Swarm de 8 agentes especializados

---

## 2. CRONOGRAMA GENERAL

```mermaid
gantt
    title Cronograma de Implementación del Rediseño
    dateFormat  YYYY-MM-DD
    section Fase 1: Planificación
    Coordinador: Plan de trabajo          :done,    p1, 2026-02-07, 4h
    Coordinador: Estructura carpetas       :active,  p2, after p1, 2h

    section Fase 2: Diseño Instruccional
    Diseñador: Objetivos por clase         :         d1, after p1, 4h
    Diseñador: Progresión técnica          :         d2, after d1, 3h
    Diseñador: Rúbricas de evaluación      :         d3, after d2, 3h

    section Fase 3: Contenido Python
    Experto Python: Notebooks U0           :         py1, after p2, 8h
    Experto Python: Notebooks U1           :         py2, after py1, 12h
    Experto Python: Modelos TaskFlow       :         py3, after py2, 6h

    section Fase 4: Contenido Web
    Experto Web: Plantilla HTML base       :         w1, after p2, 4h
    Experto Web: Clases HTML               :         w2, after w1, 12h
    Experto Web: Templates Jinja2          :         w3, after w2, 8h

    section Fase 5: Base de Datos
    Experto DB: Schema SQL                 :         db1, after p2, 6h
    Experto DB: Migraciones                :         db2, after db1, 4h
    Experto DB: Seeds y documentación      :         db3, after db2, 4h

    section Fase 6: Backend API
    Experto API: Configuración FastAPI     :         api1, after py3, 4h
    Experto API: Endpoints CRUD            :         api2, after api1, 8h
    Experto API: Autenticación JWT         :         api3, after api2, 6h

    section Fase 7: Testing
    Experto Testing: Configuración pytest  :         t1, after py3, 4h
    Experto Testing: Tests unitarios       :         t2, after t1, 8h
    Experto Testing: Tests integración     :         t3, after t2, 6h

    section Fase 8: Documentación
    Documentador: README principal         :         doc1, after api3, 3h
    Documentador: API docs                 :         doc2, after doc1, 4h
    Documentador: Guías de instalación     :         doc3, after doc2, 3h

    section Fase 9: QA
    Validador QA: Revisión código          :         qa1, after t3, 6h
    Validador QA: Revisión HTML            :         qa2, after w3, 4h
    Validador QA: Testing E2E              :         qa3, after qa2, 6h

    section Fase 10: Integración
    Coordinador: Integración final         :         i1, after qa3, 6h
    Coordinador: Reporte final             :         i2, after i1, 4h
```

---

## 3. DESGLOSE DETALLADO DE TAREAS

### FASE 1: PLANIFICACIÓN (Agente: Coordinador)

| Tarea ID | Descripción | Duración | Dependencias | Entregable |
|----------|-------------|----------|--------------|------------|
| P1-001 | Leer estrategia completa | 1h | Ninguna | Análisis documentado |
| P1-002 | Analizar estructura actual del curso | 2h | P1-001 | Mapeo de contenido |
| P1-003 | Crear PLAN_TRABAJO.md | 2h | P1-002 | Este documento |
| P1-004 | Crear ESTRUCTURA_NUEVA.md | 1h | P1-003 | Árbol de carpetas |
| P1-005 | Crear estructura física de carpetas | 2h | P1-004 | Directorios creados |
| P1-006 | Actualizar memory-bank/activeContext.md | 1h | P1-005 | Contexto actualizado |

**Total Fase 1:** 9 horas (1 día de trabajo intensivo)

---

### FASE 2: DISEÑO INSTRUCIONAL (Agente: Diseñador)

| Tarea ID | Descripción | Duración | Dependencias | Entregable |
|----------|-------------|----------|--------------|------------|
| D2-001 | Analizar estrategia pedagógica | 2h | P1-003 | Análisis pedagógico |
| D2-002 | Crear objetivos por clase | 4h | D2-001 | planificacion/objetivos-por-clase.md |
| D2-003 | Diseñar progresión técnica | 3h | D2-002 | planificacion/progresion-tecnica.md |
| D2-004 | Crear rúbricas de evaluación | 3h | D2-002 | planificacion/rubricas.md |
| D2-005 | Diseñar guías de taller | 4h | D2-003 | planificacion/guias-taller.md |
| D2-006 | Validar coherencia con estrategia | 2h | D2-005 | Validación documentada |

**Total Fase 2:** 18 horas (2-3 días)

---

### FASE 3: CONTENIDO PYTHON (Agente: Experto Python)

| Tarea ID | Descripción | Duración | Dependencias | Entregable |
|----------|-------------|----------|--------------|------------|
| PY3-001 | Configurar entorno Jupyter | 1h | P1-005 | Environment listo |
| PY3-002 | Crear notebook 00-01-introduccion-python | 2h | PY3-001 | notebooks/unidad-00/00-01.ipynb |
| PY3-003 | Crear notebook 00-02-estructuras-control | 2h | PY3-002 | notebooks/unidad-00/00-02.ipynb |
| PY3-004 | Crear notebook 00-03-estructuras-datos | 2h | PY3-003 | notebooks/unidad-00/00-03.ipynb |
| PY3-005 | Crear notebook 00-04-modulos-errores | 2h | PY3-004 | notebooks/unidad-00/00-04.ipynb |
| PY3-006 | Crear notebook 01-01-clases-objetos | 3h | PY3-005, D2-002 | notebooks/unidad-01/01-01.ipynb |
| PY3-007 | Crear notebook 01-02-encapsulamiento | 3h | PY3-006, D2-002 | notebooks/unidad-01/01-02.ipynb |
| PY3-008 | Crear notebook 01-03-herencia-composicion | 3h | PY3-007, D2-002 | notebooks/unidad-01/01-03.ipynb |
| PY3-009 | Crear notebook 01-04-polimorfismo | 2h | PY3-008, D2-002 | notebooks/unidad-01/01-04.ipynb |
| PY3-010 | Crear notebook 01-05-interfaces | 2h | PY3-009, D2-002 | notebooks/unidad-01/01-05.ipynb |
| PY3-011 | Crear modelo Usuario | 2h | PY3-010, D2-002 | src/taskflow/models/usuario.py |
| PY3-012 | Crear modelo Proyecto | 2h | PY3-011 | src/taskflow/models/proyecto.py |
| PY3-013 | Crear modelo Tarea | 2h | PY3-012 | src/taskflow/models/tarea.py |
| PY3-014 | Crear modelo Comentario | 1h | PY3-013 | src/taskflow/models/comentario.py |
| PY3-015 | Validar todos los notebooks | 2h | PY3-014 | Notebooks ejecutables |
| PY3-016 | Validar código PEP 8 | 2h | PY3-014 | Código conforme |

**Total Fase 3:** 35 horas (4-5 días)

---

### FASE 4: CONTENIDO WEB (Agente: Experto Web)

| Tarea ID | Descripción | Duración | Dependencias | Entregable |
|----------|-------------|----------|--------------|------------|
| W4-001 | Crear plantilla HTML base | 4h | P1-005 | clases-html-v2/templates/clase-template.html |
| W4-002 | Crear assets CSS compartidos | 2h | W4-001 | assets/css/styles-v2.css |
| W4-003 | Crear HTML Unidad 0 (4 clases) | 4h | W4-002, D2-002 | clases-html-v2/clase-00-*.html |
| W4-004 | Crear HTML Unidad 1 (8 clases) | 6h | W4-003, D2-002 | clases-html-v2/clase-01-*.html |
| W4-005 | Crear HTML Unidad 2 (7 clases) | 6h | W4-004, D2-002 | clases-html-v2/clase-02-*.html |
| W4-006 | Crear template Jinja2 base | 2h | W4-005 | src/taskflow/templates/base.html |
| W4-007 | Crear templates de auth | 2h | W4-006 | src/taskflow/templates/login.html, registro.html |
| W4-008 | Crear templates de proyectos | 3h | W4-007 | src/taskflow/templates/proyectos/*.html |
| W4-009 | Crear templates de tareas | 3h | W4-008 | src/taskflow/templates/tareas/*.html |
| W4-010 | Crear template dashboard | 2h | W4-009 | src/taskflow/templates/dashboard.html |
| W4-011 | Integrar HTMX en templates | 3h | W4-010 | Templates interactivos |
| W4-012 | Validar responsive design | 2h | W4-011 | HTML válido |

**Total Fase 4:** 39 horas (4-5 días)

---

### FASE 5: BASE DE DATOS (Agente: Experto DB)

| Tarea ID | Descripción | Duración | Dependencias | Entregable |
|----------|-------------|----------|--------------|------------|
| DB5-001 | Diseñar schema completo | 4h | P1-003 | Documento de diseño |
| DB5-002 | Crear schema.sql | 2h | DB5-001 | database/schema.sql |
| DB5-003 | Crear migración 001 inicial | 2h | DB5-002 | database/migrations/001_initial.sql |
| DB5-004 | Crear migración 002 datos | 2h | DB5-003 | database/migrations/002_data.sql |
| DB5-005 | Crear seed desarrollo | 2h | DB5-004 | database/seeds/desarrollo.sql |
| DB5-006 | Documentar consultas frecuentes | 3h | DB5-005 | database/consultas.md |
| DB5-007 | Crear script de setup | 2h | DB5-006 | database/setup.sql |
| DB5-008 | Validar constraints e índices | 2h | DB5-007 | Schema validado |

**Total Fase 5:** 19 horas (2-3 días)

---

### FASE 6: BACKEND API (Agente: Experto API)

| Tarea ID | Descripción | Duración | Dependencias | Entregable |
|----------|-------------|----------|--------------|------------|
| API6-001 | Configurar FastAPI | 2h | PY3-014 | src/taskflow/api/app.py |
| API6-002 | Crear módulo dependencies | 1h | API6-001 | src/taskflow/api/dependencies.py |
| API6-003 | Crear modelos Pydantic | 3h | API6-002 | src/taskflow/api/schemas.py |
| API6-004 | Crear routes de auth | 4h | API6-003 | src/taskflow/api/routes/auth.py |
| API6-005 | Crear routes de usuarios | 3h | API6-003 | src/taskflow/api/routes/usuarios.py |
| API6-006 | Crear routes de proyectos | 4h | API6-003 | src/taskflow/api/routes/proyectos.py |
| API6-007 | Crear routes de tareas | 4h | API6-006 | src/taskflow/api/routes/tareas.py |
| API6-008 | Implementar JWT auth | 4h | API6-004 | Auth completo |
| API6-009 | Crear middleware de errores | 2h | API6-008 | src/taskflow/api/middleware.py |
| API6-010 | Documentar endpoints OpenAPI | 2h | API6-009 | /docs funcional |

**Total Fase 6:** 29 horas (3-4 días)

---

### FASE 7: TESTING (Agente: Experto Testing)

| Tarea ID | Descripción | Duración | Dependencias | Entregable |
|----------|-------------|----------|--------------|------------|
| T7-001 | Configurar pytest | 2h | PY3-014 | pytest.ini, .coveragerc |
| T7-002 | Crear conftest.py con fixtures | 2h | T7-001 | tests/conftest.py |
| T7-003 | Tests de modelos Usuario | 3h | T7-002, PY3-011 | tests/test_models.py (usuario) |
| T7-004 | Tests de modelos restantes | 3h | T7-003, PY3-014 | tests/test_models.py (completo) |
| T7-005 | Tests de servicios | 6h | T7-004 | tests/test_services.py |
| T7-006 | Tests de repositorios | 4h | T7-005 | tests/test_repositories.py |
| T7-007 | Tests de API endpoints | 6h | API6-010 | tests/test_api.py |
| T7-008 | Configurar coverage | 2h | T7-007 | Coverage > 80% |
| T7-009 | Validar todos los tests pasan | 2h | T7-008 | Test suite verde |

**Total Fase 7:** 30 horas (3-4 días)

---

### FASE 8: DOCUMENTACIÓN (Agente: Documentador)

| Tarea ID | Descripción | Duración | Dependencias | Entregable |
|----------|-------------|----------|--------------|------------|
| DOC8-001 | Crear README principal | 3h | API6-010 | README.md |
| DOC8-002 | Crear guía de instalación | 3h | DOC8-001 | docs/instalacion.md |
| DOC8-003 | Documentar arquitectura | 4h | DOC8-001 | docs/arquitectura.md |
| DOC8-004 | Documentar API endpoints | 4h | API6-010 | docs/api.md |
| DOC8-005 | Crear guía de contribución | 2h | DOC8-004 | docs/contributing.md |
| DOC8-006 | Crear CHANGELOG.md | 1h | DOC8-005 | CHANGELOG.md |
| DOC8-007 | Actualizar docstrings | 4h | PY3-014, API6-010 | Código documentado |

**Total Fase 8:** 21 horas (2-3 días)

---

### FASE 9: QA (Agente: Validador QA)

| Tarea ID | Descripción | Duración | Dependencias | Entregable |
|----------|-------------|----------|--------------|------------|
| QA9-001 | Revisar código Python (PEP 8) | 3h | PY3-016 | coord/reporte-pep8.md |
| QA9-002 | Revisar type hints | 2h | QA9-001 | coord/reporte-types.md |
| QA9-003 | Revisar docstrings | 2h | QA9-002 | coord/reporte-docs.md |
| QA9-004 | Validar HTML (W3C) | 2h | W4-012 | coord/reporte-html.md |
| QA9-005 | Probar notebooks | 3h | PY3-015 | Notebooks validados |
| QA9-006 | Testing E2E manual | 4h | API6-010 | coord/reporte-e2e.md |
| QA9-007 | Verificar enlaces rotos | 2h | QA9-006 | coord/reporte-links.md |
| QA9-008 | Validar responsive design | 2h | QA9-007 | coord/reporte-responsive.md |
| QA9-009 | Crear reporte final QA | 2h | QA9-008 | coord/reporte-qa-final.md |

**Total Fase 9:** 22 horas (2-3 días)

---

### FASE 10: INTEGRACIÓN FINAL (Agente: Coordinador)

| Tarea ID | Descripción | Duración | Dependencias | Entregable |
|----------|-------------|----------|--------------|------------|
| I10-001 | Integrar todos los componentes | 3h | QA9-009 | Sistema integrado |
| I10-002 | Validar criterios de éxito | 2h | I10-001 | Validación completa |
| I10-003 | Actualizar memory-bank | 2h | I10-002 | Contexto actualizado |
| I10-004 | Crear reporte final | 3h | I10-003 | coord/REPORTE_FINAL.md |
| I10-005 | Comunicar cambios al equipo | 1h | I10-004 | Comunicación enviada |

**Total Fase 10:** 11 horas (1-2 días)

---

## 4. ASIGNACIÓN DE AGENTES

### Agente 1: Coordinador
**Responsabilidades:**
- Fase 1: Planificación completa
- Fase 10: Integración final
- Coordinación entre agentes
- Validación de entregables

**Horas estimadas:** 20 horas

### Agente 2: Diseñador Instruccional
**Responsabilidades:**
- Fase 2: Diseño pedagógico
- Objetivos de aprendizaje
- Rúbricas de evaluación
- Guías de taller

**Horas estimadas:** 18 horas

### Agente 3: Experto Python
**Responsabilidades:**
- Fase 3: Contenido Python
- Notebooks Jupyter
- Modelos de dominio
- Código PEP 8 compliant

**Horas estimadas:** 35 horas

### Agente 4: Experto Web
**Responsabilidades:**
- Fase 4: Contenido Web
- HTML de clases
- Templates Jinja2
- Integración HTMX

**Horas estimadas:** 39 horas

### Agente 5: Experto DB
**Responsabilidades:**
- Fase 5: Base de datos
- Schema SQL
- Migraciones
- Seeds y documentación

**Horas estimadas:** 19 horas

### Agente 6: Experto API
**Responsabilidades:**
- Fase 6: Backend API
- FastAPI setup
- Endpoints CRUD
- Autenticación JWT

**Horas estimadas:** 29 horas

### Agente 7: Experto Testing
**Responsabilidades:**
- Fase 7: Testing
- Configuración pytest
- Tests unitarios
- Tests de integración

**Horas estimadas:** 30 horas

### Agente 8: Documentador
**Responsabilidades:**
- Fase 8: Documentación
- README y guías
- Documentación API
- Docstrings

**Horas estimadas:** 21 horas

### Agente 9: Validador QA
**Responsabilidades:**
- Fase 9: QA
- Revisión de código
- Validación HTML
- Testing E2E

**Horas estimadas:** 22 horas

---

## 5. MILESTONES Y ENTREGABLES

| Milestone | Fecha | Entregables | Dependencias |
|-----------|-------|-------------|--------------|
| **M1: Planificación Completa** | 2026-02-07 | PLAN_TRABAJO.md, ESTRUCTURA_NUEVA.md, carpetas creadas | P1-001 a P1-006 |
| **M2: Diseño Pedagógico** | 2026-02-08 | Objetivos, rúbricas, guías | D2-001 a D2-006 |
| **M3: Contenido Python** | 2026-02-09 | Notebooks U0-U1, modelos TaskFlow | PY3-001 a PY3-016 |
| **M4: Contenido Web** | 2026-02-09 | HTML clases, templates Jinja2 | W4-001 a W4-012 |
| **M5: Base de Datos** | 2026-02-09 | Schema, migraciones, seeds | DB5-001 a DB5-008 |
| **M6: Backend API** | 2026-02-10 | FastAPI app, endpoints, auth | API6-001 a API6-010 |
| **M7: Testing** | 2026-02-10 | Suite pytest, coverage > 80% | T7-001 a T7-009 |
| **M8: Documentación** | 2026-02-10 | README, guías, API docs | DOC8-001 a DOC8-007 |
| **M9: QA Completo** | 2026-02-10 | Reportes de validación | QA9-001 a QA9-009 |
| **M10: Sistema Integrado** | 2026-02-10 | TaskFlow funcional, documentado | I10-001 a I10-005 |

---

## 6. GESTIÓN DE RIESGOS

| Riesgo | Probabilidad | Impacto | Mitigación | Plan B |
|--------|--------------|---------|------------|--------|
| Estudiantes muy beginners | Alta | Alto | Unidad 0 de repaso intensivo | Agregar más ejercicios básicos |
| Tiempo insuficiente | Media | Alto | Priorizar MVP sobre features | Eliminar Unidad 5 si es necesario |
| Complejidad FastAPI | Media | Medio | Notebooks progresivos | Usar Flask como alternativa |
| Setup PostgreSQL | Media | Medio | Docker compose listo | Usar SQLite para desarrollo |
| Cambios de estrategia | Baja | Alto | Comunicación clara | Mantener contenido anterior |

---

## 7. CRITERIOS DE ÉXITO

### Pedagógicos
- [ ] Progresión clara notebooks → VSCode
- [ ] Balance teoría-práctica 50-50
- [ ] Proyecto TaskFlow funcional al final
- [ ] Evaluaciones alineadas con objetivos

### Técnicos
- [ ] Todo el código Python sigue PEP 8
- [ ] Type hints en todo el código
- [ ] Docstrings completos (Google style)
- [ ] Tests con coverage > 80%
- [ ] Zero bugs críticos

### de Contenido
- [ ] 17+ clases HTML actualizadas
- [ ] 9+ notebooks interactivos
- [ ] Proyecto TaskFlow completo
- [ ] Documentación exhaustiva
- [ ] Todo el contenido validado por QA

---

## 8. COMUNICACIÓN Y COORDINACIÓN

### Canales de Comunicación
- **Coord/**: Tickets de estado y progreso
- **memory-bank/**: Contexto compartido
- **GitHub Issues**: Seguimiento de tareas
- **Mensajes del sistema**: Notificaciones de progreso

### Actualizaciones de Estado
Cada agente debe actualizar:
1. Su ticket en coord/ al completar cada tarea
2. Documentar bloqueos o problemas encontrados
3. Sugerir mejoras al plan de trabajo

### Reuniones de Sincronización
- **Diaria:** Brief de progreso (5 min)
- **Semanal:** Revisión de milestones (30 min)
- **Final:** Retrospectiva del proyecto (1 hora)

---

## 9. SIGUIENTES PASOS INMEDIATOS

1. **APROBACIÓN**: Revisar y aprobar este plan
2. **EJECUCIÓN FASE 1**: Coordinador crea estructura
3. **EJECUCIÓN PARALELA**: Agentes 2-5 trabajan simultáneamente
4. **INTEGRACIÓN**: Coordinador integra resultados
5. **QA**: Validador revisa todo
6. **LANZAMIENTO**: Comunicar a estudiantes

---

**FIN DEL PLAN DE TRABAJO**

**Estado:** PENDIENTE APROBACIÓN
**Firma:** AGENTE_COORDINADOR
**Fecha:** 2026-02-07
