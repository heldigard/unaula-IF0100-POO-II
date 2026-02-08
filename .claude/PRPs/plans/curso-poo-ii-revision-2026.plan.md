# Plan Integral: Revisión y Actualización del Curso IF0100-POO-II

## Resumen Ejecutivo

Este plan documenta la revisión integral del curso IF0100-POO-II para el período 2026-1, transformando el syllabus original basado en C#/.NET a Python + FastAPI, manteniendo los objetivos pedagógicos del pensum 302 de Ingeniería Informática.

## Objetivos de Aprendizaje del Curso

### Objetivo General
Desarrollar competencias avanzadas en programación orientada a objetos utilizando Python y frameworks modernos, integrando técnicas de testing (TDD/BDD), arquitectura (DDD) y desarrollo web con FastAPI.

### Objetivos Específicos
1. Aplicar principios POO: encapsulamiento, herencia, polimorfismo, abstracción
2. Implementar metodologías TDD y BDD con pytest y Gherkin
3. Aplicar conceptos de Domain-Driven Design (DDD)
4. Construir APIs REST con FastAPI y validación con Pydantic
5. Desarrollar proyecto integrador TaskFlow

---

## UX Design

### Before State (Situación Actual)
- Clases de Python básicas ya dictadas (clases 1-2)
- Contenido HTML existe pero no está vinculado a cronograma oficial
- No hay rúbricas de evaluación formales
- Falta integración con notebooks de Colab/VSCode
- Proyecto TaskFlow mencionado pero no estructurado formalmente

### After State (Estado Objetivo)
- 33 sesiones cronogramadas con fechas específicas
- 13 clases HTML existentes mejoradas y conectadas
- 4+ clases HTML nuevas creadas para gaps identificados
- Rúbricas de evaluación para cada entrega
- Notebooks de Colab enlazados desde cada clase
- Proyecto TaskFlow con milestones por semana
- GitHub Pages con índice navegable

---

## Metadata

| Campo | Valor |
|-------|-------|
| Tipo | ENHANCEMENT + NEW_CAPABILITY |
| Complejidad | ALTA |
| Sistemas Afectados | clases-html/, docs/, README.md |
| Dependencias | Bootstrap 5, Prism.js, Python 3.12+, FastAPI |
| Estimación | 20+ tareas |

---

## Fechas Críticas del Curso (Compromisos Docentes 2026-1)

| Evaluación | Porcentaje | Semana | Fecha Límite |
|------------|------------|--------|--------------|
| Parcial 1 | 20% | Semana 7 | ~23/03/2026 |
| Parcial 2 | 20% | Semana 11 | ~04/05/2026 |
| Proyecto Final | 30% | Semana 16 | ~08/06/2026 |
| Seguimiento | 30% | Continuo | - |

---

## Clases Existentes (Inventario Actual)

### Unidad 00 - Fundamentos Python (4 clases)
| Archivo | Título | Estado |
|---------|--------|--------|
| clase-00-introduccion.html | Introducción a Python | ✅ Completo |
| clase-01-variables-tipos.html | Variables y Tipos | ✅ Completo |
| clase-02-estructuras-control.html | Estructuras de Control | ✅ Completo |
| clase-03-estructuras-datos.html | Estructuras de Datos | ✅ Completo |

### Unidad 01 - POO (2 clases)
| Archivo | Título | Estado |
|---------|--------|--------|
| clase-01-clases-objetos.html | Clases y Objetos | ✅ Completo |
| clase-02-encapsulamiento.html | Encapsulamiento | ✅ Completo |

### Unidad 02 - Técnicas de Desarrollo (4 clases)
| Archivo | Título | Estado |
|---------|--------|--------|
| clase-01-tdd-intro.html | TDD Intro | ✅ Completo |
| clase-02-pytest-avanzado.html | pytest Avanzado | ⚠️ Faltante TestClient |
| clase-03-bdd-intro.html | BDD con Gherkin | ✅ Completo |
| clase-04-ddd-intro.html | DDD Intro | ✅ Completo |

