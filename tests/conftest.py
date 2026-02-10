"""
Fixtures globales de pytest - TaskFlow
Unidad: 2.3 - Fixtures y Mocks
Unidad: 3.7 - Tests de Integración (API fixtures)
"""

import pytest
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Generator, Dict

# Agregar el directorio src al path de Python
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from src.taskflow.models import (
    Usuario,
    Proyecto,
    Tarea,
    Comentario,
    EstadoUsuario,
    EstadoProyecto,
    EstadoTarea,
    PrioridadTarea,
)
from src.taskflow.repositories import (
    UsuarioRepository,
    ProyectoRepository,
    TareaRepository,
    ComentarioRepository,
)
from src.taskflow.services import (
    UsuarioService,
    ProyectoService,
    TareaService,
)


# =============================================================================
# PYTEST CONFIGURATION
# =============================================================================

def pytest_configure(config):
    """
    Configuración adicional de pytest.

    Se ejecuta al inicio de la sesión de tests.
    Configura marcadores personalizados y opciones.
    """
    # Registrar marcadores personalizados
    config.addinivalue_line(
        "markers", "unit: Tests unitarios (aislados, rápidos)"
    )
    config.addinivalue_line(
        "markers", "integration: Tests de integración (requieren dependencias externas)"
    )
    config.addinivalue_line(
        "markers", "slow: Tests que toman más de 1 segundo"
    )
    config.addinivalue_line(
        "markers", "auth: Tests relacionados con autenticación"
    )
    config.addinivalue_line(
        "markers", "api: Tests de endpoints de API"
    )


# =============================================================================
# FIXTURES DE DATOS DE PRUEBA
# =============================================================================

@pytest.fixture
def usuario_data():
    """Datos para crear un usuario de prueba."""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "nombre_completo": "Test User",
    }


@pytest.fixture
def proyecto_data():
    """Datos para crear un proyecto de prueba."""
    return {
        "nombre": "Proyecto Test",
        "descripcion": "Descripción del proyecto de prueba",
    }


@pytest.fixture
def tarea_data():
    """Datos para crear una tarea de prueba."""
    return {
        "titulo": "Tarea de prueba",
        "descripcion": "Descripción de la tarea",
        "prioridad": PrioridadTarea.MEDIA,
        "proyecto_id": 1,
        "asignado_a": 1,
    }


# =============================================================================
# FIXTURES DE MODELOS
# =============================================================================

@pytest.fixture
def usuario(usuario_data):
    """Usuario de prueba."""
    return Usuario(
        id=1,
        username=usuario_data["username"],
        email=usuario_data["email"],
        nombre_completo=usuario_data["nombre_completo"],
        estado=EstadoUsuario.ACTIVO,
        creado_en=datetime.now(),
    )


@pytest.fixture
def proyecto():
    """Proyecto de prueba."""
    return Proyecto(
        id=1,
        nombre="Proyecto Test",
        descripcion="Descripción de prueba",
        usuario_id=1,
        estado=EstadoProyecto.ACTIVO,
        creado_en=datetime.now(),
    )


@pytest.fixture
def tarea():
    """Tarea de prueba."""
    return Tarea(
        id=1,
        titulo="Tarea de prueba",
        descripcion="Descripción de prueba",
        estado=EstadoTarea.PENDIENTE,
        prioridad=PrioridadTarea.MEDIA,
        proyecto_id=1,
        asignado_a=1,
        creada_por=1,
        creada_en=datetime.now(),
    )


@pytest.fixture
def comentario():
    """Comentario de prueba."""
    return Comentario(
        id=1,
        contenido="Este es un comentario de prueba",
        tarea_id=1,
        usuario_id=1,
        creado_en=datetime.now(),
    )


# =============================================================================
# FIXTURES DE REPOSITORIOS
# =============================================================================

@pytest.fixture
def usuario_repo():
    """Repository de usuarios para pruebas."""
    repo = UsuarioRepository()
    # Crear usuario por defecto
    repo.create(Usuario(
        username="existing",
        email="existing@example.com",
        password_hash="hash",
    ))
    return repo


@pytest.fixture
def proyecto_repo():
    """Repository de proyectos para pruebas."""
    return ProyectoRepository()


@pytest.fixture
def tarea_repo():
    """Repository de tareas para pruebas."""
    return TareaRepository()


@pytest.fixture
def comentario_repo():
    """Repository de comentarios para pruebas."""
    return ComentarioRepository()


# =============================================================================
# FIXTURES DE SERVICIOS
# =============================================================================

@pytest.fixture
def usuario_service(usuario_repo):
    """Service de usuarios con repo inyectado."""
    return UsuarioService(usuario_repo)


@pytest.fixture
def proyecto_service(proyecto_repo):
    """Service de proyectos con repo inyectado."""
    return ProyectoService(proyecto_repo)


@pytest.fixture
def tarea_service(tarea_repo):
    """Service de tareas con repo inyectado."""
    return TareaService(tarea_repo)


# =============================================================================
# FIXTURES DE FECHAS
# =============================================================================

