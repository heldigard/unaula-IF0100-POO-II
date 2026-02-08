# TaskFlow - Sistema de Gestión de Tareas

**Curso:** IF0100 - Programación Orientada a Objetos II
**Periodo:** 2026-I
**Institución:** UNAULA - Universidad Autónoma Latinoamericana

---

## Tabla de Contenidos

1. [Descripción del Proyecto](#1-descripción-del-proyecto)
2. [Configuración del Entorno](#2-configuración-del-entorno)
3. [Ejecución del Proyecto](#3-ejecución-del-proyecto)
4. [Estructura del Proyecto](#4-estructura-del-proyecto)
5. [Testing](#5-testing)
6. [Fases del Proyecto (Sprints)](#6-fases-del-proyecto-sprints)
7. [Criterios de Evaluación](#7-criterios-de-evaluación)
8. [Recursos](#8-recursos)
9. [Autores](#9-autores)

---

## 1. Descripción del Proyecto

### 1.1 ¿Qué es TaskFlow?

**TaskFlow** es un sistema de gestión de tareas RESTful que permite a usuarios y equipos organizar, priorizar y dar seguimiento a sus actividades diarias de manera eficiente. El sistema implementa principios de Programación Orientada a Objetos, metodologías ágiles y mejores prácticas de desarrollo de software.

### 1.2 Funcionalidades Principales

| Módulo | Funcionalidad | Descripción |
|--------|---------------|-------------|
| **Usuarios** | Registro y autenticación | Creación de cuentas, login, gestión de perfiles |
| **Proyectos** | Gestión de proyectos | Crear, editar, eliminar y organizar proyectos |
| **Tareas** | CRUD de tareas | Crear, leer, actualizar y eliminar tareas |
| **Categorías** | Clasificación | Organizar tareas por categorías y prioridades |
| **Estados** | Flujo de trabajo | Seguimiento del estado de cada tarea |

### 1.3 Arquitectura General

```
┌─────────────────────────────────────────────────────────────┐
│                      TaskFlow System                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐       │
│  │   Frontend  │◄──►│   FastAPI   │◄──►│   Backend   │       │
│  │   (React)   │    │   REST API  │    │   Python    │       │
│  └─────────────┘    └─────────────┘    └─────────────┘       │
│                           │                   │              │
│                           ▼                   ▼              │
│                   ┌─────────────┐    ┌─────────────┐       │
│                   │  Pydantic   │    │ SQLAlchemy  │       │
│                   │  (Models)   │    │   (ORM)     │       │
│                   └─────────────┘    └─────────────┘       │
│                                          │                  │
│                                          ▼                  │
│                                   ┌─────────────┐       │
│                                   │  SQLite/    │       │
│                                   │ PostgreSQL  │       │
│                                   └─────────────┘       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.4 Patrones de Diseño Implementados

- **Repository Pattern**: Abstracción de la capa de datos
- **Dependency Injection**: Gestión de dependencias con FastAPI
- **Factory Pattern**: Creación de objetos complejos
- **Strategy Pattern**: Manejo de diferentes estrategias de persistencia

---

## 2. Configuración del Entorno

### 2.1 Requisitos Previos

```
Python 3.12+
Git
```

### 2.2 Creación del Entorno Virtual

#### Opción 1: Usando venv (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows CMD)
venv\Scripts\activate

# Activar entorno virtual (Windows PowerShell)
venv\Scripts\Activate.ps1

# Activar entorno virtual (Git Bash/Mac/Linux)
source venv/bin/activate
```

#### Opción 2: Usando Poetry (Opcional)

```bash
# Instalar Poetry si no está instalado
pip install poetry

# Configurar proyecto
poetry install

# Activar entorno virtual
poetry shell
```

### 2.3 Instalación de Dependencias

```bash
# Con pip (después de activar venv)
pip install -r requirements.txt

# Verificar instalación
python --version  # Debe ser 3.12+
fastapi --version
pytest --version
```

### 2.4 Configuración de Variables de Entorno

Crear archivo `.env` en la raíz del proyecto (`proyecto/.env`):

```bash
# Base de datos
DATABASE_URL=sqlite:///./taskflow.db

# Seguridad
SECRET_KEY=your-secret-key-change-this-in-production

# Aplicación
APP_NAME=TaskFlow
APP_VERSION=1.0.0

# Entorno
ENVIRONMENT=development
```

---

## 3. Ejecución del Proyecto

### 3.1 Desarrollo

```bash
# Asegúrate de estar en el directorio 'proyecto'
cd F:/UNAULA/IF0100-POO-II/proyecto

# Activar entorno virtual (si no está activo)
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Git Bash/Mac/Linux

# Ejecutar servidor de desarrollo
uvicorn src.taskflow.api.main:app --reload --host 0.0.0.0 --port 8000
```

### 3.2 Verificación

El servidor debería iniciar con mensajes similares a:

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 3.3 Accesos

| Entorno | URL | Descripción |
|---------|-----|-------------|
| Local | http://localhost:8000 | API principal |
| Root | http://localhost:8000/ | Información de la API |
| Health | http://localhost:8000/health | Endpoint de salud |
| Swagger | http://localhost:8000/docs | Documentación Swagger UI |
| ReDoc | http://localhost:8000/redoc | Documentación ReDoc |

### 3.4 Verificación de Endpoints

```bash
# Verificar endpoint raíz
curl http://localhost:8000/

# Verificar health check
curl http://localhost:8000/health

# Verificar documentación Swagger
# Abrir en navegador: http://localhost:8000/docs
```

---

## 4. Estructura del Proyecto

### 4.1 Árbol de Directorios Actual

```
proyecto/
├── README.md                  # Este archivo
├── requirements.txt           # Dependencias del proyecto
├── requirements-dev.txt       # Dependencias de desarrollo (opcional)
├── .env.example              # Ejemplo de variables de entorno
├── .gitignore                # Archivos ignorados por Git
│
├── sprint-1-setup.md         # Guía Sprint 1
├── sprint-2-api.md           # Guía Sprint 2
├── sprint-3-testing.md       # Guía Sprint 3
├── sprint-4-finalizacion.md  # Guía Sprint 4
│
├── src/                       # Código fuente
│   └── taskflow/              # Paquete principal
│       ├── __init__.py
│       │
│       ├── core/              # Núcleo compartido
│       │   ├── __init__.py
│       │   ├── config.py      # Configuración de la aplicación
│       │   └── exceptions.py  # Excepciones personalizadas
│       │
│       ├── domain/            # Capa de dominio (DDD)
│       │   ├── __init__.py
│       │   ├── entities.py    # Entidades del dominio
│       │   └── value_objects.py  # Value Objects
│       │
│       ├── application/       # Capa de aplicación
│       │   ├── __init__.py
│       │   └── services.py    # Servicios de aplicación
│       │
│       ├── infrastructure/    # Capa de infraestructura
│       │   ├── __init__.py
│       │   ├── database.py    # Configuración de BD
│       │   └── repositories.py  # Implementación de repositorios
│       │
│       └── api/               # Capa de API
│           ├── __init__.py
│           ├── main.py        # Punto de entrada FastAPI
│           └── dependencies.py # Dependencias de FastAPI
│
├── tests/                     # Tests (por crear)
│   ├── __init__.py
│   ├── conftest.py           # Configuración de pytest
│   ├── unit/                 # Tests unitarios
│   └── integration/          # Tests de integración
│
├── features/                  # Tests BDD (behave) (por crear)
│   ├── environment.py         # Configuración BDD
│   └── *.feature             # Archivos de escenarios
│
└── docs/                      # Documentación adicional (opcional)
    ├── api.md                # Documentación de API
    └── architecture.md       # Documentación de arquitectura
```

### 4.2 Descripción de Módulos

#### 4.2.1 Capa de Dominio (`domain/`)

Contiene las reglas de negocio puras, sin dependencias de frameworks:

- **Entities**: Objetos del dominio con identidad propia
- **Value Objects**: Objetos inmutables sin identidad

```python
# Ejemplo actual: entities.py
@dataclass
class Task(Entity):
    """Task entity representing a work item."""
    title: str
    description: str | None = None
    status: str = "pending"
    priority: str = "medium"
    due_date: datetime | None = None
    assigned_to: UUID | None = None
    project_id: UUID | None = None
```

#### 4.2.2 Capa de Aplicación (`application/`)

Orquesta los casos de uso y coordina la lógica de negocio:

```python
# Ejemplo: services.py
class TaskService:
    """Service for managing tasks."""

    def __init__(self, task_repository):
        self.task_repository = task_repository
```

#### 4.2.3 Capa de Infraestructura (`infrastructure/`)

Implementaciones técnicas de los contratos del dominio:

```python
# Ejemplo: database.py
def init_db():
    """Initialize database."""
    # Create tables, run migrations, etc.
```

#### 4.2.4 Capa de API (`api/`)

Endpoints REST y configuración de FastAPI:

```python
# Ejemplo: main.py
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Task Management API with clean architecture"
)
```

---

## 5. Testing

### 5.1 Configuración de Tests

```bash
# Crear directorio de tests
mkdir -p tests/unit tests/integration
```

### 5.2 Tests Unitarios

```bash
# Ejecutar todos los tests unitarios
pytest tests/unit/ -v

# Con cobertura
pytest tests/unit/ --cov=taskflow --cov-report=term-missing

# Reporte HTML de cobertura
pytest tests/unit/ --cov=taskflow --cov-report=html
# Abrir: htmlcov/index.html
```

### 5.3 Tests de Integración

```bash
# Tests de API
pytest tests/integration/ -v
```

### 5.4 Tests BDD (behave)

```bash
# Ejecutar todos los features
behave features/

# Feature específico
behave features/tasks.feature

# Con verbose
behave -v
```

### 5.5 Verificar que pytest funciona

```bash
# Verificar versión
pytest --version

# Test simple
python -m pytest --version
```

---

## 6. Fases del Proyecto (Sprints)

### 6.1 Roadmap General

| Sprint | Semanas | Entregables | Peso |
|--------|---------|-------------|------|
| Sprint 1 | 8 | Fundamentos | 20% |
| Sprint 2 | 10 | API Backend | 25% |
| Sprint 3 | 12 | Persistencia | 25% |
| Sprint 4 | 14 | Testing y Calidad | 15% |
| Sprint 5 | 16 | Finalización | 15% |

### 6.2 Sprint 1: Fundamentos (Semana 8)

**Objetivo:** Establecer las bases del proyecto con el dominio modelado.

#### Entregables

| Componente | Descripción | Criterio de Aceptación |
|------------|-------------|------------------------|
| Setup del proyecto | Estructura inicial con venv | requirements.txt configurado |
| Entidades del dominio | User, Task, Project, Category | Tests unitarios pasando |
| Value Objects | TaskStatus, Priority | Tests unitarios pasando |
| Documentación | README.md actualizado | Completo y actual |

#### Criterios de Evaluación Sprint 1

| Criterio | Porcentaje |
|----------|------------|
| Estructura del proyecto | 20% |
| Entidades del dominio (POO) | 30% |
| Value Objects y enums | 20% |
| Tests unitarios (>50% cobertura) | 20% |
| Documentación | 10% |

#### Comandos Útiles

```bash
# Crear estructura de dominio
mkdir -p src/taskflow/domain

# Verificar entidades
python -c "from taskflow.domain.entities import Task; print('Entities OK')"

# Ejecutar tests
pytest tests/unit/test_entities.py -v
```

### 6.3 Sprint 2: API Backend (Semana 10)

**Objetivo:** Implementar la API REST con validación y documentación.

#### Entregables

| Componente | Descripción | Criterio de Aceptación |
|------------|-------------|------------------------|
| Endpoints CRUD | API REST completa | Tests de API pasando |
| Esquemas Pydantic | Validación de datos | 100% de endpoints validados |
| Documentación Swagger | OpenAPI/Swagger UI | /docs accesible |
| Código HTTP correcto | 200, 201, 404, 400, 422 | Tests verificando |

#### Endpoints a Implementar

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /api/v1/users | Listar usuarios |
| POST | /api/v1/users | Crear usuario |
| GET | /api/v1/users/{id} | Obtener usuario por ID |
| PUT | /api/v1/users/{id} | Actualizar usuario |
| DELETE | /api/v1/users/{id} | Eliminar usuario |
| GET | /api/v1/projects | Listar proyectos |
| POST | /api/v1/projects | Crear proyecto |
| GET | /api/v1/tasks | Listar tareas |
| POST | /api/v1/tasks | Crear tarea |
| GET | /api/v1/tasks/{id} | Obtener tarea por ID |
| PUT | /api/v1/tasks/{id} | Actualizar tarea |
| DELETE | /api/v1/tasks/{id} | Eliminar tarea |

#### Criterios de Evaluación Sprint 2

| Criterio | Porcentaje |
|----------|------------|
| Endpoints CRUD funcionales | 40% |
| Validación Pydantic | 20% |
| Documentación Swagger | 15% |
| Códigos HTTP correctos | 15% |
| Tests de API | 10% |

#### Comandos Útiles

```bash
# Verificar documentación Swagger
# Abrir en navegador: http://localhost:8000/docs

# Probar API con curl
curl -X GET http://localhost:8000/api/v1/tasks
curl -X POST http://localhost:8000/api/v1/tasks -H "Content-Type: application/json" -d '{"title":"Test"}'
```

### 6.4 Sprint 3: Persistencia (Semana 12)

**Objetivo:** Implementar persistencia con SQLAlchemy y repositories.

#### Entregables

| Componente | Descripción | Criterio de Aceptación |
|------------|-------------|------------------------|
| Modelos SQLAlchemy | User, Task, Project, Category | Modelos mapeados |
| Relaciones | FK y relaciones entre entidades | Integrity constraints |
| Repositories | Patron Repository implementado | Tests de integración |
| Migraciones | Alembic o migrations | Base de datos actualizada |

#### Criterios de Evaluación Sprint 3

| Criterio | Porcentaje |
|----------|------------|
| Modelos SQLAlchemy correctos | 30% |
| Relaciones entre entidades | 25% |
| Implementación Repository | 25% |
| Tests de integración | 15% |
| Documentación técnica | 5% |

### 6.5 Sprint 4: Testing y Calidad (Semana 14)

**Objetivo:** Asegurar calidad del código con tests automatizados.

#### Entregables

| Componente | Descripción | Criterio de Aceptación |
|------------|-------------|------------------------|
| Tests unitarios | Cobertura >80% | pytest --cov |
| Tests BDD | Escenarios behave | feature files pasando |
| Linting | Ruff, Black, mypy | Sin errores |

#### Criterios de Evaluación Sprint 4

| Criterio | Porcentaje |
|----------|------------|
| Cobertura de tests >80% | 40% |
| Tests BDD (behave) | 25% |
| Linting (Ruff, Black) | 15% |
| Pre-commit hooks | 10% |
| Documentación de tests | 10% |

### 6.6 Sprint 5: Finalización (Semana 16)

**Objetivo:** Entrega final del proyecto y sustentación.

#### Entregables

| Componente | Descripción | Criterio de Aceptación |
|------------|-------------|------------------------|
| Documentación final | README.md completo | Toda la información documentada |
| Video de sustentación | Demo + explicación | Video de 10-15 minutos |
| Refactoring | Código limpio | Sin warnings de linting |

#### Criterios de Evaluación Sprint 5

| Criterio | Porcentaje |
|----------|------------|
| Documentación completa | 30% |
| Video de sustentación | 40% |
| Calidad del código (refactoring) | 20% |
| Presentación | 10% |

---

## 7. Criterios de Evaluación

### 7.1 Checklist General por Sprint

| Criterio | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 | Sprint 5 |
|----------|:--------:|:--------:|:--------:|:--------:|:--------:|
| Código funcional | ✓ | ✓ | ✓ | ✓ | ✓ |
| Tests unitarios | ✓ | ✓ | ✓ | ✓ | ✓ |
| Tests integración | - | ✓ | ✓ | ✓ | ✓ |
| Tests BDD | - | - | - | ✓ | ✓ |
| Cobertura >80% | - | - | - | ✓ | ✓ |
| Documentación | ✓ | ✓ | ✓ | ✓ | ✓ |
| API documentada | - | ✓ | ✓ | ✓ | ✓ |
| Linting passing | - | ✓ | ✓ | ✓ | ✓ |

### 7.2 Porcentajes de Evaluación Final

| Componente | Porcentaje |
|------------|------------|
| Sprint 1: Fundamentos | 20% |
| Sprint 2: API Backend | 25% |
| Sprint 3: Persistencia | 25% |
| Sprint 4: Testing y Calidad | 15% |
| Sprint 5: Finalización | 15% |
| **Total** | **100%** |

### 7.3 Rúbrica de Evaluación

| Nivel | Puntuación | Descripción |
|-------|------------|-------------|
| Excelente | 90-100% | Supera expectativas, código limpio, tests completos |
| Bueno | 80-89% | Cumple todos los requisitos, buena calidad |
| Aceptable | 70-79% | Cumple requisitos básicos, algunas mejoras necesarias |
| Insuficiente | <70% | No cumple requisitos mínimos |

### 7.4 Requisitos Mínimos para Aprobar

- [ ] Proyecto funcionando en ambiente local
- [ ] Todos los endpoints CRUD implementados
- [ ] Cobertura de tests >= 80%
- [ ] Documentación completa en README.md
- [ ] Video de sustentación entregado
- [ ] Sin errores de linting (Ruff, Black, mypy)

---

## 8. Recursos

### 8.1 Enlaces Útiles

| Recurso | Enlace |
|---------|--------|
| Documentación FastAPI | https://fastapi.tiangolo.com |
| Documentación Pydantic | https://docs.pydantic.dev |
| Documentación SQLAlchemy | https://docs.sqlalchemy.org |
| pytest | https://docs.pytest.org |
| behave (BDD) | https://behave.readthedocs.io |

### 8.2 Comandos Rápidos de Referencia

```bash
# === INSTALACIÓN ===
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# === EJECUCIÓN ===
uvicorn src.taskflow.api.main:app --reload --port 8000

# === TESTING ===
pytest tests/unit/ -v
pytest tests/ --cov=taskflow
behave features/

# === VERIFICACIÓN ===
python --version
pytest --version
fastapi --version
curl http://localhost:8000/health
```

---

## 9. Autores

### Estudiantes del Curso

| Nombre | Código | Correo |
|--------|--------|--------|
| [Estudiante 1] | [Código] | [correo@univ.edu] |
| [Estudiante 2] | [Código] | [correo@univ.edu] |
| [Estudiante 3] | [Código] | [correo@univ.edu] |
| [Estudiante 4] | [Código] | [correo@univ.edu] |

### Docente

| Rol | Nombre | Correo |
|-----|--------|--------|
| Docente del Curso | [Nombre del Docente] | [correo@univ.edu] |

---

## Anexo: Solución de Problemas Comunes

### Problema: Módulo no encontrado

```bash
# Error: ModuleNotFoundError: No module named 'taskflow'
# Solución: Asegúrate de estar en el directorio 'proyecto'
cd F:/UNAULA/IF0100-POO-II/proyecto

# Y que el entorno virtual esté activo
venv\Scripts\activate
```

### Problema: Puerto 8000 en uso

```bash
# Error: [Errno 48] Address already in use
# Solución: Usa otro puerto
uvicorn src.taskflow.api.main:app --reload --port 8001
```

### Problema: pytest no encuentra tests

```bash
# Asegúrate de tener __init__.py en directorios de tests
touch tests/__init__.py
touch tests/unit/__init__.py
```

---

**Documento actualizado:** 2026-02-08
**Versión:** 1.0.0
**Curso:** IF0100 - POO II
**Repositorio:** [URL del repositorio - por completar]
