# TaskFlow - Sistema de Gestion de Tareas

**Curso:** IF0100 - Lenguaje de Programacion OO II
**Institucion:** UNAULA
**Semestre:** 2026-I
**Stack:** Python 3.11+, FastAPI, PostgreSQL, Jinja2, HTMX

---

## Descripcion del Proyecto

TaskFlow es un sistema completo de gestion de proyectos y tareas desarrollado durante el curso IF0100. Los estudiantes construyen el sistema iterativamente desde cero, aplicando conceptos de POO, TDD, BDD, DDD, FastAPI y desarrollo web.

### Enfoque Pedagogico

Este curso utiliza un enfoque practico centrado en el proyecto integrador:

1. **Aprendizaje Progresivo:** Notebooks Jupyter -> Python puro -> VSCode -> Produccion
2. **Construccion Iterativa:** El sistema evoluciona desde MVP hasta producto completo
3. **Balance Teoria-Practica:** 50% contenido HTML teorico + 50% codigo practico
4. **Tecnicas Profesionales:** TDD, BDD, DDD, arquitectura limpia, testing

---

## Caracteristicas

### M1: Configuracion (Semana 9-10)
- Estructura del proyecto Clean Architecture
- Entorno de desarrollo configurado
- Repositorio Git inicializado

### M2: Modelos (Semana 11-12)
- Entidades de dominio (User, Task, Project)
- Value Objects con Pydantic
- Repositories basicos

### M3: API Core (Semana 13-14)
- Endpoints CRUD funcionando
- Validacion con Pydantic
- Sistema de dependencias

### M4: Testing (Semana 15) - 15% Proyecto Parcial
- Tests con >80% cobertura
- pytest fixtures y mocks
- BDD con Behave

### M5: Persistencia (Semana 16)
- SQLAlchemy integrado
- Migraciones de base de datos
- Seeds de datos

### M6: Entrega Final (Semana 17) - 20% Proyecto Final
- Sistema completo documentado
- API REST funcional
- Tests automatizados
- Dashboard web

---

## Instalacion

### Prerrequisitos

- Python 3.11+
- PostgreSQL 15+
- Git
- (Opcional) Docker y Docker Compose

### Pasos de Instalacion

#### 1. Clonar el Repositorio

```bash
git clone https://github.com/heldigard/unaula-IF0100-POO-II.git
cd IF0100-POO-II
```

#### 2. Crear Entorno Virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

#### 4. Configurar Variables de Entorno

Crear archivo `.env` en la raiz del proyecto:

```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar .env con tus valores
# DATABASE_URL=postgresql://usuario:password@localhost:5432/taskflow
# SECRET_KEY=tu-clave-secreta-aqui
```

#### 5. Crear Base de Datos

```bash
# Conectarse a PostgreSQL
psql -U postgres

# Crear base de datos
CREATE DATABASE taskflow;
\q

# Ejecutar schema
psql -U postgres -d taskflow -f database/schema.sql

# Ejecutar seeds (datos de prueba)
psql -U postgres -d taskflow -f database/seeds/desarrollo.sql
```

#### 6. Ejecutar el Servidor de Desarrollo

```bash
uvicorn src.taskflow.api.app:app --reload
```

#### 7. Acceder a la Aplicacion

- **API:** http://localhost:8000
- **Documentacion API (Swagger):** http://localhost:8000/docs
- **Documentacion API (ReDoc):** http://localhost:8000/redoc
- **Frontend:** http://localhost:8000

---

## Estructura del Proyecto

