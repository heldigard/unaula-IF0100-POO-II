# Sprint 3: Testing y BDD

## Información del Sprint

| Atributo | Detalle |
|----------|---------|
| Sprint | 3 |
| Duración | 1 semana |
| Objetivo | Implementar suite de tests completa |
| Entregable Principal | Suite de tests con cobertura >80% |

---

## Entregables

1. **Tests Unitarios para Modelos**
   - Modelos `User`, `Task`, `Project` completamente probados
   - Validaciones de datos verificadas
   - Relaciones entre modelos testeadas

2. **Tests de Integración para API**
   - Endpoints REST completamente probados
   - Operaciones CRUD verificadas
   - Manejo de errores validado

3. **Tests BDD con Behave**
   - Features definidos en Gherkin
   - Steps implementados
   - Escenarios de negocio cubiertos

4. **Métricas de Calidad**
   - Cobertura de código >80%
   - Tests pasan en pipeline CI/CD
   - Documentación de tests actualizada

---

## Criterios de Aceptación

- [ ] Tests unitarios para User, Task, Project implementados
- [ ] Tests de API con TestClient funcionales
- [ ] Scenarios BDD definidos y ejecutándose
- [ ] Coverage >80% logrado
- [ ] Tests pasan en CI/CD (GitHub Actions)

---

## Requisitos Técnicos

### Dependencias Requeridas

```txt
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-asyncio>=0.21.0
httpx>=0.25.0
behave>=1.2.6
coverage>=7.3.0
```

### Herramientas del Stack

| Herramienta | Propósito |
|------------|-----------|
| pytest | Framework de testing principal |
| pytest-cov | Medición de cobertura de código |
| httpx | Cliente HTTP para tests de API |
| behave | Framework BDD para tests de comportamiento |
| TestClient | Cliente de testing de FastAPI |

---

## Guía de Implementación

### Paso 1: Configurar pytest