### Unidad 03 - Desarrollo Backend (3 clases)
| Archivo | Título | Estado |
|---------|--------|--------|
| clase-01-fastapi-intro.html | FastAPI Intro | ✅ Completo |
| clase-02-pydantic-validacion.html | Pydantic | ✅ Completo |
| clase-03-dependencias.html | Dependencias | ✅ Completo |

---

## Gaps Identificados

### Prioridad ALTA
| Gap | Archivo Afectado | Solución |
|-----|------------------|----------|
| Herencia y Polimorfismo | clase-01-clases-objetos.html | Crear clase-03-herencia-polimorfismo.html |
| Clases Abstractas | clase-02-encapsulamiento.html | Crear clase-04-abc.html |
| Testing FastAPI APIs | clase-02-pytest-avanzado.html | Agregar sección TestClient |
| Persistencia Datos | No existe | Crear clase-04-bd-sqlite.html |

### Prioridad MEDIA
| Gap | Solución |
|-----|----------|
| Metodos Especiales Python | Crear clase-05-metodos-especiales.html |
| Integración Proyecto Final | Crear sesión project-sprint-*.html |

---

## Cronograma Académico 2026-1

### UNIDAD 00 - Fundamentos Python (Clases 1-4)

| Clase | Fecha | Contenido | Entrega |
|-------|-------|-----------|---------|
| 1 | 02/02 | Intro Python + Entorno | - |
| 2 | 09/02 | Variables y Tipos | - |
| 3 | 10/02 | Estructuras Control | - |
| 4 | 16/02 | Estructuras Datos | Lab 1: Scripts Python |

### UNIDAD 01 - POO (Clases 5-8)

| Clase | Fecha | Contenido | Entrega |
|-------|-------|-----------|---------|
| 5 | 17/02 | Clases y Objetos | - |
| 6 | 23/02 | Encapsulamiento | - |
| 7 | 24/02 | **Herencia y Polimorfismo** | Lab 2: Clases POO |
| 8 | 02/03 | **Clases Abstractas** | - |

### UNIDAD 02 - Técnicas Desarrollo (Clases 9-12)

| Clase | Fecha | Contenido | Entrega |
|-------|-------|-----------|---------|
| 9 | 03/03 | TDD Intro | - |
| 10 | 09/03 | pytest Avanzado | Lab 3: Tests Unitarios |
| 11 | 10/03 | BDD Intro | - |
| 12 | 16/03 | DDD Intro | - |

### SEMANA SANTA (Receso)
| Fecha | Estado |
|-------|--------|
| 24-31/03 | Receso |
| 01-07/04 | Receso |

### UNIDAD 03 - Backend + Proyecto (Clases 13-24)

| Clase | Fecha | Contenido | Entrega |
|-------|-------|-----------|---------|
| 13 | 13/04 | FastAPI Intro | - |
| 14 | 14/04 | Pydantic Validación | Lab 4: API Basic |
| 15 | 20/04 | Dependencias + Auth | - |
| 16 | 21/04 | **Testing FastAPI APIs** | - |
| 17 | 27/04 | **Persistencia SQLite** | - |
| 18 | 28/04 | Proyecto TaskFlow | Sprint 1 |
| 19 | 04/05 | Proyecto TaskFlow | - |
| 20 | 05/05 | Proyecto TaskFlow | **PARCIAL 2** |

### PROYECTO FINAL (Clases 21-33)

| Clase | Fecha | Contenido | Entrega |
|-------|-------|-----------|---------|
| 21 | 11/05 | TaskFlow: Autenticación | - |
| 22 | 12/05 | TaskFlow: CRUD Tasks | - |
| 23 | 18/05 | TaskFlow: Testing BDD | Lab 5: BDD Tests |
| 24 | 19/05 | TaskFlow: Documentación | - |
| 25 | 25/05 | TaskFlow: Refactoring | - |
| 26 | 26/05 | TaskFlow: Polish | - |
| 27 | 01/06 | Repaso General | - |
| 28 | 02/06 | Consultas Proyecto | - |
| 29 | 08/06 | **Entrega Final** | **PROYECTO FINAL** |
| 30 | 09/06 | Sustentaciones | - |
| 31+ | Restantes | Sustentaciones | - |

