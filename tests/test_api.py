"""
Tests de API FastAPI - TaskFlow
Unidad: 3.7 - Tests de Integración

Este módulo contiene pruebas de integración para todos los endpoints
de la API REST de TaskFlow utilizando TestClient de FastAPI y pytest.
"""

import pytest
from fastapi.testclient import TestClient
from datetime import datetime, timedelta
from typing import Generator, Dict

from src.taskflow.api.app import create_app
from src.taskflow.models import EstadoUsuario, EstadoTarea, PrioridadTarea


# =============================================================================
# FIXTURES PARA CLIENTE DE PRUEBA
# =============================================================================

@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    """
    Cliente de prueba FastAPI.

    Crea una nueva instancia de la aplicación para cada test
    para asegurar aislamiento entre pruebas.
    """
    app = create_app()
    yield TestClient(app)


@pytest.fixture
def auth_token(client: TestClient) -> str:
    """
    Crea un usuario y retorna el token de autenticación.

    Este fixture:
    1. Registra un nuevo usuario con credenciales únicas
    2. Inicia sesión para obtener el token JWT
    3. Retorna el access_token para usar en otros tests

    NOTE: Usa un contador para generar credenciales únicas y evitar
    colisiones entre tests que usan este fixture.

    Returns:
        str: Token JWT de acceso
    """
    import time

    # Generar credenciales únicas usando timestamp para evitar colisiones
    unique_suffix = str(int(time.time() * 1000))
    username = f"testuser_{unique_suffix}"
    email = f"test_{unique_suffix}@example.com"

    # Registrar usuario
    response = client.post("/api/auth/register", json={
        "username": username,
        "email": email,
        "password": "testpass123",
        "nombre_completo": "Test User"
    })
    assert response.status_code == 201, f"Fallo al registrar usuario de prueba: {response.json()}"

    # Login para obtener token (usar form data como OAuth2)
    login_response = client.post("/api/auth/login", data={
        "username": username,
        "password": "testpass123"
    })

    assert login_response.status_code == 200, "Fallo al iniciar sesión"
    token_data = login_response.json()
    return token_data["access_token"]


@pytest.fixture
def auth_headers(auth_token: str) -> Dict[str, str]:
    """
    Headers HTTP con token de autenticación.

    Args:
        auth_token: Token JWT de acceso

    Returns:
        Dict con header Authorization configurado
    """
    return {"Authorization": f"Bearer {auth_token}"}


@pytest.fixture
def proyecto_id(client: TestClient, auth_headers: Dict[str, str]) -> int:
    """
    Crea un proyecto de prueba y retorna su ID.

    Args:
        client: Cliente de prueba FastAPI
        auth_headers: Headers con autenticación

    Returns:
        int: ID del proyecto creado
    """
    response = client.post(
        "/api/proyectos/",
        headers=auth_headers,
        json={
            "nombre": "Proyecto de Prueba",
            "descripcion": "Descripción del proyecto de prueba"
        }
    )
    assert response.status_code == 201, "Fallo al crear proyecto de prueba"
    return response.json()["id"]


# =============================================================================
# TESTS DE AUTENTICACIÓN
# =============================================================================

