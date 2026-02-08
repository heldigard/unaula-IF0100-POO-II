# Sprint 1: Setup del Proyecto y Modelos del Dominio

## Informacion del Sprint

| Campo | Valor |
|-------|-------|
| Sprint | 1 |
| Duracion | 1 semana |
| Objetivo | Configurar entorno de desarrollo y crear entidades base del dominio |
| Entrega | Domingo de la semana 1, 23:59 |

---

## Entregables

| Entregable | Descripcion | Estado |
|------------|-------------|--------|
| Repositorio Git | Configurado con `.gitignore`, `pyproject.toml` y estructura base | Pendiente |
| Entidad User | Clase con atributos y metodos base | Pendiente |
| Entidad Task | Clase con atributos y metodos base | Pendiente |
| Entidad Project | Clase con atributos y metodos base | Pendiente |
| Tests Unitarios | Cobertura superior al 50% | Pendiente |
| Documentacion | README.md actualizado | Pendiente |

---

## Criterios de Aceptacion

- [ ] Python 3.12+ instalado y configurado
- [ ] `pyproject.toml` con dependencias definidas (pytest, black, mypy)
- [ ] Clase `User` implementada con atributos: `id`, `username`, `email`, `password_hash`, `created_at`
- [ ] Clase `Task` implementada con atributos: `id`, `title`, `description`, `status`, `priority`, `project_id`, `assignee_id`, `created_at`, `due_date`
- [ ] Clase `Project` implementada con atributos: `id`, `name`, `description`, `owner_id`, `created_at`
- [ ] Tests unitarios para todas las clases (cobertura > 50%)
- [ ] README.md con instrucciones de instalacion y ejecucion
- [ ] Codigo type-hinted y compliant con PEP 8

---

## Requisitos Tecnicos

### Tecnologia Principal

| Requisito | Version Minima | Descripcion |
|-----------|----------------|-------------|
| Python | 3.12+ | Lenguaje de programacion |
| pytest | 7.0+ | Framework de testing |
| black | 23.0+ | Formateador de codigo |
| mypy | 1.0+ | Verificador de tipos |

### Estandares de Codigo

```python
# Type hints obligatorios en todas las funciones y metodos
def create_user(self, username: str, email: str, password: str) -> User:
    ...

# PEP 8 compliance verificado con black
# Lineas maximas: 88 caracteres (default de black)
```

---

## Guia de Implementacion

### Paso 1: Crear Estructura de Directorios

```bash
proyecto/
├── src/
│   └── taskflow/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── user.py
│       │   ├── task.py
│       │   └── project.py
├── tests/
│   ├── __init__.py
│   ├── test_user.py
│   ├── test_task.py
│   └── test_project.py
├── pyproject.toml
└── README.md
```

### Paso 2: Configurar `pyproject.toml`

```toml
[tool.pyproject.toml]
name = "taskflow"
version = "0.1.0"
description = "Sistema de gestion de tareas y proyectos"
requires-python = ">=3.12"
readme = "README.md"

[tool.pyproject.dependencies]
pytest = "^8.0.0"
pytest-cov = "^4.0.0"

[tool.black]
line-length = 88
target-version = ["py312"]

[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
```

### Paso 3: Implementar Clase User

```python
# src/taskflow/models/user.py
from datetime import datetime
from uuid import uuid4


class User:
    """Representa un usuario del sistema."""

    def __init__(self, username: str, email: str, password: str) -> None:
        self.id: str = str(uuid4())
        self.username = username
        self.email = email
        self.password_hash = self._hash_password(password)
        self.created_at = datetime.utcnow()

    def _hash_password(self, password: str) -> str:
        """Hashea la contraseña (simulado)."""
        # TODO: Implementar con bcrypt en Sprint 2
        return f"hash_{password}"

    def verify_password(self, password: str) -> bool:
        """Verifica la contraseña del usuario."""
        return self.password_hash == f"hash_{password}"
```

### Paso 4: Implementar Clase Task