---

## Rúbricas de Evaluación

### Rúbrica: Laboratorio 1 - Scripts Python Basics

| Criterio | Excelente (5) | Bueno (4) | Suficiente (3) | Insuficiente (1-2) |
|----------|---------------|-----------|----------------|---------------------|
| **Funcionalidad** | Código ejecuta sin errores y cumple todos requisitos | Código ejecuta con errores menores | Código ejecuta pero no cumple todos requisitos | No ejecuta o no compila |
| **Estilo PEP 8** | Sigue PEP 8 completamente, código legible | Sigue la mayoría de reglas PEP 8 | Algunos errores de estilo | No sigue PEP 8 |
| **Variables** | Nombres descriptivos, convención snake_case | Nombres adecuados | Nombres confusos | Nombres de una letra |
| **Comentarios** | Documenta el propósito y lógica compleja | Documenta lo esencial | Comentarios insuficientes | Sin comentarios |
| **Ejecución** | Output correcto y formateado | Output correcto | Output parcial | Output incorrecto |

**Porcentaje**: 5% del curso (Parte del 30% Seguimiento)

---

### Rúbrica: Laboratorio 2 - Clases POO

| Criterio | Excelente (5) | Bueno (4) | Suficiente (3) | Insuficiente (1-2) |
|----------|---------------|-----------|----------------|---------------------|
| **Definición Clases** | Clases bien estructuradas con `__init__`, métodos, docstrings | Estructura básica correcta | Clase incompleta | No define clases |
| **Encapsulamiento** | Uso correcto de `@property`, atributos protegidos | Uso parcial | Encapsulamiento incorrecto | Sin encapsulamiento |
| **Herencia** | Herencia aplicada correctamente con `super()` | Herencia básica | Herencia mal aplicada | Sin herencia |
| **Polimorfismo** | Métodos sobreescritos con `@override` | Polimorfismo básico | Concepto mal aplicado | Sin polimorfismo |
| **Tests** | Tests unitarios con pytest covering todo | Tests básicos | Tests insuficientes | Sin tests |

**Porcentaje**: 5% del curso (Parte del 30% Seguimiento)

---

### Rúbrica: Parcial 1 (Semana 7)

| Tema | Porcentaje | Descripción |
|------|------------|-------------|
| Python Basics | 25% | Variables, tipos, estructuras, estructuras de datos |
| POO | 35% | Clases, objetos, encapsulamiento, herencia, polimorfismo |
| Testing | 25% | TDD, pytest básico, ciclo Red-Green-Refactor |
| DDD | 15% | Conceptos básicos de dominio |

**Porcentaje Total**: 20% del curso

---

### Rúbrica: Laboratorio 3 - Tests Unitarios

| Criterio | Excelente (5) | Bueno (4) | Suficiente (3) | Insuficiente (1-2) |
|----------|---------------|-----------|----------------|---------------------|
| **Cobertura** | >90% coverage | 70-90% coverage | 50-70% coverage | <50% coverage |
| **Fixtures** | Uso avanzado de `@pytest.fixture` | Fixtures básicos | Fixture mal usado | Sin fixtures |
| **Parametrización** | `@pytest.mark.parametrize` efectivo | Parametrización parcial | Parametrización mínima | Sin parametrizar |
| **Mocks** | `monkeypatch` y `pytest-mock` correctos | Mocks básicos | Mocks incorrectos | Sin mocks |
| **Asserts** | Asserts descriptivos y variados | Asserts básicos | Asserts mínimos | Asserts incorrectos |

**Porcentaje**: 5% del curso (Parte del 30% Seguimiento)

---

### Rúbrica: Laboratorio 4 - API con FastAPI

