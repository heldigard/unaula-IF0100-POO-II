# IF0100 - Lenguaje de Programación OO II
## Programa del Curso - Stack Python/FastAPI (Actualizado 2026-1)

---

## Información General

| Campo | Valor |
|-------|-------|
| **Código** | IF0100 |
| **Nombre** | Lenguaje de Programación OO II |
| **Pensum** | 302 Pensum 2023-2 |
| **Créditos** | 3 |
| **Nivel** | 4° semestre |
| **Horas presenciales** | 48 horas semestrales |
| **Horas trabajo autónomo** | 96 horas semestrales |
| **Modalidad** | Presencial |
| **Semestre** | 2026-I |
| **Área** | Área de Ingeniería Aplicada |
| **Dominio** | Aplica |
| **Prerrequisito** | IF0094 Lenguaje de Programación OO I |

---

## Descripción del Curso

### Presentación
La Programación busca capacitar a los alumnos para construir programas legibles, correctos, eficientes y fáciles de mantener. Dentro del marco de la Programación orientada a objetos, se introducen una serie de técnicas que favorecen los criterios de calidad: la facilidad para mantener y modificar los programas, y la posibilidad de desarrollar programas fácilmente reutilizables.

### Justificación (Actualizada 2026-1)
Al ingeniero informático que se desempeñe como programador, le interesará conocer **Python** y **FastAPI**. Python es uno de los lenguajes más demandados en el mercado laboral actual, con sintaxis clara y amigable. FastAPI permite construir APIs modernas y de alto rendimiento. El stack **Python + FastAPI + SQLAlchemy** representa el estándar actual para desarrollo backend profesional.

---

## Pregunta Problematizadora

¿Cuáles son las posibles soluciones y los desafíos inherentes asociados a su implementación mediante el lenguaje de programación orientado a objetos II?

---

## Competencias

| Tipo | Competencia |
|------|-------------|
| **Genérica** | Pensamiento crítico |
| **Específica** | Desarrollo de software |

---

## Resultados de Aprendizaje

| Resultado de Aprendizaje | Metodología | Porcentaje | Fecha |
|--------------------------|-------------|------------|-------|
| Conoce los conceptos fundamentales de objetos clases | **Taller** (Entrega 1) | 15% | 26/02/2026 |
| Técnicas de Desarrollo de software | **Laboratorio** (Entrega 2) | 15% | 12/03/2026 |
| Desarrollo Web | **Prototipo** (Entrega 3) | 20% | 26/03/2026 |
| Construye sistemas con persistencia de datos en archivos planos | **Software** (Entrega 4) | 15% | 23/04/2026 |
| Desarrolla sistemas con persistencia en bases de datos | **Software** (Entrega 5) | 15% | 07/05/2026 |
| Conoce e implementa la arquitectura de datos desconectados | **Proyecto** (Sustentación) | 20% | 28/05/2026 |

---

## Contenido Programático

### UNIDAD 1: Conceptos fundamentales de objetos y clases

**Duración:** 4 semanas | **Evaluación:** E1 (15%) - **Taller (Entrega 1: Dominio)** 26/02/2026

**Temas (Python):**
1. **Lógica de programación**
   - Estructuras de control en Python
   - Algoritmos básicos
   - List comprehensions y generadores

2. **Modelamiento de bases de datos**
   - Modelo entidad-relación
   - Normalización
   - Diseño de esquemas

3. **Clases, Objeto y Mensaje**
   - Definición de clases en Python (`class`)
   - Constructor `__init__` y `self`
   - Instanciación de objetos
   - Métodos de instancia, clase y estáticos

4. **Encapsulamiento**
   - Convenio de privacidad (`_atributo`, `__atributo`)
   - Properties con `@property`, `@setter`
   - Dataclasses para modelos simples

5. **Herencia**
   - Clases base y derivadas
   - `super()` y MRO (Method Resolution Order)
   - Herencia múltiple en Python
   - Mixins

6. **Polimorfismo**
   - Duck typing
   - Métodos especiales (`__str__`, `__repr__`, `__eq__`)
   - Clases abstractas con `abc`

