"""
Script de Práctica - Clase 3.4: Testing de FastAPI

Este script demuestra cómo probar FastAPI:
- Usar TestClient para testing sin servidor
- Testing de endpoints GET, POST, PUT, DELETE
- Testing con Pytest
- Testing de dependencias
- Testing de validación de datos
- Mock y fixtures

Autor: IF0100 - UNAULA
"""

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional, List

# =====================================================
// APLICACIÓN A PROBAR
// =====================================================

app = FastAPI(title="TaskFlow API - Testing")


# Modelos
class TareaCreate(BaseModel):
    titulo: str = Field(..., min_length=5, max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = Field(default="media", regex="^(baja|media|alta)$")


class TareaResponse(TareaCreate):
    id: int
    completada: bool = False


# Base de datos simulada
tareas_db = {
    1: {"id": 1, "titulo": "Implementar login", "descripcion": "Crear endpoint", "completada": False, "prioridad": "alta"},
    2: {"id": 2, "titulo": "Diseñar base de datos", "descripcion": "Modelo ER", "completada": True, "prioridad": "media"},
}


# Endpoints
@app.get("/")
def read_root():
    return {"mensaje": "TaskFlow API", "version": "1.0"}


@app.get("/tareas", response_model=List[TareaResponse])
def get_tareas(completada: Optional[bool] = None):
    """Listar todas las tareas opcionalmente filtradas por estado"""
    tareas = list(tareas_db.values())
    if completada is not None:
        tareas = [t for t in tareas if t["completada"] == completada]
    return tareas


@app.get("/tareas/{tarea_id}", response_model=TareaResponse)
def get_tarea(tarea_id: int):
    """Obtener una tarea por ID"""
    if tarea_id not in tareas_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tareas_db[tarea_id]


@app.post("/tareas", response_model=TareaResponse, status_code=201)
def create_tarea(tarea: TareaCreate):
    """Crear una nueva tarea"""
    nuevo_id = max(tareas_db.keys()) + 1 if tareas_db else 1
    nueva_tarea = {
        "id": nuevo_id,
        "titulo": tarea.titulo,
        "descripcion": tarea.descripcion,
        "completada": False,
        "prioridad": tarea.prioridad
    }
    tareas_db[nuevo_id] = nueva_tarea
    return nueva_tarea


@app.put("/tareas/{tarea_id}", response_model=TareaResponse)
def update_tarea(tarea_id: int, tarea: TareaCreate):
    """Actualizar una tarea existente"""
    if tarea_id not in tareas_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    tareas_db[tarea_id]["titulo"] = tarea.titulo
    tareas_db[tarea_id]["descripcion"] = tarea.descripcion
    tareas_db[tarea_id]["prioridad"] = tarea.prioridad
    return tareas_db[tarea_id]


@app.delete("/tareas/{tarea_id}")
def delete_tarea(tarea_id: int):
    """Eliminar una tarea"""
    if tarea_id not in tareas_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tareas_db.pop(tarea_id)
    return {"mensaje": "Tarea eliminada"}


# Dependencia para auth
def get_current_user(api_key: str = "test-key"):
    """Dependencia simple de autenticación"""
    if api_key != "valid-key":
        raise HTTPException(status_code=401, detail="API Key inválida")
    return {"user_id": 1, "username": "test_user"}


@app.get("/perfil")
def leer_perfil(current_user: dict = Depends(get_current_user)):
    """Endpoint protegido que requiere autenticación"""
    return current_user


# =====================================================
# EJECUCIÓN DE LA APP (para desarrollo)
# =====================================================

if __name__ == "__main__":
    import uvicorn
    print("=" * 50)
    print("TaskFlow API - Modo Desarrollo")
    print("=" * 50)
    print("\nEjecuta los tests con: pytest tests/test_api.py")
    print("\nServidor: http://localhost:8003")
    print("=" * 50)

    uvicorn.run(app, host="127.0.0.1", port=8003, reload=True)


"""
=====================================================
TESTING CON PYTEST
=====================================================

Crea un archivo: tests/test_fastapi_testing.py

```python
import pytest
from fastapi.testclient import TestClient
from scripts.unidad_03.testing_fastapi import app, tareas_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_db():
    """Fixture que resetea la BD antes de cada test"""
    global tareas_db
    tareas_db = {
        1: {"id": 1, "titulo": "Implementar login", "descripcion": "Crear endpoint", "completada": False, "prioridad": "alta"},
        2: {"id": 2, "titulo": "Diseñar BD", "descripcion": "Modelo ER", "completada": True, "prioridad": "media"},
    }
    yield
    tareas_db.clear()


def test_read_root():
    \"\"\"Test GET /\"\"\"
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "TaskFlow API"


def test_get_tareas():
    \"\"\"Test GET /tareas\"\"\"
    response = client.get("/tareas")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_tareas_filtradas():
    \"\"\"Test GET /tareas?completada=true\"\"\"
    response = client.get("/tareas?completada=true")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == 2


def test_get_tarea_existente():
    \"\"\"Test GET /tareas/1\"\"\"
    response = client.get("/tareas/1")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Implementar login"


def test_get_tarea_inexistente():
    \"\"\"Test GET /tareas/999\"\"\"
    response = client.get("/tareas/999")
    assert response.status_code == 404
    assert "no encontrada" in response.json()["detail"]


def test_create_tarea_valida():
    \"\"\"Test POST /tareas con datos válidos\"\"\"
    nueva_tarea = {
        "titulo": "Nueva tarea de prueba",
        "descripcion": "Testing",
        "prioridad": "alta"
    }
    response = client.post("/tareas", json=nueva_tarea)
    assert response.status_code == 201
    assert response.json()["titulo"] == "Nueva tarea de prueba"
    assert response.json()["id"] == 3


def test_create_tarea_invalida():
    \"\"\"Test POST /tareas con título muy corto\"\"\"
    tarea_invalida = {
        "titulo": "abc",
        "prioridad": "media"
    }
    response = client.post("/tareas", json=tarea_invalida)
    assert response.status_code == 422  # Validation Error


def test_update_tarea():
    \"\"\"Test PUT /tareas/1\"\"\"
    datos_actualizacion = {
        "titulo": "Título actualizado",
        "descripcion": "Nueva descripción",
        "prioridad": "baja"
    }
    response = client.put("/tareas/1", json=datos_actualizacion)
    assert response.status_code == 200
    assert response.json()["titulo"] == "Título actualizado"


def test_delete_tarea():
    \"\"\"Test DELETE /tareas/1\"\"\"
    response = client.delete("/tareas/1")
    assert response.status_code == 200
    assert "eliminada" in response.json()["mensaje"]


def test_perfil_con_auth_valida():
    \"\"\"Test GET /perfil con API key válida\"\"\"
    headers = {"X-API-Key": "valid-key"}
    response = client.get("/perfil", headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == "test_user"


def test_perfil_con_auth_invalida():
    \"\"\"Test GET /perfil con API key inválida\"\"\"
    headers = {"X-API-Key": "invalid-key"}
    response = client.get("/perfil", headers=headers)
    assert response.status_code == 401


# Test parametrizado
@pytest.mark.parametrize("prioridad", ["baja", "media", "alta"])
def test_create_tarea_con_diferentes_prioridades(prioridad):
    \"\"\"Test que todas las prioridades válidas funcionan\"\"\"
    tarea = {
        "titulo": "Tarea de prueba",
        "prioridad": prioridad
    }
    response = client.post("/tareas", json=tarea)
    assert response.status_code == 201
    assert response.json()["prioridad"] == prioridad
```

=====================================================
EJECUTAR LOS TESTS
=====================================================

1. Instalar pytest:
   pip install pytest

2. Crear el archivo tests/test_fastapi_testing.py

3. Ejecutar tests:
   pytest tests/test_fastapi_testing.py -v

4. Ejecutar con coverage:
   pip install pytest-cov
   pytest tests/test_fastapi_testing.py --cov=scripts/unidad-03 --cov-report=html

5. Ejecutar solo un test específico:
   pytest tests/test_fastapi_testing.py::test_get_tareas -v

6. Ejecutar tests que coincidan con un patrón:
   pytest tests/test_fastapi_testing.py -k "create" -v

=====================================================
TIPOS DE ASSERTS
=====================================================

- assert response.status_code == 200
- assert response.json()["clave"] == "valor"
- assert len(response.json()) == 3
- assert "mensaje" in response.json()
- assert response.status_code != 401
- pytest.raises(HTTPException)...

=====================================================
FIXTURES ÚTILES
====================================================

```python
@pytest.fixture
def client():
    \"\"\"Retorna un TestClient\"\"\"
    return TestClient(app)

@pytest.fixture
def tarea_de_prueba():
    \"\"\"Crea una tarea de prueba\"\"\"
    return {"titulo": "Test", "prioridad": "media"}

@pytest.fixture
def auth_headers():
    \"\"\"Retorna headers de autenticación\"\"\"
    return {"X-API-Key": "valid-key"}
```
"""
