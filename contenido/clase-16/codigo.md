# Codigo - Testing en APIs con pytest y httpx

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Configuracion de Tests

```python
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
asyncio_mode = auto
addopts = -v --tb=short
filterwarnings =
    ignore::DeprecationWarning
```

```python
# conftest.py (raiz del proyecto)
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.db.database import Base, get_db

# Base de datos de prueba
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False
}
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override de dependencias
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    """Cliente de prueba"""
    return TestClient(app)

@pytest.fixture
def db_session():
    """Sesion de base de datos para tests"""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 2. Tests de Modelos

```python
# tests/test_models.py
import pytest
from src.models.user import User
from src.schemas.user import UserCreate

def test_user_model_creation():
    """Test de creacion de modelo User"""
    user = User(
        email="test@example.com",
        nombre_completo="Test User",
        hashed_password="hashed_password"
    )

    assert user.email == "test@example.com"
    assert user.nombre_completo == "Test User"
    assert user.activo == True

def test_user_create_schema():
    """Test de schema UserCreate"""
    user_data = UserCreate(
        email="test@example.com",
        nombre_completo="Test User",
        password="securepassword123"
    )

    assert user_data.email == "test@example.com"
    assert user_data.password == "securepassword123"
```

---

## 3. Tests de API - Usuarios

```python
# tests/test_users.py
from fastapi.testclient import TestClient

def test_create_user(client):
    """Test: Crear usuario exitosamente"""
    user_data = {
        "email": "test@example.com",
        "nombre_completo": "Test User",
        "password": "password123"
    }

    response = client.post("/api/usuarios/", json=user_data)

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["nombre_completo"] == "Test User"
    assert "id" in data
    assert "password" not in data  # Password no debe ser visible

def test_get_users_empty(client):
    """Test: Obtener usuarios cuando no hay ninguno"""
    response = client.get("/api/usuarios/")

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "total" in data
    assert isinstance(data["data"], list)

def test_get_user_not_found(client):
    """Test: Usuario no existe"""
    response = client.get("/api/usuarios/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Usuario no encontrado"

def test_create_user_duplicate_email(client):
    """Test: No permitir email duplicado"""
    user_data = {
        "email": "duplicate@example.com",
        "nombre_completo": "First User",
        "password": "password123"
    }

    # Crear primer usuario
    client.post("/api/usuarios/", json=user_data)

    # Intentar crear segundo con mismo email
    response = client.post("/api/usuarios/", json=user_data)

    assert response.status_code == 400
    assert "ya registrado" in response.json()["detail"]
```

---

## 4. Tests de API - Proyectos

```python
# tests/test_projects.py
def test_create_project(client, db_session):
    """Test: Crear proyecto"""
    project_data = {
        "nombre": "Mi Proyecto",
        "descripcion": "Descripcion del proyecto"
    }

    response = client.post("/api/proyectos/", json=project_data)

    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Mi Proyecto"
    assert data["estado"] == "activo"
    assert "id" in data

def test_get_projects_list(client):
    """Test: Listar proyectos"""
    response = client.get("/api/proyectos/")

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)

def test_get_project_with_tasks(client, db_session):
    """Test: Obtener proyecto con sus tareas"""
    # Crear proyecto
    project_data = {"nombre": "Project with Tasks", "descripcion": ""}
    project_response = client.post("/api/proyectos/", json=project_data)
    project_id = project_response.json()["id"]

    # Obtener proyecto
    response = client.get(f"/api/proyectos/{project_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Project with Tasks"
```

---

## 5. Tests Parametrizados

```python
# tests/test_validation.py
import pytest

@pytest.mark.parametrize("email,expected_valid", [
    ("test@example.com", True),
    ("user.name@domain.com", True),
    ("invalid-email", False),
    ("@nodomain.com", False),
    ("noat.com", False),
])
def test_email_validation(client, email, expected_valid):
    """Test parametrizado para validacion de email"""
    user_data = {
        "email": email,
        "nombre_completo": "Test User",
        "password": "password123"
    }

    response = client.post("/api/usuarios/", json=user_data)

    if expected_valid:
        assert response.status_code == 200
    else:
        assert response.status_code == 422

@pytest.mark.parametrize("skip,limit,expected_keys", [
    (0, 10, ["data", "total", "skip", "limit"]),
    (0, 50, ["data", "total", "skip", "limit"]),
    (100, 20, ["data", "total", "skip", "limit"]),
])
def test_pagination_structure(client, skip, limit, expected_keys):
    """Test de estructura de paginacion"""
    response = client.get(f"/api/usuarios/?skip={skip}&limit={limit}")

    assert response.status_code == 200
    data = response.json()
    assert all(key in data for key in expected_keys)
```

---

## 6. Coverage y Reportes

```bash
# Instalar coverage
pip install pytest-cov

# Ejecutar con coverage
pytest --cov=src --cov-report=html

# Reporte en terminal
pytest --cov=src --cov-report=term-missing

# Coverage minimum
pytest --cov=src --cov-fail-under=80
```

---

**Ultima actualizacion:** 2026-02-08