7. **Sobrecarga y Sobreescritura**
   - Sobrecarga con `*args` y `**kwargs`
   - Valores por defecto
   - Sobreescritura de métodos

**Metodología:** Clases prácticas creando sistemas en Python. Prácticas de clase y exposiciones. Talleres con retos para aplicar POO.

**Tecnologías:** Python 3.11+, pytest, dataclasses

---

### UNIDAD 2: Técnicas de Desarrollo de software

**Duración:** 2 semanas | **Evaluación:** E2 (15%) - Taller 12/03/2026

**Temas (Python):**
1. **Test Driven Development (TDD)**
   - Ciclo Red-Green-Refactor
   - Escribir tests antes que código
   - pytest: fixtures, parametrize, markers
   - Cobertura con pytest-cov

2. **Behavior Driven Development (BDD)**
   - Especificación con ejemplos
   - Gherkin en español
   - behave para tests BDD
   - Escenarios Given-When-Then

3. **Domain Driven Design (DDD)**
   - Entidades y Value Objects en Python
   - Agregados y Repositorios
   - Bounded Contexts
   - Pydantic para validación de dominio

**Metodología:** Clases magistrales explicando técnicas. Clases prácticas desarrollando sistemas con TDD/BDD. Talleres con retos.

**Tecnologías:** pytest, pytest-cov, behave, hypothesis, Pydantic

---

### UNIDAD 3: Desarrollo Web

**Duración:** 4 semanas | **Evaluación:** E3 (20%) - Proyecto 26/03/2026

**Temas (Python/FastAPI):**
1. **Excepciones y Manejo de Errores**
   - Try-except-finally en Python
   - Excepciones personalizadas
   - HTTPException en FastAPI
   - Manejadores de errores globales

2. **FastAPI**
   - Arquitectura de FastAPI
   - Routers y Path Operations
   - Dependency Injection
   - Middleware
   - OpenAPI automático

3. **Pydantic y Validación**
   - Modelos Pydantic
   - Validación automática
   - Serialización JSON
   - Configuración de modelos

4. **Jinja2 Templates**
   - Templates HTML
   - Herencia de templates
   - Filtros personalizados
   - Context processors

5. **HTML 5**
   - Estructura semántica
   - Formularios HTML5
   - Validaciones nativas
   - Multimedia

6. **HTMX**
   - Interactividad sin JavaScript
   - AJAX simplificado
   - Partial updates
   - Eventos y atributos

7. **Bootstrap**
   - Sistema de grillas
   - Componentes UI
   - Diseño responsivo
   - Integración con FastAPI

**Metodología:** Clases prácticas desarrollando aplicaciones web con FastAPI. Introducción a HTMX para interactividad. Talleres con retos.

**Tecnologías:** FastAPI, Uvicorn, Jinja2, HTMX, Bootstrap 5, Pydantic

---

### UNIDAD 4: Manejo de persistencia (archivos y bases de datos)

**Duración:** 4 semanas | **Evaluaciones:** E4 (15%) + E5 (15%)

**Temas (Python/SQLAlchemy):**
1. **Persistencia en archivos planos** (E4 - 23/04/2026)
   - Lectura y escritura con `pathlib`
   - Archivos JSON con `json` module
   - Archivos CSV con `csv` module
   - Serialización con `pickle`
   - Configuración con archivos YAML/JSON

2. **Introducción a SQLAlchemy**
   - ¿Qué es SQLAlchemy?
   - Engine y Session
   - Modelos declarativos
   - Tipos de columnas

3. **ORM SQLAlchemy**
   - Relaciones (One-to-Many, Many-to-Many)
   - Foreign Keys
   - Lazy loading vs Eager loading
   - Herencia de tablas

4. **CRUD con SQLAlchemy** (E5 - 07/05/2026)
   - Create, Read, Update, Delete
   - Queries con ORM
   - Filtros y ordenamiento
   - Paginación

5. **Transacciones y Migraciones**
   - Sesiones y transacciones
   - Rollback y commit
   - Alembic para migraciones
   - Versionado de esquema

6. **Integración con FastAPI**
   - Dependency Injection de sesiones
   - Endpoints CRUD
   - Validación con Pydantic + SQLAlchemy