Crear archivo `F:/UNAULA/IF0100-POO-II/proyecto/tests/pytest.ini`:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
asyncio_mode = auto
```

Crear archivo `F:/UNAULA/IF0100-POO-II/proyecto/tests/conftest.py`:

```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Configuración de base de datos de prueba
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Fixture para sesión de base de datos de prueba."""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db_session):
    """Fixture para cliente de testing."""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
```

### Paso 2: Tests Unitarios de Modelos

Crear archivo `F:/UNAULA/IF0100-POO-II/proyecto/tests/test_models.py`:

```python
from datetime import datetime
from app.models import User, Task, Project

class TestUserModel:
    """Tests para el modelo User."""

    def test_create_user(self, db_session):
        """Test creación básica de usuario."""
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password="hashed_password"
        )
        db_session.add(user)
        db_session.commit()

        assert user.id is not None
        assert user.email == "test@example.com"
        assert user.created_at is not None

    def test_user_email_unique(self, db_session):
        """Test restricción de email único."""
        user1 = User(
            email="unique@example.com",
            username="user1",
            hashed_password="password1"
        )
        user2 = User(
            email="unique@example.com",
            username="user2",
            hashed_password="password2"
        )
        db_session.add(user1)
        db_session.commit()

        db_session.add(user2)
        from sqlalchemy.exc import IntegrityError
        assert db_session.commit_lambda or \
               lambda: db_session.commit() and False

    def test_user_password_hashing(self, db_session):
        """Test que la contraseña no se almacena en texto plano."""
        user = User(
            email="hash@test.com",
            username="hashtest",
            hashed_password="plain_password"
        )
        assert user.hashed_password != "plain_password"

class TestTaskModel:
    """Tests para el modelo Task."""

    def test_create_task(self, db_session, test_user):
        """Test creación de tarea."""
        task = Task(
            title="Tarea de prueba",
            description="Descripción de prueba",
            user_id=test_user.id,
            status="pending"
        )
        db_session.add(task)
        db_session.commit()

        assert task.id is not None
        assert task.title == "Tarea de prueba"
        assert task.status == "pending"

    def test_task_status_values(self, db_session, test_user):
        """Test valores válidos de estado."""
        valid_statuses = ["pending", "in_progress", "completed"]

        for status in valid_statuses:
            task = Task(
                title=f"Tarea {status}",
                user_id=test_user.id,
                status=status
            )
            db_session.add(task)
            db_session.commit()
            assert task.status == status
```

### Paso 3: Tests de API

Crear archivo `F:/UNAULA/IF0100-POO-II/proyecto/tests/test_api_users.py`:

```python
from fastapi.testclient import TestClient

class TestUserAPI:
    """Tests para endpoints de usuarios."""

    def test_create_user_success(self, client):
        """Test creación exitosa de usuario."""
        user_data = {
            "email": "nuevo@test.com",
            "username": "nuevouser",
            "password": "password123"
        }

        response = client.post("/users/", json=user_data)

        assert response.status_code == 201
        data = response.json()
        assert data["email"] == user_data["email"]
        assert data["username"] == user_data["username"]
        assert "id" in data

    def test_create_user_validation_error(self, client):
        """Test error de validación con datos inválidos."""
        user_data = {
            "email": "email-invalido",
            "username": "",
            "password": "123"
        }

        response = client.post("/users/", json=user_data)

        assert response.status_code == 422

    def test_get_user(self, client, test_user):
        """Test obtener usuario por ID."""
        response = client.get(f"/users/{test_user.id}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == test_user.id
        assert data["email"] == test_user.email

    def test_get_user_not_found(self, client):
        """Test obtener usuario inexistente."""
        response = client.get("/users/99999")

        assert response.status_code == 404

    def test_list_users(self, client, test_user):
        """Test listar todos los usuarios."""
        response = client.get("/users/")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
```

### Paso 4: Definir Features BDD

Crear archivo `F:/UNAULA/IF0100-POO-II/proyecto/tests/features/users.feature`:

```gherkin
Feature: Gestión de Usuarios
  Como administrador del sistema
  Quiero crear y gestionar usuarios
  Para controlar el acceso a las funcionalidades

  Background:
    Given que el sistema está operativo

  Scenario: Crear usuario exitosamente
    Given que no existe un usuario con email "nuevo@test.com"
    When envío POST a /users con datos válidos
      | email      | nuevo@test.com    |
      | username   | nuevouser         |
      | password   | password123       |
    Then el response status es 201
    And el usuario es creado en la base de datos
    And el response contiene el email "nuevo@test.com"

  Scenario: Error al crear usuario con email duplicado
    Given que existe un usuario con email "existente@test.com"
    When envío POST a /users con el mismo email
      | email      | existente@test.com |
      | username   | otro_usuario       |
      | password   | password456        |
    Then el response status es 400
    And el mensaje de error contiene "duplicate"

  Scenario: Obtener usuario por ID
    Given que existe un usuario con username "testuser"
    When envío GET a /users/{id}
    Then el response status es 200
    And el response contiene "testuser"
```

### Paso 5: Implementar Steps BDD

Crear archivo `F:/UNAULA/IF0100-POO-II/proyecto/tests/features/steps/user_steps.py`:

```python
from behave import given, when, then
import requests

BASE_URL = "http://localhost:8000"

@given("que no existe un usuario con email '{email}'")
def step_no_user_with_email(context, email):
    # Limpiar usuario si existe
    # Implementar lógica de cleanup
    pass

@when("envío POST a /users con datos válidos")
def step_create_user_valid(context):
    """Envía request para crear usuario con datos válidos."""
    data = {}
    for row in context.table:
        data = dict(row)

    context.response = requests.post(
        f"{BASE_URL}/users/",
        json=data
    )
    context.response_data = context.response.json()

@then("el response status es {status_code:d}")
def step_check_status(context, status_code):
    """Verifica que el status code sea el esperado."""
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"

@then("el usuario es creado en la base de datos")
def step_user_in_database(context):
    """Verifica que el usuario existe en la base de datos."""
    # Implementar verificación en DB
    user_id = context.response_data.get("id")
    assert user_id is not None
```

### Paso 6: Medir Coverage

Ejecutar tests con coverage:

```bash
# Instalar coverage
pip install pytest-cov coverage

# Ejecutar tests con coverage
pytest --cov=app --cov-report=html --cov-report=term-missing

# Generar reporte HTML
coverage html -o htmlcov

# Verificar cobertura mínima
coverage report --fail-under=80
```

Archivo de configuración `F:/UNAULA/IF0100-POO-II/proyecto/.coveragerc`:

```ini
[run]
source = app
omit =
    tests/*
    */__pycache__/*
    *main.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
    if TYPE_CHECKING:

[html]
title = Coverage Report - TaskFlow
```

---

## Conexión con Clases del Curso

| Unidad | Clase | Tema | Aplicación en Sprint |
|--------|-------|------|---------------------|
| Unidad 02 | Clase 01 | TDD Intro | Metodología de desarrollo guiado por tests |
| Unidad 02 | Clase 02 | pytest Avanzado | Fixtures, parametrización, plugins |
| Unidad 02 | Clase 03 | BDD Intro | Definición de features en Gherkin |
| Unidad 03 | Clase 04 | Testing FastAPI | TestClient, dependency overrides |

---

## Recursos

### Documentación Oficial

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [behave Documentation](https://behave.readthedocs.io/)
- [Coverage.py Documentation](https://coverage.readthedocs.io/)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)

### Ejemplos de Configuración

```bash
# Estructura de directorios recomendada
proyecto/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_api_users.py
│   ├── test_api_tasks.py
│   ├── features/
│   │   ├── users.feature
│   │   ├── tasks.feature
│   │   └── steps/
│   │       ├── __init__.py
│   │       ├── user_steps.py
│   │       └── task_steps.py
```

---

## Evaluación

| Componente | Porcentaje | Descripción |
|------------|------------|-------------|
| Cobertura | 40% | >80% de cobertura de código |
| Tests Unitarios | 25% | Models User, Task, Project |
| Tests API | 20% | Endpoints CRUD completos |
| Tests BDD | 15% | Scenarios de negocio definidos |

### Rúbrica de Evaluación

| Nivel | Cobertura | Tests Unitarios | Tests API | Tests BDD |
|-------|-----------|-----------------|------------|-----------|
| Excelente | >90% | Completos + edge cases | Completos + errores | Completos |
| Bueno | 80-90% | Principales cubiertos | Principales cubiertos | Principales |
| Suficiente | 70-80% | Basic coverage | Basic coverage | Basic |
| Insuficiente | <70% | Incompleto | Incompleto | Incompleto |

---

## Checklist de Completitud

- [ ] `pytest.ini` configurado
- [ ] `conftest.py` con fixtures definidos
- [ ] `test_models.py` con tests de User, Task, Project
- [ ] `test_api_*.py` con tests de endpoints
- [ ] Features BDD definidos en Gherkin
- [ ] Steps BDD implementados
- [ ] Coverage >80% verificado
- [ ] Tests pasan en CI/CD
- [ ] Documentación actualizada

---

**Última Actualización:** Sprint 3 - Testing y BDD
**Versión:** 1.0