| Criterio | Excelente (5) | Bueno (4) | Suficiente (3) | Insuficiente (1-2) |
|----------|---------------|-----------|----------------|---------------------|
| **Endpoints CRUD** | 4+ endpoints funcionales | 3 endpoints | 2 endpoints | <2 endpoints |
| **Validación Pydantic** | Validación completa con mensajes claros | Validación básica | Validación parcial | Sin validación |
| **Status Codes** | Uso correcto de 200,201,404,422,500 | Status básicos | Algunos incorrectos | Sin status codes |
| **Documentación** | Swagger/OpenAPI completo | Documentación básica | Documentación mínima | Sin docs |
| **Testing API** | TestClient con tests completos | Tests básicos | Tests insuficientes | Sin tests |

**Porcentaje**: 5% del curso (Parte del 30% Seguimiento)

---

### Rúbrica: Parcial 2 (Semana 11)

| Tema | Porcentaje | Descripción |
|------|------------|-------------|
| FastAPI | 35% | Endpoints, path/query params, request body |
| Pydantic | 25% | Modelos, validación, schemas |
| Dependencias | 20% | Inyección de dependencias, autenticación |
| pytest FastAPI | 20% | TestClient, fixtures de testing |

**Porcentaje Total**: 20% del curso

---

### Rúbrica: Proyecto Final - TaskFlow (30%)

| Criterio | Porcentaje | Excelente (5) | Bueno (4) | Suficiente (3) | Insuficiente (1-2) |
|----------|------------|---------------|-----------|----------------|---------------------|
| **Funcionalidad** | 30% | Todas las features implementadas y funcionando | Features principales funcionando | Funcionalidad parcial | No funciona |
| **Arquitectura DDD** | 20% | Entities, Value Objects, Aggregates bien definidos | Arquitectura básica DDD | Arquitectura parcial | Sin DDD |
| **API REST** | 20% | API completa con documentación Swagger | API básica funcional | API parcial | API no funcional |
| **Testing** | 15% | >80% coverage con unit + BDD tests | Coverage 50-80% | Coverage <50% | Sin tests |
| **Código Calidad** | 10% | PEP 8, código limpio, bien documentado | Código aceptable | Código con problemas | Código muy malo |
| **Documentación** | 5% | README completo, diagramas UML, video demo | README básico | Documentación mínima | Sin docs |

**Porcentaje Total**: 30% del curso

---

## Archivos a Modificar/Crear

### Modificaciones (Clases Existentes)

| Archivo | Cambio |
|---------|--------|
| clase-01-clases-objetos.html | Agregar notas sobre herencia (hasta crear clase nueva) |
| clase-02-encapsulamiento.html | Agregar referencia a ABC |
| clase-02-pytest-avanzado.html | Agregar sección TestClient FastAPI |
| index.html | Actualizar índice con fechas y navegación |

### Creaciones Nuevas

| Archivo | Descripción | Prioridad |
|---------|-------------|-----------|
| clase-03-herencia-polimorfismo.html | Herencia, polimorfismo, super(), override | ALTA |
| clase-04-clases-abstractas.html | ABC, abstractmethod, patrón template | ALTA |
| clase-04-testing-fastapi.html | TestClient, testing APIs | MEDIA |
| clase-05-persistencia-datos.html | SQLite, SQLAlchemy basics | MEDIA |
| proyecto/taskflow-sprint-1.md | Sprint 1: Setup y modelos | ALTA |
| proyecto/taskflow-sprint-2.md | Sprint 2: API básica | ALTA |
| proyecto/taskflow-sprint-3.md | Sprint 3: Testing y BDD | MEDIA |
| proyecto/taskflow-sprint-4.md | Sprint 4: Polish y docs | MEDIA |
| docs/rubricas.md | Todas las rúbricas consolidadas | ALTA |
| docs/cronograma.md | Calendario con fechas | ALTA |

---

## Integración con Notebooks

### Patrón de Enlace para Cada Clase

```html
<div class="alert-tip">
    <strong>🚀 Práctica en Notebook:</strong>
    <a href="https://colab.research.google.com/github/unaula/course-notebooks/blob/main/unidad-01/clase-03.ipynb" target="_blank">
        Abrir en Google Colab
    </a>
    |
    <a href="vscode://folder/F:/UNAULA/IF0100-POO-II/notebooks/unidad-01/clase-03.ipynb">
        Abrir en VSCode
    </a>
</div>
```