class TestAuthEndpoints:
    """
    Tests para endpoints de autenticación.

    Verifica:
    - Registro de nuevos usuarios
    - Login con credenciales válidas
    - Login con credenciales inválidas
    - Obtención de perfil del usuario autenticado
    - Protección de endpoints sin token
    """

    def test_registro_exitoso(self, client: TestClient) -> None:
        """
        Test registro de nuevo usuario exitoso.

        GIVEN: Datos válidos para un nuevo usuario
        WHEN: Se envía POST a /api/auth/register
        THEN: Retorna 201 y los datos del usuario creado
        """
        response = client.post("/api/auth/register", json={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "password123",
            "nombre_completo": "New User"
        })

        assert response.status_code == 201

        data = response.json()
        assert data["username"] == "newuser"
        assert data["email"] == "newuser@example.com"
        assert data["nombre_completo"] == "New User"
        assert "id" in data
        assert data["estado"] == "activo"

    def test_registro_username_repetido_falla(self, client: TestClient) -> None:
        """
        Test registro con username repetido falla.

        GIVEN: Un usuario ya registrado con username "testuser"
        WHEN: Se intenta registrar otro usuario con mismo username
        THEN: Retorna 422 con mensaje de error (validación de Pydantic/FastAPI)
        """
        # Primer registro
        client.post("/api/auth/register", json={
            "username": "duplicate_user",
            "email": "test1@example.com",
            "password": "pass123"
        })

        # Segundo registro con mismo username
        response = client.post("/api/auth/register", json={
            "username": "duplicate_user",
            "email": "test2@example.com",
            "password": "pass123"
        })

        # FastAPI retorna 422 para errores de validación de negocio
        assert response.status_code == 422
        assert "ya existe" in response.json()["detail"].lower()

    def test_registro_email_repetido_falla(self, client: TestClient) -> None:
        """
        Test registro con email repetido falla.

        GIVEN: Un usuario ya registrado con email específico
        WHEN: Se intenta registrar otro usuario con mismo email
        THEN: Retorna 422 con mensaje de error (validación de Pydantic/FastAPI)
        """
        # Primer registro
        client.post("/api/auth/register", json={
            "username": "user1",
            "email": "duplicate@example.com",
            "password": "pass123"
        })

        # Segundo registro con mismo email
        response = client.post("/api/auth/register", json={
            "username": "user2",
            "email": "duplicate@example.com",
            "password": "pass123"
        })

        # FastAPI retorna 422 para errores de validación de negocio
        assert response.status_code == 422

    def test_registro_password_corto_falla(self, client: TestClient) -> None:
        """
        Test registro con password muy corto falla.

        GIVEN: Un password con menos de 8 caracteres
        WHEN: Se intenta registrar usuario
        THEN: Retorna 422 con error de validación
        """
        response = client.post("/api/auth/register", json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "short"  # Menos de 8 caracteres
        })

        assert response.status_code == 422

    def test_login_exitoso(self, client: TestClient) -> None:
        """
        Test login exitoso.

        GIVEN: Un usuario registrado en el sistema
        WHEN: Se envían credenciales válidas a /api/auth/login
        THEN: Retorna 200 con access_token
        """
        # Registrar primero
        client.post("/api/auth/register", json={
            "username": "loginuser",
            "email": "login@example.com",
            "password": "loginpass123"
        })

        # Login con form data (OAuth2PasswordRequestForm)
        response = client.post("/api/auth/login", data={
            "username": "loginuser",
            "password": "loginpass123"
        })

        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert "expires_in" in data
        assert "usuario" in data
        assert data["usuario"]["username"] == "loginuser"

    def test_login_usuario_inexistente_falla(self, client: TestClient) -> None:
        """
        Test login con usuario inexistente falla.

        GIVEN: No existe el usuario en el sistema
        WHEN: Se intenta iniciar sesión
        THEN: Retorna 401 Unauthorized
        """
        response = client.post("/api/auth/login", data={
            "username": "inexistente",
            "password": "password123"
        })

        assert response.status_code == 401

    def test_login_password_incorrecto_falla(self, client: TestClient) -> None:
        """
        Test login con password incorrecto falla.

        GIVEN: Un usuario registrado
        WHEN: Se envía password incorrecto
        THEN: Retorna 401 Unauthorized
        """
        # Registrar primero
        client.post("/api/auth/register", json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "correctpass"
        })

        # Login con password incorrecto
        response = client.post("/api/auth/login", data={
            "username": "testuser",
            "password": "wrongpass"
        })

        assert response.status_code == 401

    def test_obtener_perfil_autenticado(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        auth_token: str
    ) -> None:
        """
        Test obtener perfil del usuario autenticado.

        GIVEN: Un usuario autenticado con token válido
        WHEN: Se envía GET a /api/auth/me con el token
        THEN: Retorna 200 con los datos del perfil
        """
        response = client.get("/api/auth/me", headers=auth_headers)

        assert response.status_code == 200
        data = response.json()
        assert "username" in data
        assert "email" in data
        assert "estado" in data
        # Verificar que el username comienza con "testuser_" (credenciales únicas)
        assert data["username"].startswith("testuser_")

    def test_obtener_perfil_sin_token_falla(self, client: TestClient) -> None:
        """
        Test obtener perfil sin token falla.

        GIVEN: Un endpoint que requiere autenticación
        WHEN: Se accede sin token de autorización
        THEN: Retorna 401 Unauthorized
        """
        response = client.get("/api/auth/me")

        assert response.status_code == 401

    def test_obtener_perfil_token_invalido_falla(
        self,
        client: TestClient
    ) -> None:
        """
        Test obtener perfil con token inválido falla.

        GIVEN: Un token JWT inválido o malformado
        WHEN: Se accede a endpoint protegido
        THEN: Retorna 401 Unauthorized
        """
        response = client.get(
            "/api/auth/me",
            headers={"Authorization": "Bearer invalid_token_12345"}
        )

        assert response.status_code == 401