**Metodología:** Clases magistrales de SQLAlchemy. Clases prácticas creando sistemas con persistencia. Talleres con retos.

**Tecnologías:** SQLAlchemy 2.0, Alembic, SQLite, PostgreSQL, Pydantic

---

### UNIDAD 5: Arquitectura de datos desconectados

**Duración:** 3 semanas | **Evaluación:** E6 (20%) - Proyecto 28/05/2026

**Temas (Python/Arquitectura):**
1. **Patrón Repository**
   - Abstracción de acceso a datos
   - Interface Repository genérica
   - Implementación con SQLAlchemy
   - Unit of Work pattern

2. **Clean Architecture**
   - Capas: Domain, Use Cases, Infrastructure
   - Inyección de dependencias
   - Inversión de control
   - Separación de responsabilidades

3. **DTOs y Serialización**
   - Dataclasses vs Pydantic
   - Mapeo objeto-relacional
   - Serialización JSON
   - Validación de datos

4. **Caché y Datos Desconectados**
   - Caché en memoria con `cachetools`
   - Redis para caché distribuido
   - Estrategias de invalidación
   - Trabajar offline con datos

5. **APIs REST Avanzadas**
   - Paginación
   - Filtrado y búsqueda
   - Ordenamiento
   - HATEOAS básico

6. **Proyecto Integrador**
   - Aplicación completa FastAPI + SQLAlchemy
   - Arquitectura limpia
   - Testing completo
   - Documentación OpenAPI

**Metodología:** Clases magistrales de arquitectura. Clases prácticas desarrollando proyecto integrador. Sustentación final.

**Tecnologías:** FastAPI, SQLAlchemy, Pydantic, cachetools, Redis (opcional)

---

## Metodología de Enseñanza

### Estrategias Pedagógicas

| Componente | Descripción | % Tiempo |
|------------|-------------|----------|
| Clases magistrales | Exposición de conceptos teóricos | 30% |
| Clases prácticas | Desarrollo de código en clase | 40% |
| Laboratorios | Práctica guiada con ejercicios | 20% |
| Proyectos | Desarrollo de aplicaciones completas | 10% |

### Estrategias de Evaluación (según PDF oficial)
- Prácticas de laboratorios
- Trabajos de campo
- Foros
- Pruebas escritas
- Talleres
- Proyectos de aula
- Ensayos
- Exposiciones
- Diarios de campo
- Informes
- Visitas

---

## Evaluación

### Distribución de Evaluaciones

| Eval | % | Semana | Tipo | Descripción |
|------|---|--------|------|-------------|
| E1 | 15% | 4 | **Taller** | **Entrega 1:** Modelado del Dominio del Proyecto |
| E2 | 15% | 6 | **Laboratorio** | **Entrega 2:** Testing (TDD/BDD) del Proyecto |
| E3 | 20% | 8 | **Prototipo** | **Entrega 3:** API Web y UI (FastAPI + Jinja2) |
| E4 | 15% | 11 | **Software** | **Entrega 4:** Persistencia en Archivos (JSON/CSV) |
| E5 | 15% | 13 | **Software** | **Entrega 5:** Persistencia en BD (SQLAlchemy) |
| E6 | 20% | 16 | **Proyecto** | **Sustentación Final:** Arquitectura Limpia |

### Seguimientos Universitarios

| Seguimiento | Porcentaje | Evaluaciones | Fecha Límite | Estado |
|-------------|------------|--------------|--------------|--------|
| Primer Seguimiento | 50% | E1 (15%) + E2 (15%) + E3 (20%) | 2026-03-27 | ✅ E3: 26/03 |
| Segundo Seguimiento | 80% | E4 (15%) + E5 (15%) | 2026-05-15 | ✅ E5: 07/05 |
| Tercer Seguimiento | 100% | E6 (20%) | 2026-05-28 | ✅ E6: 28/05 |

---

## Laboratorios

| Lab | Tema | Objetivo |
|-----|------|----------|
| 1 | Python Básico | Sintaxis, variables, estructuras de control |
| 2 | POO en Python | Clases, herencia, polimorfismo, dataclasses |
| 3 | Testing con pytest | TDD, fixtures, parametrize, cobertura |
| 4 | FastAPI Básico | Crear API REST con validación Pydantic |
| 5 | SQLAlchemy ORM | Modelos, relaciones, CRUD, transacciones |
| 6 | Proyecto Integrador | Aplicación completa con arquitectura limpia |