### Estructura de Notebooks Sugerida

```
notebooks/
├── unidad-00/
│   ├── clase-00-introduccion.ipynb
│   ├── clase-01-variables-tipos.ipynb
│   ├── clase-02-estructuras-control.ipynb
│   └── clase-03-estructuras-datos.ipynb
├── unidad-01/
│   ├── clase-01-clases-objetos.ipynb
│   ├── clase-02-encapsulamiento.ipynb
│   ├── clase-03-herencia-polimorfismo.ipynb  # NUEVO
│   └── clase-04-clases-abstractas.ipynb       # NUEVO
├── unidad-02/
│   ├── clase-01-tdd-intro.ipynb
│   ├── clase-02-pytest-avanzado.ipynb
│   ├── clase-03-bdd-intro.ipynb
│   └── clase-04-ddd-intro.ipynb
└── unidad-03/
    ├── clase-01-fastapi-intro.ipynb
    ├── clase-02-pydantic-validacion.ipynb
    ├── clase-03-dependencias.ipynb
    └── clase-04-testing-fastapi.ipynb          # NUEVO
```

---

## Métricas de Progreso del Curso

| Semana | Fecha | Clases | Entregas | Porcentaje Acumulado |
|--------|-------|--------|----------|---------------------|
| 1 | 02-10/02 | 1-3 | - | 0% |
| 2 | 16-17/02 | 4-5 | Lab 1 | 5% |
| 3 | 23-24/02 | 6-7 | Lab 2 | 10% |
| 4 | 02-03/03 | 8-9 | - | 10% |
| 5 | 09-10/03 | 10-11 | Lab 3 | 15% |
| 6 | 16-17/03 | 12-13 | - | 15% |
| 7 | 23-24/03 | 14-15 | **PARCIAL 1** | **35%** |
| 8 | 30-31/03 | - | Semana Santa | 35% |
| 9 | 01-07/04 | - | Semana Santa | 35% |
| 10 | 13-14/04 | 16-17 | Lab 4 | 40% |
| 11 | 20-21/04 | 18-19 | **PARCIAL 2** | **60%** |
| 12 | 27-28/04 | 20-21 | Lab 5 BDD | 65% |
| 13 | 04-05/05 | 22-23 | - | 65% |
| 14 | 11-12/05 | 24-25 | - | 65% |
| 15 | 18-19/05 | 26-27 | - | 65% |
| 16 | 25-26/05 | 28-29 | - | 70% |
| 17 | 01-02/06 | 30-31 | **PROYECTO FINAL** | **100%** |

---

## Acceptance Criteria

- [ ] Clases HTML existentes verificadas y mejoradas
- [ ] Clases nuevas creadas para gaps identificados (herencia, ABC, testing APIs)
- [ ] Cronograma académico con fechas específicas publicado
- [ ] Rúbricas de evaluación para cada entrega creadas
- [ ] Integración con notebooks de Colab/VSCode configurada
- [ ] Proyecto TaskFlow con sprints documentados
- [ ] GitHub Pages actualizado con nuevo índice navegable

---

## Risks and Mitigations

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Tiempo insuficiente para crear contenido | ALTA | ALTA | Priorizar gaps críticos (herencia, ABC) |
| Cambios en calendario académico | MEDIA | MEDIA | Mantener flexibilidad en cronograma |
| Dificultad estudiantes con conceptos POO | ALTA | MEDIA | Agregar ejercicios extras en notebooks |
| Complejidad proyecto TaskFlow | MEDIA | ALTA | Dividir en sprints pequeños |

---

## Notes

1. El Lunes 9 de febrero ya es la Clase 2 (según contexto del usuario)
2. Las clases de Python básico (Unidad 00) ya fueron dictadas como refresh
3. La transición de C# a Python mantiene todos los objetivos pedagógicos del syllabus original
4. FastAPI reemplaza ASP.NET Core con curva de aprendizaje más suave
5. pytest + behave reemplaza MSTest + SpecFlow manteniendo metodología TDD/BDD