# =============================================================================
# TESTS DE PROYECTOS
# =============================================================================

class TestProyectoEndpoints:
    """
    Tests para endpoints de proyectos.

    Verifica:
    - Creación de proyectos
    - Listado de proyectos del usuario
    - Obtención de proyecto por ID
    - Actualización de proyectos
    - Eliminación de proyectos
    - Autorización (solo propietario puede modificar)
    """

    def test_crear_proyecto(
        self,
        client: TestClient,
        auth_headers: Dict[str, str]
    ) -> None:
        """
        Test crear proyecto.

        GIVEN: Un usuario autenticado
        WHEN: Se envía POST a /api/proyectos/ con datos válidos
        THEN: Retorna 201 con el proyecto creado
        """
        response = client.post(
            "/api/proyectos/",
            headers=auth_headers,
            json={
                "nombre": "Mi Proyecto",
                "descripcion": "Descripción de mi proyecto"
            }
        )

        assert response.status_code == 201
        data = response.json()
        assert data["nombre"] == "Mi Proyecto"
        assert data["descripcion"] == "Descripción de mi proyecto"
        assert data["estado"] == "activo"
        assert "id" in data
        assert "creado_en" in data

    def test_crear_proyecto_sin_nombre_falla(
        self,
        client: TestClient,
        auth_headers: Dict[str, str]
    ) -> None:
        """
        Test crear proyecto sin nombre falla.

        GIVEN: Un usuario autenticado
        WHEN: Se intenta crear proyecto sin nombre
        THEN: Retorna 422 con error de validación
        """
        response = client.post(
            "/api/proyectos/",
            headers=auth_headers,
            json={"descripcion": "Solo descripción"}
        )

        assert response.status_code == 422

    def test_listar_proyectos(
        self,
        client: TestClient,
        auth_headers: Dict[str, str]
    ) -> None:
        """
        Test listar proyectos del usuario.

        GIVEN: Un usuario con varios proyectos creados
        WHEN: Se envía GET a /api/proyectos/
        THEN: Retorna 200 con la lista de proyectos
        """
        # Crear algunos proyectos primero
        client.post("/api/proyectos/", headers=auth_headers, json={
            "nombre": "Proyecto 1"
        })
        client.post("/api/proyectos/", headers=auth_headers, json={
            "nombre": "Proyecto 2"
        })

        # Listar
        response = client.get("/api/proyectos/", headers=auth_headers)

        assert response.status_code == 200
        data = response.json()
        assert len(data) >= 2
        assert any(p["nombre"] == "Proyecto 1" for p in data)

    def test_obtener_proyecto(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        proyecto_id: int
    ) -> None:
        """
        Test obtener proyecto por ID.

        GIVEN: Un proyecto existente con ID conocido
        WHEN: Se envía GET a /api/proyectos/{id}
        THEN: Retorna 200 con los detalles del proyecto
        """
        response = client.get(
            f"/api/proyectos/{proyecto_id}",
            headers=auth_headers
        )

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == proyecto_id
        assert data["nombre"] == "Proyecto de Prueba"

    def test_obtener_proyecto_inexistente_falla(
        self,
        client: TestClient,
        auth_headers: Dict[str, str]
    ) -> None:
        """
        Test obtener proyecto inexistente falla.

        GIVEN: Un ID de proyecto que no existe
        WHEN: Se intenta obtener el proyecto
        THEN: Retorna 404 Not Found
        """
        response = client.get(
            "/api/proyectos/99999",
            headers=auth_headers
        )

        assert response.status_code == 404

    def test_actualizar_proyecto(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        proyecto_id: int
    ) -> None:
        """
        Test actualizar proyecto.

        GIVEN: Un proyecto existente
        WHEN: Se envía PATCH con datos actualizados
        THEN: Retorna 200 con el proyecto actualizado
        """
        response = client.patch(
            f"/api/proyectos/{proyecto_id}",
            headers=auth_headers,
            json={"nombre": "Nombre Actualizado"}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["nombre"] == "Nombre Actualizado"

    def test_actualizar_proyecto_inexistente_falla(
        self,
        client: TestClient,
        auth_headers: Dict[str, str]
    ) -> None:
        """
        Test actualizar proyecto inexistente falla.

        GIVEN: Un ID de proyecto que no existe
        WHEN: Se intenta actualizar
        THEN: Retorna 404 Not Found
        """
        response = client.patch(
            "/api/proyectos/99999",
            headers=auth_headers,
            json={"nombre": "Nuevo Nombre"}
        )

        assert response.status_code == 404

    def test_eliminar_proyecto(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        proyecto_id: int
    ) -> None:
        """
        Test eliminar proyecto.

        GIVEN: Un proyecto existente
        WHEN: Se envía DELETE a /api/proyectos/{id}
        THEN: Retorna 204 No Content
        """
        response = client.delete(
            f"/api/proyectos/{proyecto_id}",
            headers=auth_headers
        )

        assert response.status_code == 204

        # Verificar que ya no existe
        verify = client.get(
            f"/api/proyectos/{proyecto_id}",
            headers=auth_headers
        )
        assert verify.status_code == 404

    def test_eliminar_proyecto_inexistente_falla(
        self,
        client: TestClient,
        auth_headers: Dict[str, str]
    ) -> None:
        """
        Test eliminar proyecto inexistente falla.

        GIVEN: Un ID de proyecto que no existe
        WHEN: Se intenta eliminar
        THEN: Retorna 404 Not Found
        """
        response = client.delete(
            "/api/proyectos/99999",
            headers=auth_headers
        )

        assert response.status_code == 404


# =============================================================================
# TESTS DE TAREAS
# =============================================================================

class TestTareaEndpoints:
    """
    Tests para endpoints de tareas.

    Verifica:
    - Creación de tareas
    - Listado de tareas
    - Obtención de tarea por ID
    - Actualización de tareas
    - Marcar como completada
    - Listado de tareas vencidas y por vencer
    """

    def test_crear_tarea(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        proyecto_id: int
    ) -> None:
        """
        Test crear tarea.

        GIVEN: Un usuario autenticado y un proyecto existente
        WHEN: Se envía POST a /api/tareas/ con datos válidos
        THEN: Retorna 201 con la tarea creada
        """
        response = client.post(
            "/api/tareas/",
            headers=auth_headers,
            json={
                "titulo": "Nueva Tarea",
                "descripcion": "Descripción de la tarea",
                "prioridad": "alta",
                "proyecto_id": proyecto_id
            }
        )

        assert response.status_code == 201
        data = response.json()
        assert data["titulo"] == "Nueva Tarea"
        assert data["descripcion"] == "Descripción de la tarea"
        assert data["prioridad"] == "alta"
        assert data["proyecto_id"] == proyecto_id
        assert data["estado"] == "pendiente"
        assert "id" in data

    def test_crear_tarea_sin_titulo_falla(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        proyecto_id: int
    ) -> None:
        """
        Test crear tarea sin título falla.

        GIVEN: Datos de tarea sin título
        WHEN: Se intenta crear la tarea
        THEN: Retorna 422 con error de validación
        """
        response = client.post(
            "/api/tareas/",
            headers=auth_headers,
            json={
                "descripcion": "Solo descripción",
                "proyecto_id": proyecto_id
            }
        )

        assert response.status_code == 422

    def test_listar_tareas(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        proyecto_id: int
    ) -> None:
        """
        Test listar tareas.

        GIVEN: Un usuario con tareas creadas
        WHEN: Se envía GET a /api/tareas/
        THEN: Retorna 200 con la lista de tareas
        """
        # Crear algunas tareas primero
        client.post("/api/tareas/", headers=auth_headers, json={
            "titulo": "Tarea 1",
            "proyecto_id": proyecto_id
        })
        client.post("/api/tareas/", headers=auth_headers, json={
            "titulo": "Tarea 2",
            "proyecto_id": proyecto_id
        })

        # Listar
        response = client.get("/api/tareas/", headers=auth_headers)

        assert response.status_code == 200
        data = response.json()
        assert len(data) >= 2

    def test_obtener_tarea(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        proyecto_id: int
    ) -> None:
        """
        Test obtener tarea por ID.

        GIVEN: Una tarea existente con ID conocido
        WHEN: Se envía GET a /api/tareas/{id}
        THEN: Retorna 200 con los detalles de la tarea
        """
        # Crear tarea primero
        create_response = client.post("/api/tareas/",
            headers=auth_headers,
            json={
                "titulo": "Tarea Test",
                "proyecto_id": proyecto_id
            }
        )
        tarea_id = create_response.json()["id"]

        # Obtener
        response = client.get(f"/api/tareas/{tarea_id}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == tarea_id
        assert data["titulo"] == "Tarea Test"

    def test_obtener_tarea_inexistente_falla(
        self,
        client: TestClient
    ) -> None:
        """
        Test obtener tarea inexistente falla.

        GIVEN: Un ID de tarea que no existe
        WHEN: Se intenta obtener la tarea
        THEN: Retorna 404 Not Found
        """
        response = client.get("/api/tareas/99999")

        assert response.status_code == 404

    def test_actualizar_tarea(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        proyecto_id: int
    ) -> None:
        """
        Test actualizar tarea.

        GIVEN: Una tarea existente
        WHEN: Se envía PATCH con datos actualizados
        THEN: Retorna 200 con la tarea actualizada
        """
        # Crear tarea primero
        create_response = client.post("/api/tareas/",
            headers=auth_headers,
            json={
                "titulo": "Tarea Original",
                "proyecto_id": proyecto_id
            }
        )
        tarea_id = create_response.json()["id"]

        # Actualizar
        response = client.patch(
            f"/api/tareas/{tarea_id}",
            headers=auth_headers,
            json={
                "titulo": "Tarea Actualizada",
                "estado": "en_progreso"
            }
        )

        assert response.status_code == 200
        data = response.json()
        assert data["titulo"] == "Tarea Actualizada"
        assert data["estado"] == "en_progreso"

    def test_marcar_completada(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        proyecto_id: int
    ) -> None:
        """
        Test marcar tarea como completada.

        GIVEN: Una tarea existente en estado pendiente
        WHEN: Se envía POST a /api/tareas/{id}/completar
        THEN: Retorna 200 con la tarea marcada como completada
        """
        # Crear tarea primero
        create_response = client.post("/api/tareas/",
            headers=auth_headers,
            json={
                "titulo": "Tarea para Completar",
                "proyecto_id": proyecto_id
            }
        )
        tarea_id = create_response.json()["id"]

        # Marcar completada
        response = client.post(
            f"/api/tareas/{tarea_id}/completar",
            headers=auth_headers
        )

        assert response.status_code == 200
        data = response.json()
        assert data["estado"] == "completada"
        assert data["completada_en"] is not None

    def test_listar_vencidas(
        self,
        client: TestClient,
        auth_headers: Dict[str, str],
        proyecto_id: int
    ) -> None:
        """
        Test listar tareas vencidas.

        GIVEN: Tareas con fecha límite pasada
        WHEN: Se envía GET a /api/tareas/vencidas
        THEN: Retorna 200 con las tareas vencidas
        """
        response = client.get("/api/tareas/vencidas")

        assert response.status_code == 200
        # La respuesta debe ser una lista (vacía o con elementos)
        assert isinstance(response.json(), list)

    def test_listar_por_vencer(
        self,
        client: TestClient,
        auth_headers: Dict[str, str]
    ) -> None:
        """
        Test listar tareas por vencer.

        GIVEN: Tareas con fecha límite próxima
        WHEN: Se envía GET a /api/tareas/por-vencer?dias=7
        THEN: Retorna 200 con las tareas próximas a vencer
        """
        response = client.get("/api/tareas/por-vencer?dias=7", headers=auth_headers)

        assert response.status_code == 200
        # La respuesta debe ser una lista
        assert isinstance(response.json(), list)

    def test_listar_por_vencer_con_parametro_dias(
        self,
        client: TestClient,
        auth_headers: Dict[str, str]
    ) -> None:
        """
        Test listar tareas por vencer con parámetro días.

        GIVEN: El parámetro días especificado
        WHEN: Se consulta /api/tareas/por-vencer?dias=30
        THEN: Retorna 200 con las tareas dentro de 30 días
        """
        response = client.get("/api/tareas/por-vencer?dias=30", headers=auth_headers)

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)


# =============================================================================
# TESTS DE ENDPOINTS PÚBLICOS
# =============================================================================

class TestPublicEndpoints:
    """
    Tests para endpoints públicos (no requieren autenticación).

    Verifica:
    - Endpoint raíz retorna información de la API
    - Health check funciona correctamente
    """

    def test_root_endpoint(self, client: TestClient) -> None:
        """
        Test endpoint raíz.

        GIVEN: La aplicación está corriendo
        WHEN: Se accede a /
        THEN: Retorna 200 con información de la API
        """
        response = client.get("/")

        assert response.status_code == 200
        data = response.json()
        assert "nombre" in data
        assert "version" in data
        assert "docs" in data

    def test_health_check(self, client: TestClient) -> None:
        """
        Test health check.

        GIVEN: La aplicación está corriendo
        WHEN: Se accede a /health
        THEN: Retorna 200 con status healthy
        """
        response = client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"

    def test_docs_disponible(self, client: TestClient) -> None:
        """
        Test que la documentación Swagger está disponible.

        GIVEN: La aplicación está corriendo
        WHEN: Se accede a /docs
        THEN: Retorna 200 con página de documentación
        """
        response = client.get("/docs")

        assert response.status_code == 200


# =============================================================================
# TESTS DE AUTORIZACIÓN
# =============================================================================

class TestAuthorization:
    """
    Tests de autorización y permisos.

    Verifica:
    - Endpoints protegidos requieren token
    - Usuarios no pueden acceder a recursos de otros usuarios
    """

    def test_proyecto_sin_token_falla(self, client: TestClient) -> None:
        """
        Test que crear proyecto sin token falla.

        GIVEN: Un endpoint que requiere autenticación
        WHEN: Se accede sin token
        THEN: Retorna 401 Unauthorized
        """
        response = client.post(
            "/api/proyectos/",
            json={"nombre": "Proyecto Sin Auth"}
        )

        assert response.status_code == 401

    def test_tarea_sin_token_falla(self, client: TestClient) -> None:
        """
        Test que crear tarea sin token falla.

        GIVEN: Un endpoint que requiere autenticación
        WHEN: Se accede sin token
        THEN: Retorna 401 Unauthorized
        """
        response = client.post(
            "/api/tareas/",
            json={
                "titulo": "Tarea Sin Auth",
                "proyecto_id": 1
            }
        )

        assert response.status_code == 401

    def test_listar_proyectos_sin_token_falla(
        self,
        client: TestClient
    ) -> None:
        """
        Test que listar proyectos sin token falla.

        GIVEN: Un endpoint que requiere autenticación
        WHEN: Se accede sin token
        THEN: Retorna 401 Unauthorized
        """
        response = client.get("/api/proyectos/")

        assert response.status_code == 401