```python
# src/taskflow/models/task.py
from datetime import datetime
from enum import Enum
from uuid import uuid4


class TaskStatus(Enum):
    """Estados posibles de una tarea."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TaskPriority(Enum):
    """Prioridades de una tarea."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


class Task:
    """Representa una tarea en el sistema."""

    def __init__(
        self,
        title: str,
        description: str,
        project_id: str,
        priority: TaskPriority = TaskPriority.MEDIUM,
    ) -> None:
        self.id: str = str(uuid4())
        self.title = title
        self.description = description
        self.status = TaskStatus.PENDING
        self.priority = priority
        self.project_id = project_id
        self.assignee_id: str | None = None
        self.created_at = datetime.utcnow()
        self.due_date: datetime | None = None

    def assign_to(self, user_id: str) -> None:
        """Asigna la tarea a un usuario."""
        self.assignee_id = user_id

    def complete(self) -> None:
        """Marca la tarea como completada."""
        self.status = TaskStatus.COMPLETED
```

### Paso 5: Implementar Clase Project

```python
# src/taskflow/models/project.py
from datetime import datetime
from uuid import uuid4


class Project:
    """Representa un proyecto en el sistema."""

    def __init__(self, name: str, description: str, owner_id: str) -> None:
        self.id: str = str(uuid4())
        self.name = name
        self.description = description
        self.owner_id = owner_id
        self.created_at = datetime.utcnow()

    def is_owner(self, user_id: str) -> bool:
        """Verifica si el usuario es el propietario."""
        return self.owner_id == user_id
```

### Paso 6: Escribir Tests Unitarios

```python
# tests/test_user.py
import pytest
from taskflow.models.user import User


class TestUser:
    """Tests para la clase User."""

    def test_create_user(self) -> None:
        """Verifica que se crea un usuario con los atributos correctos."""
        user = User(username="juan", email="juan@correo.com", password="123456")

        assert user.id is not None
        assert user.username == "juan"
        assert user.email == "juan@correo.com"
        assert user.created_at is not None

    def test_verify_password_correct(self) -> None:
        """Verifica contraseña correcta."""
        user = User(username="juan", email="juan@correo.com", password="123456")

        assert user.verify_password("123456") is True

    def test_verify_password_incorrect(self) -> None:
        """Verifica contraseña incorrecta."""
        user = User(username="juan", email="juan@correo.com", password="123456")

        assert user.verify_password("wrong") is False
```

---

## Conexion con Clases del Curso

| Unidad | Clase | Tema | Relacion con Sprint |
|--------|-------|------|-------------------|
| Unidad 00 | Clase 01 | Variables y tipos de datos | Uso de `str`, `int`, `datetime` |
| Unidad 00 | Clase 02 | Estructuras de control | Validaciones en metodos |
| Unidad 00 | Clase 03 | Estructuras de datos | `Enum` para estados |
| Unidad 01 | Clase 01 | Clases y objetos | Definicion de clases `User`, `Task`, `Project` |
| Unidad 01 | Clase 02 | Encapsulamiento | Atributos privados con `_` |
| Unidad 01 | Clase 03 | Herencia y polimorfismo | Enums heredan de `Enum` |
| Unidad 01 | Clase 04 | Modelado de BD | Diseno de entidades |
| Unidad 02 | Clase 01 | TDD | Tests primero, luego implementacion |

---

## Recursos

### Documentacion Oficial

| Recurso | Enlace |
|---------|--------|
| Documentacion Python | https://docs.python.org/3.12/ |
| Documentacion pytest | https://docs.pytest.org/en/stable/ |
| PEP 8 Style Guide | https://peps.python.org/pep-0008/ |
| Documentacion Enum | https://docs.python.org/3/library/enum.html |
| datetime Module | https://docs.python.org/3/library/datetime.html |

### Ejemplos de Estructura

```bash
# Verificar instalacion de Python
python --version  # Debe mostrar 3.12+

# Verificar ejecucion de tests
pytest tests/ -v --cov=src

# Verificar type hints
mypy src/
```

---

## Evaluacion del Sprint

| Criterio | Peso | Descripcion |
|----------|------|-------------|
| Funcionalidad | 40% | Codigo corre, clases implementadas correctamente |
| Calidad de codigo | 30% | Type hints, PEP 8, clean code |
| Tests | 20% | Cobertura > 50%, tests significativos |
| Documentacion | 10% | README claro, instrucciones completas |

### Calificacion maxima del Sprint: 10% del Proyecto Final

---

## Notas del Instructor

- Este Sprint establece la base del proyecto. Tómate el tiempo necesario para entender la estructura.
- En el Sprint 2 agregaremos persistencia de datos y autenticación.
- Las clases deben ser simples por ahora; las complejidades vendrán gradualmente.
- Consulta la documentacion de Python si tienes dudas sobre type hints o enumeraciones.