@pytest.fixture
def hoy():
    """Fecha actual."""
    return datetime.now().date()


@pytest.fixture
def manana():
    """Fecha mañana."""
    return (datetime.now() + timedelta(days=1)).date()


@pytest.fixture
def ayer():
    """Fecha ayer."""
    return (datetime.now() - timedelta(days=1)).date()


@pytest.fixture
def dentro_de_7_dias():
    """Fecha dentro de 7 días."""
    return (datetime.now() + timedelta(days=7)).date()


# =============================================================================
# FIXTURES UTILIDADES
# =============================================================================

@pytest.fixture
def fake_password_hash():
    """Hash de password falso para pruebas."""
    return "fake_hash_for_testing"


@pytest.fixture
def access_token():
    """Token JWT de acceso falso para pruebas."""
    return "fake_jwt_token_for_testing"


# =============================================================================
# API TESTING FIXTURES (Unidad 3.7 - Tests de Integración)
# =============================================================================

@pytest.fixture
def api_client():
    """
    Cliente de prueba FastAPI.

    Crea una nueva instancia de la aplicación para cada test
    para asegurar aislamiento entre pruebas.

    Unidad: 3.7 - Tests de Integración
    """
    from fastapi.testclient import TestClient
    from src.taskflow.api.app import create_app

    app = create_app()
    return TestClient(app)


@pytest.fixture
def api_auth_token(api_client):
    """
    Crea un usuario y retorna el token de autenticación.

    Este fixture:
    1. Registra un nuevo usuario con credenciales únicas
    2. Inicia sesión para obtener el token JWT
    3. Retorna el access_token para usar en otros tests

    NOTE: Usa un contador para generar credenciales únicas y evitar
    colisiones entre tests que usan este fixture.

    Unidad: 3.7 - Tests de Integración
    """
    import time

    # Generar credenciales únicas usando timestamp para evitar colisiones
    unique_suffix = str(int(time.time() * 1000))
    username = f"testuser_{unique_suffix}"
    email = f"test_{unique_suffix}@example.com"

    # Registrar usuario
    response = api_client.post("/api/auth/register", json={
        "username": username,
        "email": email,
        "password": "testpass123",
        "nombre_completo": "Test User"
    })
    assert response.status_code == 201, f"Fallo al registrar usuario de prueba: {response.json()}"

    # Login para obtener token
    login_response = api_client.post("/api/auth/login", data={
        "username": username,
        "password": "testpass123"
    })

    assert login_response.status_code == 200, "Fallo al iniciar sesión"
    token_data = login_response.json()
    return token_data["access_token"]


@pytest.fixture
def api_auth_headers(api_auth_token):
    """
    Headers HTTP con token de autenticación.

    Unidad: 3.7 - Tests de Integración

    Args:
        api_auth_token: Token JWT de acceso

    Returns:
        Dict con header Authorization configurado
    """
    return {"Authorization": f"Bearer {api_auth_token}"}


@pytest.fixture
def api_proyecto_id(api_client, api_auth_headers):
    """
    Crea un proyecto de prueba y retorna su ID.

    Unidad: 3.7 - Tests de Integración

    Args:
        api_client: Cliente de prueba FastAPI
        api_auth_headers: Headers con autenticación

    Returns:
        int: ID del proyecto creado
    """
    response = api_client.post(
        "/api/proyectos/",
        headers=api_auth_headers,
        json={
            "nombre": "Proyecto de Prueba",
            "descripcion": "Descripción del proyecto de prueba"
        }
    )
    assert response.status_code == 201, "Fallo al crear proyecto de prueba"
    return response.json()["id"]


# =============================================================================
# TEST HELPERS
# =============================================================================

class TestHelpers:
    """
    Clase utilitaria con funciones auxiliares para tests.

    Unidad: 3.7 - Tests de Integración
    """

    @staticmethod
    def assert_valid_response(response, expected_status: int = 200):
        """
        Verifica que la respuesta HTTP tiene el estado esperado.

        Args:
            response: Respuesta de TestClient
            expected_status: Código HTTP esperado

        Raises:
            AssertionError: Si el status code no coincide
        """
        assert response.status_code == expected_status, (
            f"Expected status {expected_status}, got {response.status_code}. "
            f"Response: {response.json() if response.text else 'No content'}"
        )

    @staticmethod
    def assert_auth_required(response):
        """
        Verifica que el endpoint retorna 401 Unauthorized.

        Args:
            response: Respuesta de TestClient
        """
        assert response.status_code == 401, (
            f"Expected 401 Unauthorized, got {response.status_code}"
        )

    @staticmethod
    def assert_validation_error(response):
        """
        Verifica que la respuesta es un error de validación (422).

        Args:
            response: Respuesta de TestClient
        """
        assert response.status_code == 422, (
            f"Expected 422 Validation Error, got {response.status_code}"
        )


@pytest.fixture
def test_helpers():
    """
    Provee la clase de helpers para tests.

    Unidad: 3.7 - Tests de Integración

    Usage:
        def test_alguna_cosa(test_helpers):
            test_helpers.assert_valid_response(response, 201)
    """
    return TestHelpers