---

## Proyectos del Curso (Metodología Incremental)

Este curso se desarrolla como un único **Proyecto de Aula Incremental**. Cada entrega suma funcionalidad sobre la anterior.

### Entrega 1: Modelado de Dominio (Semana 1-4)
- **Objetivo:** Definir las entidades y lógica de negocio
- **Tipo:** Taller
- **Tecnología:** Python 3.11+, dataclasses

### Entrega 2: Calidad y Testing (Semana 5-6)
- **Objetivo:** Asegurar la lógica con TDD/BDD
- **Tipo:** Laboratorio
- **Tecnología:** pytest, behave
- **Requisito:** Debe basarse en el código de la Entrega 1

### Entrega 3: Prototipo Web (Semana 7-8)
- **Objetivo:** Exponer el dominio vía Web/API
- **Tipo:** Prototipo
- **Tecnología:** FastAPI, Jinja2, HTMX
- **Requisito:** Integrar el dominio testeado en la web

### Entrega 4: Persistencia Local (Semana 11)
- **Objetivo:** Guardar datos sin base de datos
- **Tipo:** Software
- **Tecnología:** JSON/CSV, pathlib

### Entrega 5: Persistencia Relacional (Semana 13)
- **Objetivo:** Migrar el almacenamiento a SQL
- **Tipo:** Software
- **Tecnología:** SQLAlchemy ORM, Alembic

### Entrega 6: Sustentación Final (Semana 14-16)
- **Objetivo:** Aplicación completa con Arquitectura Limpia
- **Tipo:** Proyecto
- **Tecnología:** Repository Pattern, DTOs
- **Sustentación:** Defensa del código y arquitectura final

---

## Materiales y Recursos

### Hardware
- Computadores con Windows 10/11, macOS o Linux
- Mínimo 8GB RAM
- Procesador moderno

### Software
- Python 3.11+
- VS Code o PyCharm
- Git y GitHub
- Docker (opcional para PostgreSQL)

---

## Bibliografía

### Básica (Actualizada Python)
1. **"Python Crash Course"** - Eric Matthes, No Starch Press, 3rd Edition
2. **"Fluent Python"** - Luciano Ramalho, O'Reilly Media, 2nd Edition
3. **"Architecture Patterns with Python"** - Harry Percival & Bob Gregory, O'Reilly
4. **FastAPI Documentation** - https://fastapi.tiangolo.com/

### Complementaria
- Documentación oficial de Python (docs.python.org)
- Documentación de SQLAlchemy 2.0
- Real Python tutorials
- Test-Driven Development with Python (Harry Percival)

---

## Stack Tecnológico del Curso

| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Lenguaje** | Python | 3.11+ |
| **Framework Web** | FastAPI | 0.109+ |
| **ORM** | SQLAlchemy | 2.0+ |
| **Templates** | Jinja2 | 3.1+ |
| **Frontend Interactivo** | HTMX | 1.9+ |
| **CSS Framework** | Bootstrap | 5.3+ |
| **Testing** | pytest | 8.0+ |
| **Validación** | Pydantic | 2.5+ |
| **Base de Datos** | SQLite / PostgreSQL | - |
| **Migraciones** | Alembic | 1.13+ |

---

## Fechas Importantes 2026-I

| Evento | Fecha |
|--------|-------|
| Inicio de clases | 2026-02-03 (Martes) |
| Concertación de Evaluación | 2026-02-13 |
| Semana Santa (receso) | 2026-03-30 al 2026-04-03 |
| Primer Seguimiento (50%) | Límite: 2026-03-27 |
| Segundo Seguimiento (80%) | Límite: 2026-05-15 |
| Tercer Seguimiento (100%) | Límite: 2026-05-28 |
| Finalización de clases | 2026-05-29 |

---

**Última actualización:** 2026-02-14
**Estado:** Actualizado a Python/FastAPI para 2026-1
**Nota:** Los resultados de aprendizaje se mantienen según PDF oficial IF0100-v002
