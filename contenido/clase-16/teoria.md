# Teoria - Testing en APIs con pytest y httpx

**IF0100 - Lenguaje de Programacion OO II**

---

## Testing en FastAPI

### Por que Testear?

| Tipo de Test | Proposito |
|--------------|-----------|
| **Unit Tests** | Verificar funciones individuales |
| **Integration Tests** | Probar interacciones entre componentes |
| **API Tests** | Probar endpoints de la API |

### Herramientas

| Herramienta | Uso |
|-------------|-----|
| **pytest** | Framework de testing |
| **httpx** | Cliente HTTP para testing de APIs |
| **TestClient** | Wrapper de httpx para FastAPI |
| **pytest-asyncio** | Testing de codigo async |

---

## TestClient de FastAPI

### Instalacion

```bash
pip install pytest httpx pytest-asyncio
```

### Configuracion de pytest

```python
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
asyncio_mode = auto
```

### TestClient Basico

```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    """Cliente de prueba para la API"""
    return TestClient(app)

def test_read_root(client):
    """Test del endpoint raiz"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to TaskFlow"}
```

---

## Fixtures de pytest

### Fixture de Base de Datos

```python
# tests/conftest.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.database import Base, get_db
from src.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False
}
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## Testing de Endpoints

### Test de GET

```python
# tests/test_users.py
from fastapi.testclient import TestClient

def test_get_users(client):
    """Test para obtener lista de usuarios"""
    response = client.get("/api/usuarios/")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "total" in data

def test_get_user_not_found(client):
    """Test para usuario no encontrado"""
    response = client.get("/api/usuarios/9999")
    assert response.status_code == 404

def test_get_user_by_id(client, db_session):
    """Test para obtener usuario por ID con fixture"""
    # Arrange - Crear datos de prueba
    user_data = {"email": "test@example.com", "nombre_completo": "Test User"}
    response = client.post("/api/usuarios/", json=user_data)
    user_id = response.json()["id"]

    # Act
    response = client.get(f"/api/usuarios/{user_id}")

    # Assert
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
```

### Test de POST

```python
# tests/test_users.py
def test_create_user(client):
    """Test para crear usuario"""
    user_data = {
        "email": "nuevo@example.com",
        "nombre_completo": "Nuevo Usuario",
        "password": "securepassword123"
    }

    response = client.post("/api/usuarios/", json=user_data)

    assert response.status_code == 200  # O 201 Created
    data = response.json()
    assert data["email"] == "nuevo@example.com"
    assert "id" in data
    assert "password" not in response.json()  # No debe devolver password

def test_create_user_invalid_email(client):
    """Test con email invalido"""
    user_data = {
        "email": "email-invalido",
        "nombre_completo": "Test User"
    }

    response = client.post("/api/usuarios/", json=user_data)
    assert response.status_code == 422  # Validation Error
```

### Test de PUT y DELETE

```python
# tests/test_users.py
def test_update_user(client, db_session):
    """Test para actualizar usuario"""
    # Crear usuario
    user_data = {"email": "update@example.com", "nombre_completo": "Original"}
    create_response = client.post("/api/usuarios/", json=user_data)
    user_id = create_response.json()["id"]

    # Actualizar
    update_data = {"nombre_completo": "Actualizado"}
    response = client.put(f"/api/usuarios/{user_id}", json=update_data)

    assert response.status_code == 200
    assert response.json()["nombre_completo"] == "Actualizado"

def test_delete_user(client, db_session):
    """Test para eliminar usuario"""
    # Crear usuario
    user_data = {"email": "delete@example.com", "nombre_completo": "Delete Me"}
    create_response = client.post("/api/usuarios/", json=user_data)
    user_id = create_response.json()["id"]

    # Eliminar
    response = client.delete(f"/api/usuarios/{user_id}")
    assert response.status_code == 200

    # Verificar eliminacion
    get_response = client.get(f"/api/usuarios/{user_id}")
    assert get_response.status_code == 404
```

---

## Parametrizacion de Tests

```python
import pytest

@pytest.mark.parametrize("email,expected_status", [
    ("test@example.com", 200),
    ("invalid-email", 422),
    ("", 422),
])
def test_create_user_validation(client, email, expected_status):
    """Test parametrizado para validacion de email"""
    user_data = {
        "email": email,
        "nombre_completo": "Test User",
        "password": "password123"
    }
    response = client.post("/api/usuarios/", json=user_data)
    assert response.status_code == expected_status
```

---

## Marcadores Personalizados

```python
# pytest.ini o conftest.py
import pytest

@pytest.mark.slow
def test_complicated_workflow():
    """Test que tarda mucho en ejecutar"""
    # Este test puede ser ignorado con: pytest -m "not slow"
    pass

@pytest.mark.unit
def test_pure_function():
    """Test de unidad"""
    pass

@pytest.mark.integration
def test_database_operation():
    """Test de integracion"""
    pass
```

---

**Ultima actualizacion:** 2026-02-08