```
IF0100-POO-II/
|-- README.md                    # Este archivo
|-- requirements.txt             # Dependencias Python
|-- .env.example                 # Plantilla de variables de entorno
|-- pyproject.toml              # Configuracion del proyecto
|-- pytest.ini                  # Configuracion de tests
|
|-- memory-bank/                # Documentacion del proyecto
|   |-- projectbrief.md         # Vision general del proyecto
|   |-- productContext.md       # Contexto del producto
|   |-- systemPatterns.md       # Patrones de diseno
|   |-- techContext.md          # Contexto tecnologico
|   |-- activeContext.md        # Contexto activo
|   |-- progress.md             # Progreso del proyecto
|   |-- ESTRATEGIA_REDISENIO.md # Estrategia de redisenio
|   |-- instructions/           # Instrucciones para agentes AI
|   `-- tasks/                  # Tareas del proyecto
|
|-- notebooks/                  # Jupyter Notebooks de aprendizaje
|   |-- unidad-00/             # Fundamentos Python
|   `-- unidad-01/             # POO Avanzada
|
|-- clases-html-v2/            # Contenido HTML de teoria (clases)
|
|-- src/taskflow/              # Codigo fuente del proyecto
|   |-- __init__.py
|   |-- models/                # Modelos de dominio
|   |   |-- __init__.py
|   |   |-- usuario.py
|   |   |-- proyecto.py
|   |   |-- tarea.py
|   |   `-- comentario.py
|   |-- schemas/               # Schemas Pydantic (DTOs)
|   |   |-- __init__.py
|   |   |-- usuario.py
|   |   |-- proyecto.py
|   |   |-- tarea.py
|   |   |-- comentario.py
|   |   `-- auth.py
|   |-- repositories/          # Acceso a datos
|   |   |-- __init__.py
|   |   |-- base.py
|   |   |-- usuario_repo.py
|   |   |-- proyecto_repo.py
|   |   |-- tarea_repo.py
|   |   `-- comentario_repo.py
|   |-- services/              # Logica de negocio
|   |   |-- __init__.py
|   |   |-- usuario_service.py
|   |   |-- proyecto_service.py
|   |   `-- tarea_service.py
|   |-- api/                   # Aplicacion FastAPI
|   |   |-- __init__.py
|   |   |-- app.py             # Aplicacion principal
|   |   |-- config.py          # Configuracion
|   |   |-- security.py        # Seguridad y JWT
|   |   |-- dependencies.py    # Dependencias FastAPI
|   |   `-- routes/            # Rutas de la API
|   |       |-- __init__.py
|   |       |-- auth.py        # Autenticacion
|   |       |-- usuarios.py    # CRUD usuarios
|   |       |-- proyectos.py   # CRUD proyectos
|   |       `-- tareas.py      # CRUD tareas
|   `-- templates/             # Templates Jinja2
|       |-- base.html
|       |-- index.html
|       |-- login.html
|       |-- dashboard.html
|       |-- proyectos/
|       `-- tareas/
|
|-- tests/                     # Suite de tests pytest
|   |-- __init__.py
|   |-- conftest.py            # Fixtures compartidas
|   |-- test_models.py         # Tests de modelos
|   |-- test_services.py       # Tests de servicios
|   `-- test_api.py            # Tests de API
|
|-- database/                  # Scripts de base de datos
|   |-- schema.sql             # Esquema completo
|   |-- migrations/            # Migraciones
|   |   `-- 001_initial.sql
|   `-- seeds/                 # Datos de prueba
|       `-- desarrollo.sql
|
|-- planificacion/             # Documentacion de planificacion
|   |-- syllabus.md            # Programa del curso
|   |-- cronograma.md          # Calendario
|   `-- cronograma-actualizado-2026.md
|
|-- evaluaciones/              # Guías de evaluaciones
|   |-- evaluacion-01-*.md
|   |-- evaluacion-02-*.md
|   `-- ...
|
|-- assets/                    # Recursos estaticos
|   |-- css/                   # Estilos personalizados
|   |-- js/                    # JavaScript
|   `-- infografias/           # Diagramas
|
|-- docs/                      # Documentacion adicional
|   |-- instalacion.md         # Guia de instalacion detallada
|   |-- arquitectura.md        # Diagramas y arquitectura
|   `-- api.md                 # Documentacion de la API
|
|-- coord/                     # Coordinacion del proyecto
|   `-- apply_syntax_highlight.py
|
`-- .venv/                     # Entorno virtual (gitignored)
```

---

## Tecnologias Utilizadas

| Componente | Tecnologia | Version |
|-----------|-----------|---------|
| **Backend** | FastAPI | 0.109+ |
| **Lenguaje** | Python | 3.11+ |
| **Base de datos** | PostgreSQL | 15+ |
| **ORM** | SQLAlchemy | 2.0+ |
| **Autenticacion** | JWT | python-jose |
| **Password Hashing** | bcrypt | passlib |
| **Frontend** | Jinja2 | 3.1+ |
| **Interactividad** | HTMX | 1.9+ |
| **CSS Framework** | Bootstrap 5 | 5.3+ |
| **Testing** | pytest | 7.4+ |
| **HTTP Client** | httpx | 0.26+ |
| **Validacion** | Pydantic | 2.5+ |
| **Migraciones** | Alembic | 1.13+ |

---

## Testing

### Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar con salida detallada
pytest -v

# Ejecutar solo tests de modelos
pytest tests/test_models.py

# Ejecutar solo tests de API
pytest tests/test_api.py
```

### Coverage

```bash
# Ejecutar con coverage
pytest --cov=src/taskflow --cov-report=html

# Abrir reporte de coverage
# Windows: start htmlcov/index.html
# Linux/Mac: open htmlcov/index.html
```

### Fixtures Disponibles

- `db_session`: Sesion de base de datos para pruebas
- `client`: Cliente de prueba FastAPI
- `usuario_data`: Datos de prueba para usuario
- `proyecto_data`: Datos de prueba para proyecto

---

## Modelo de Datos

### Entidades Principales

```mermaid
erDiagram
    usuarios ||--o{ proyectos : "crea"
    usuarios ||--o{ tareas : "asignado_a"
    usuarios ||--o{ tareas : "crea"
    usuarios ||--o{ comentarios : "escribe"
    proyectos ||--o{ tareas : "contiene"
    tareas ||--o{ comentarios : "tiene"

    usuarios {
        int id PK
        string username UK
        string email UK
        string password_hash
        string nombre_completo
        bool activo
        timestamp creado_en
        timestamp actualizado_en
    }

    proyectos {
        int id PK
        string nombre
        text descripcion
        int usuario_id FK
        string estado
        timestamp creado_en
        timestamp actualizado_en
    }

    tareas {
        int id PK
        string titulo
        text descripcion
        string estado
        string prioridad
        int proyecto_id FK
        int asignado_a FK
        int creada_por FK
        date fecha_limite
        timestamp completada_en
        timestamp creada_en
        timestamp actualizada_en
    }

    comentarios {
        int id PK
        text contenido
        int tarea_id FK
        int usuario_id FK
        timestamp creado_en
    }
```

---

## API Endpoints

### Autenticacion

| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| POST | `/api/auth/register` | Registrar nuevo usuario |
| POST | `/api/auth/login` | Iniciar sesion |
| POST | `/api/auth/refresh` | Renovar token JWT |
| GET | `/api/auth/me` | Obtener usuario actual |

### Usuarios

| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| GET | `/api/usuarios` | Listar usuarios |
| GET | `/api/usuarios/{id}` | Obtener usuario por ID |
| PUT | `/api/usuarios/{id}` | Actualizar usuario |
| DELETE | `/api/usuarios/{id}` | Eliminar usuario (soft delete) |

### Proyectos

| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| GET | `/api/proyectos` | Listar proyectos |
| POST | `/api/proyectos` | Crear proyecto |
| GET | `/api/proyectos/{id}` | Obtener proyecto por ID |
| PUT | `/api/proyectos/{id}` | Actualizar proyecto |
| DELETE | `/api/proyectos/{id}` | Eliminar proyecto |
| GET | `/api/proyectos/{id}/tareas` | Obtener tareas de proyecto |

### Tareas

| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| GET | `/api/tareas` | Listar tareas (con filtros) |
| POST | `/api/tareas` | Crear tarea |
| GET | `/api/tareas/{id}` | Obtener tarea por ID |
| PUT | `/api/tareas/{id}` | Actualizar tarea |
| DELETE | `/api/tareas/{id}` | Eliminar tarea |
| PATCH | `/api/tareas/{id}/estado` | Cambiar estado de tarea |
| GET | `/api/tareas/{id}/comentarios` | Obtener comentarios de tarea |
| POST | `/api/tareas/{id}/comentarios` | Agregar comentario |

---

## Guias de Clase

### Unidades del Curso

| Unidad | Clases | Nombre | Enfoque |
|--------|--------|--------|---------|
| 0 | 4 | Fundamentos de Python | Repaso intensivo |
| 1 | 4 | POO Avanzada con Python | Clases, herencia, polimorfismo |
| 2 | 4 | Tecnicas de Desarrollo | TDD, BDD, DDD |
| 3 | 5 | Desarrollo Backend con FastAPI | API REST, Pydantic, Testing |

**Total:** 17 clases de 2 horas (16 efectivas + 1 cancelada por Semana Santa)

### Ver Clases Online

Las 17 clases del curso estan disponibles en formato HTML interactivo:

**[IF0100 GitHub Pages](https://heldigard.github.io/unaula-IF0100-POO-II/)**

---

## Sistema de Evaluacion

### Estructura Oficial (2026-I)

```
Primer Seguimiento (50%): 15% + 15% + 20% antes de Semana Santa
Segundo Seguimiento (80%): +15% + 15% antes del 15 de mayo
Tercer Seguimiento (100%): +20% antes del 28 de mayo
```

| Seguimiento | Evaluacion | Peso | Fecha | Tema |
|-------------|------------|------|-------|------|
| **Primer (50%)** | Quiz 1 | 15% | 17/02/2026 | Fundamentos Python |
| **Primer (50%)** | Taller 1 | 15% | 10/03/2026 | Modelado OO |
| **Primer (50%)** | Parcial 1 | 20% | 17/03/2026 | Python + POO |
| **Segundo (80%)** | Taller 2 | 15% | 14/04/2026 | TDD + Testing |
| **Segundo (80%)** | Proyecto Parcial | 15% | 12/05/2026 | TaskFlow API CRUD |
| **Tercer (100%)** | Proyecto Final | 20% | 26/05/2026 | TaskFlow Completo |

### Fechas Limite Oficiales

| Seguimiento | Porcentaje Acumulado | Fecha Limite |
|-------------|----------------------|--------------|
| Primer Seguimiento | 50% | 27/03/2026 (antes de Semana Santa) |
| Segundo Seguimiento | 80% | 15/05/2026 |
| Tercer Seguimiento | 100% | 28/05/2026 |

---

## Contribucion

Este es un proyecto educativo desarrollado durante el curso IF0100. Las contribuciones deben seguir:

1. **Code Style:** PEP 8 + Black formatting
2. **Type Hints:** Todas las funciones deben tener type hints
3. **Docstrings:** Google style docstrings
4. **Tests:** Coverage > 80%
5. **Commits:** Mensajes de commit claros y descriptivos

---

## Recursos de Aprendizaje

### Documentacion Oficial

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [HTMX Documentation](https://htmx.org/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)

### Tutoriales Recomendados

- [Real Python](https://realpython.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)

---

## Autores

- **Curso:** IF0100 - Lenguaje de Programacion Orientada a Objetos II
- **Institucion:** UNAULA (Universidad Autonoma Latinoamericana)
- **Semestre:** 2026-I
- **Docente:** [Por definir]

---

## Licencia

MIT License - Ver archivo LICENSE para detalles

---

## Soporte

Para preguntas o problemas relacionados con el curso:

1. Revisar la documentacion en `docs/`
2. Consultar las clases en HTML
3. Revisar los notebooks en `notebooks/`
4. Contactar al docente

---

**UNAULA - Ingenieria Informatica - 2026-I**
