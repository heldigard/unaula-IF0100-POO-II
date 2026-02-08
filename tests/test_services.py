"""
Tests de servicios - TaskFlow
Unidad: 2.3 - TDD con Fixtures y Mocks

Este módulo contiene pruebas unitarias para los servicios del dominio.
Los servicios encapsulan la lógica de negocio y coordinan modelos con repositorios.

Estrategia de testing:
- Usamos fixtures pytest para configurar el estado de prueba
- Mockeamos los repositorios para aislar la lógica de negocio
- Probamos casos exitosos y casos edge/error
"""

import pytest
from datetime import datetime, date, timedelta
from unittest.mock import Mock, MagicMock, patch
from typing import Optional

from src.taskflow.models import (
    Usuario,
    Proyecto,
    Tarea,
    EstadoUsuario,
    EstadoProyecto,
    EstadoTarea,
    PrioridadTarea,
)
from src.taskflow.schemas import (
    UsuarioCreate,
    UsuarioUpdate,
    ProyectoCreate,
    ProyectoUpdate,
    TareaCreate,
    TareaUpdate,
)
from src.taskflow.services import (
    UsuarioService,
    ProyectoService,
    TareaService,
)


# =============================================================================
# FIXTURES GLOBALES
# =============================================================================

@pytest.fixture
def mock_usuario_repo():
    """Crea un mock de UsuarioRepository."""
    repo = Mock()
    repo.get_by_username = Mock(return_value=None)
    repo.get_by_email = Mock(return_value=None)
    repo.get_by_id = Mock(return_value=None)
    repo.create = Mock()
    repo.update = Mock()
    repo.get_activos = Mock(return_value=[])
    repo.get_all = Mock(return_value=[])
    return repo


@pytest.fixture
def mock_proyecto_repo():
    """Crea un mock de ProyectoRepository."""
    repo = Mock()
    repo.get_by_id = Mock(return_value=None)
    repo.get_by_usuario = Mock(return_value=[])
    repo.get_all = Mock(return_value=[])
    repo.get_activos = Mock(return_value=[])
    repo.get_archivados = Mock(return_value=[])
    repo.create = Mock()
    repo.update = Mock()
    repo.delete = Mock(return_value=False)
    repo.count = Mock(return_value=0)
    return repo


@pytest.fixture
def mock_tarea_repo():
    """Crea un mock de TareaRepository."""
    repo = Mock()
    repo.get_by_id = Mock(return_value=None)
    repo.get_by_proyecto = Mock(return_value=[])
    repo.get_by_asignado = Mock(return_value=[])
    repo.get_by_creador = Mock(return_value=[])
    repo.get_all = Mock(return_value=[])
    repo.get_pendientes = Mock(return_value=[])
    repo.get_en_progreso = Mock(return_value=[])
    repo.get_vencidas = Mock(return_value=[])
    repo.get_por_vencer = Mock(return_value=[])
    repo.get_by_proyecto_y_estado = Mock(return_value=[])
    repo.create = Mock()
    repo.update = Mock()
    repo.count = Mock(return_value=0)
    return repo


@pytest.fixture
def usuario_service(mock_usuario_repo):
    """Crea una instancia de UsuarioService con repo mockeado."""
    return UsuarioService(mock_usuario_repo)


@pytest.fixture
def proyecto_service(mock_proyecto_repo):
    """Crea una instancia de ProyectoService con repo mockeado."""
    return ProyectoService(mock_proyecto_repo)


@pytest.fixture
def tarea_service(mock_tarea_repo):
    """Crea una instancia de TareaService con repo mockeado."""
    return TareaService(mock_tarea_repo)


@pytest.fixture
def usuario_data():
    """Datos de prueba para crear un usuario."""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",
        "nombre_completo": "Test User"
    }


@pytest.fixture
def proyecto_data():
    """Datos de prueba para crear un proyecto."""
    return {
        "nombre": "Proyecto Test",
        "descripcion": "Descripción de prueba"
    }


@pytest.fixture
def tarea_data():
    """Datos de prueba para crear una tarea."""
    return {
        "titulo": "Nueva Tarea",
        "descripcion": "Descripción de la tarea",
        "prioridad": PrioridadTarea.ALTA,
        "proyecto_id": 1,
        "asignado_a": 1,
    }


# =============================================================================
# TESTS DE USUARIO SERVICE
# =============================================================================

class TestUsuarioService:
    """Tests para UsuarioService."""

    def test_crear_usuario_exitoso(
        self, usuario_service, mock_usuario_repo, usuario_data
    ):
        """Test crear usuario exitosamente."""
        # Configurar mock para devolver None (username disponible)
        mock_usuario_repo.get_by_username.return_value = None
        mock_usuario_repo.get_by_email.return_value = None

        # Usuario creado que debería devolver el repo
        usuario_creado = Usuario(
            id=1,
            username=usuario_data["username"],
            email=usuario_data["email"],
            password_hash="hashed_password",
            nombre_completo=usuario_data["nombre_completo"],
            estado=EstadoUsuario.ACTIVO,
        )
        mock_usuario_repo.create.return_value = usuario_creado

        # Ejecutar
        data = UsuarioCreate(**usuario_data)
        usuario = usuario_service.crear_usuario(data)

        # Validar
        assert usuario is not None
        assert usuario.username == "testuser"
        assert usuario.email == "test@example.com"
        assert usuario.esta_activo()
        mock_usuario_repo.create.assert_called_once()

    def test_crear_usuario_username_repetido_falla(
        self, usuario_service, mock_usuario_repo, usuario_data
    ):
        """Test crear usuario con username existente falla."""
        # Configurar mock para devolver usuario existente
        usuario_existente = Usuario(
            id=1,
            username=usuario_data["username"],
            email="other@example.com",
            password_hash="hash",
        )
        mock_usuario_repo.get_by_username.return_value = usuario_existente

        # Ejecutar y validar excepción
        data = UsuarioCreate(**usuario_data)
        with pytest.raises(ValueError) as exc:
            usuario_service.crear_usuario(data)

        assert "ya existe" in str(exc.value)
        mock_usuario_repo.create.assert_not_called()

    def test_crear_usuario_email_repetido_falla(
        self, usuario_service, mock_usuario_repo, usuario_data
    ):
        """Test crear usuario con email existente falla."""
        # Username disponible, email repetido
        mock_usuario_repo.get_by_username.return_value = None

        usuario_existente = Usuario(
            id=1,
            username="other",
            email=usuario_data["email"],
            password_hash="hash",
        )
        mock_usuario_repo.get_by_email.return_value = usuario_existente

        # Ejecutar y validar excepción
        data = UsuarioCreate(**usuario_data)
        with pytest.raises(ValueError) as exc:
            usuario_service.crear_usuario(data)

        assert "ya está registrado" in str(exc.value)
        mock_usuario_repo.create.assert_not_called()

    def test_autenticar_exitoso(self, usuario_service, mock_usuario_repo):
        """Test autenticación exitosa."""
        # Crear usuario con password hasheado
        import bcrypt
        password = "password123"
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        usuario = Usuario(
            id=1,
            username="testuser",
            email="test@example.com",
            password_hash=password_hash,
            estado=EstadoUsuario.ACTIVO,
        )
        mock_usuario_repo.get_by_username.return_value = usuario

        # Ejecutar
        usuario_auth = usuario_service.autenticar("testuser", password)

        # Validar
        assert usuario_auth is not None
        assert usuario_auth.username == "testuser"
        mock_usuario_repo.get_by_username.assert_called_once_with("testuser")

    def test_autenticar_usuario_inexistente_falla(
        self, usuario_service, mock_usuario_repo
    ):
        """Test autenticación con usuario inexistente falla."""
        mock_usuario_repo.get_by_username.return_value = None

        with pytest.raises(ValueError) as exc:
            usuario_service.autenticar("inexistente", "password123")

        assert "Credenciales inválidas" in str(exc.value)

    def test_autenticar_password_incorrecto_falla(
        self, usuario_service, mock_usuario_repo
    ):
        """Test autenticación con password incorrecto falla."""
        usuario = Usuario(
            id=1,
            username="testuser",
            email="test@example.com",
            password_hash="wrong_hash",
            estado=EstadoUsuario.ACTIVO,
        )
        mock_usuario_repo.get_by_username.return_value = usuario

        # Mock para que verify_password devuelva False
        with patch.object(usuario_service, '_verify_password', return_value=False):
            with pytest.raises(ValueError) as exc:
                usuario_service.autenticar("testuser", "wrong_password")

            assert "Credenciales inválidas" in str(exc.value)

    def test_autenticar_usuario_inactivo_falla(
        self, usuario_service, mock_usuario_repo
    ):
        """Test autenticación con usuario inactivo falla."""
        import bcrypt
        password = "password123"
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        usuario = Usuario(
            id=1,
            username="testuser",
            email="test@example.com",
            password_hash=password_hash,
            estado=EstadoUsuario.INACTIVO,
        )
        mock_usuario_repo.get_by_username.return_value = usuario

        # Mock para que verify_password devuelva True (pero usuario inactivo)
        with patch.object(usuario_service, '_verify_password', return_value=True):
            with pytest.raises(ValueError) as exc:
                usuario_service.autenticar("testuser", password)

            assert "inactivo" in str(exc.value).lower()

    def test_obtener_usuario_existente(
        self, usuario_service, mock_usuario_repo
    ):
        """Test obtener usuario existente por ID."""
        usuario = Usuario(
            id=1,
            username="testuser",
            email="test@example.com",
            password_hash="hash",
        )
        mock_usuario_repo.get_by_id.return_value = usuario

        usuario_obtenido = usuario_service.obtener_usuario(1)

        assert usuario_obtenido is not None
        assert usuario_obtenido.username == "testuser"
        mock_usuario_repo.get_by_id.assert_called_once_with(1)

    def test_obtener_usuario_inexistente_falla(
        self, usuario_service, mock_usuario_repo
    ):
        """Test obtener usuario inexistente falla."""
        mock_usuario_repo.get_by_id.return_value = None

        with pytest.raises(ValueError) as exc:
            usuario_service.obtener_usuario(999)

        assert "no encontrado" in str(exc.value)

    def test_actualizar_usuario(self, usuario_service, mock_usuario_repo):
        """Test actualizar usuario."""
        usuario = Usuario(
            id=1,
            username="testuser",
            email="test@example.com",
            password_hash="hash",
            nombre_completo="Nombre Viejo",
        )
        mock_usuario_repo.get_by_id.return_value = usuario

        usuario_actualizado = Usuario(
            id=1,
            username="testuser",
            email="test@example.com",
            password_hash="hash",
            nombre_completo="Nombre Nuevo",
        )
        mock_usuario_repo.update.return_value = usuario_actualizado

        data = UsuarioUpdate(nombre_completo="Nombre Nuevo")
        resultado = usuario_service.actualizar_usuario(1, data)

        assert resultado.nombre_completo == "Nombre Nuevo"
        mock_usuario_repo.update.assert_called_once()

    def test_cambiar_password_exitoso(self, usuario_service, mock_usuario_repo):
        """Test cambiar password exitosamente."""
        import bcrypt
        password_actual = "oldpass123"
        password_nuevo = "newpass123"
        password_hash = bcrypt.hashpw(
            password_actual.encode('utf-8'), bcrypt.gensalt()
        ).decode('utf-8')

        usuario = Usuario(
            id=1,
            username="testuser",
            email="test@example.com",
            password_hash=password_hash,
        )
        mock_usuario_repo.get_by_id.return_value = usuario
        mock_usuario_repo.update.return_value = usuario

        # Mock verify_password para devolver True
        with patch.object(usuario_service, '_verify_password', return_value=True):
            usuario_service.cambiar_password(1, password_actual, password_nuevo)

            # Verificar que se llamó a update
            mock_usuario_repo.update.assert_called_once()

    def test_cambiar_password_password_actual_incorrecto_falla(
        self, usuario_service, mock_usuario_repo
    ):
        """Test cambiar password con password actual incorrecto falla."""
        usuario = Usuario(
            id=1,
            username="testuser",
            email="test@example.com",
            password_hash="hash",
        )
        mock_usuario_repo.get_by_id.return_value = usuario

        with patch.object(usuario_service, '_verify_password', return_value=False):
            with pytest.raises(ValueError) as exc:
                usuario_service.cambiar_password(1, "wrong", "newpass123")

            assert "incorrecto" in str(exc.value).lower()
            mock_usuario_repo.update.assert_not_called()

    def test_cambiar_password_nuevo_corto_falla(
        self, usuario_service, mock_usuario_repo
    ):
        """Test cambiar password con nuevo password muy corto falla."""
        usuario = Usuario(
            id=1,
            username="testuser",
            email="test@example.com",
            password_hash="hash",
        )
        mock_usuario_repo.get_by_id.return_value = usuario

        with patch.object(usuario_service, '_verify_password', return_value=True):
            with pytest.raises(ValueError) as exc:
                usuario_service.cambiar_password(1, "oldpass123", "corto")

            assert "8+ caracteres" in str(exc.value) or "8" in str(exc.value)
            mock_usuario_repo.update.assert_not_called()

    def test_listar_activos(self, usuario_service, mock_usuario_repo):
        """Test listar usuarios activos."""
        usuarios = [
            Usuario(id=1, username="user1", email="user1@example.com", password_hash="h1"),
            Usuario(id=2, username="user2", email="user2@example.com", password_hash="h2"),
        ]
        mock_usuario_repo.get_activos.return_value = usuarios

        resultado = usuario_service.listar_activos()

        assert len(resultado) == 2
        mock_usuario_repo.get_activos.assert_called_once()

    def test_listar_todos(self, usuario_service, mock_usuario_repo):
        """Test listar todos los usuarios."""
        usuarios = [
            Usuario(id=1, username="user1", email="user1@example.com", password_hash="h1"),
            Usuario(id=2, username="user2", email="user2@example.com", password_hash="h2"),
        ]
        mock_usuario_repo.get_all.return_value = usuarios

        resultado = usuario_service.listar_todos()

        assert len(resultado) == 2
        mock_usuario_repo.get_all.assert_called_once()


# =============================================================================
# TESTS DE PROYECTO SERVICE
# =============================================================================

class TestProyectoService:
    """Tests para ProyectoService."""

    def test_crear_proyecto_exitoso(
        self, proyecto_service, mock_proyecto_repo, proyecto_data
    ):
        """Test crear proyecto exitosamente."""
        # Configurar mocks
        proyecto_creado = Proyecto(
            id=1,
            nombre=proyecto_data["nombre"],
            descripcion=proyecto_data["descripcion"],
            usuario_id=1,
            estado=EstadoProyecto.ACTIVO,
        )
        mock_proyecto_repo.create.return_value = proyecto_creado

        # Ejecutar
        data = ProyectoCreate(**proyecto_data)
        proyecto = proyecto_service.crear_proyecto(usuario_id=1, data=data)

        # Validar
        assert proyecto.id is not None
        assert proyecto.nombre == "Proyecto Test"
        assert proyecto.usuario_id == 1
        assert proyecto.estado == EstadoProyecto.ACTIVO
        mock_proyecto_repo.create.assert_called_once()

    def test_obtener_proyecto_con_permiso(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test obtener proyecto con permiso correcto."""
        proyecto = Proyecto(
            id=1,
            nombre="Mi Proyecto",
            descripcion="Descripción",
            usuario_id=1,
            estado=EstadoProyecto.ACTIVO,
        )
        mock_proyecto_repo.get_by_id.return_value = proyecto

        # Obtener con mismo usuario_id (permiso)
        resultado = proyecto_service.obtener_proyecto(1, usuario_id=1)

        assert resultado is not None
        assert resultado.nombre == "Mi Proyecto"
        mock_proyecto_repo.get_by_id.assert_called_once_with(1)

    def test_obtener_proyecto_sin_permiso_falla(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test obtener proyecto sin permiso falla."""
        proyecto = Proyecto(
            id=1,
            nombre="Mi Proyecto",
            descripcion="Descripción",
            usuario_id=1,  # Pertenece al usuario 1
            estado=EstadoProyecto.ACTIVO,
        )
        mock_proyecto_repo.get_by_id.return_value = proyecto

        # Intentar obtener con diferente usuario_id
        with pytest.raises(ValueError) as exc:
            proyecto_service.obtener_proyecto(1, usuario_id=2)

        assert "permiso" in str(exc.value).lower()

    def test_obtener_proyecto_sin_filtro_usuario(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test obtener proyecto sin filtro de usuario (admin)."""
        proyecto = Proyecto(
            id=1,
            nombre="Mi Proyecto",
            descripcion="Descripción",
            usuario_id=1,
            estado=EstadoProyecto.ACTIVO,
        )
        mock_proyecto_repo.get_by_id.return_value = proyecto

        # Obtener sin usuario_id (sin verificación de permiso)
        resultado = proyecto_service.obtener_proyecto(1)

        assert resultado is not None
        assert resultado.nombre == "Mi Proyecto"

    def test_listar_proyectos_filtrados(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test listar proyectos filtrados por usuario."""
        # Crear proyectos para diferentes usuarios
        proyectos = [
            Proyecto(id=1, nombre="Proyecto Usuario 1", usuario_id=1, estado=EstadoProyecto.ACTIVO),
            Proyecto(id=2, nombre="Proyecto Usuario 2", usuario_id=2, estado=EstadoProyecto.ACTIVO),
        ]
        mock_proyecto_repo.get_by_usuario.return_value = [proyectos[0]]

        # Listar proyectos del usuario 1
        resultado = proyecto_service.listar_proyectos(usuario_id=1)

        assert len(resultado) == 1
        assert resultado[0].nombre == "Proyecto Usuario 1"
        mock_proyecto_repo.get_by_usuario.assert_called_once_with(1)

    def test_listar_todos_los_proyectos(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test listar todos los proyectos sin filtro."""
        proyectos = [
            Proyecto(id=1, nombre="Proyecto 1", usuario_id=1, estado=EstadoProyecto.ACTIVO),
            Proyecto(id=2, nombre="Proyecto 2", usuario_id=2, estado=EstadoProyecto.ACTIVO),
        ]
        mock_proyecto_repo.get_all.return_value = proyectos

        resultado = proyecto_service.listar_proyectos()

        assert len(resultado) == 2
        mock_proyecto_repo.get_all.assert_called_once()

    def test_archivar_proyecto(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test archivar proyecto."""
        proyecto = Proyecto(
            id=1,
            nombre="A Archivar",
            descripcion="Descripción",
            usuario_id=1,
            estado=EstadoProyecto.ACTIVO,
        )
        mock_proyecto_repo.get_by_id.return_value = proyecto

        proyecto_archivado = Proyecto(
            id=1,
            nombre="A Archivar",
            descripcion="Descripción",
            usuario_id=1,
            estado=EstadoProyecto.ARCHIVADO,
        )
        mock_proyecto_repo.update.return_value = proyecto_archivado

        resultado = proyecto_service.archivar_proyecto(1, usuario_id=1)

        assert resultado.estado == EstadoProyecto.ARCHIVADO
        mock_proyecto_repo.update.assert_called_once()

    def test_reactivar_proyecto(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test reactivar proyecto."""
        proyecto = Proyecto(
            id=1,
            nombre="Proyecto",
            descripcion="Descripción",
            usuario_id=1,
            estado=EstadoProyecto.ARCHIVADO,
        )
        mock_proyecto_repo.get_by_id.return_value = proyecto

        proyecto_reactivado = Proyecto(
            id=1,
            nombre="Proyecto",
            descripcion="Descripción",
            usuario_id=1,
            estado=EstadoProyecto.ACTIVO,
        )
        mock_proyecto_repo.update.return_value = proyecto_reactivado

        resultado = proyecto_service.reactivar_proyecto(1, usuario_id=1)

        assert resultado.estado == EstadoProyecto.ACTIVO
        mock_proyecto_repo.update.assert_called_once()

    def test_completar_proyecto(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test completar proyecto."""
        proyecto = Proyecto(
            id=1,
            nombre="Proyecto",
            descripcion="Descripción",
            usuario_id=1,
            estado=EstadoProyecto.ACTIVO,
        )
        mock_proyecto_repo.get_by_id.return_value = proyecto

        proyecto_completado = Proyecto(
            id=1,
            nombre="Proyecto",
            descripcion="Descripción",
            usuario_id=1,
            estado=EstadoProyecto.COMPLETADO,
        )
        mock_proyecto_repo.update.return_value = proyecto_completado

        resultado = proyecto_service.completar_proyecto(1, usuario_id=1)

        assert resultado.estado == EstadoProyecto.COMPLETADO
        mock_proyecto_repo.update.assert_called_once()

    def test_actualizar_proyecto(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test actualizar proyecto."""
        proyecto = Proyecto(
            id=1,
            nombre="Nombre Original",
            descripcion="Descripción Original",
            usuario_id=1,
            estado=EstadoProyecto.ACTIVO,
        )
        mock_proyecto_repo.get_by_id.return_value = proyecto

        proyecto_actualizado = Proyecto(
            id=1,
            nombre="Nombre Actualizado",
            descripcion="Descripción Actualizada",
            usuario_id=1,
            estado=EstadoProyecto.COMPLETADO,
        )
        mock_proyecto_repo.update.return_value = proyecto_actualizado

        data = ProyectoUpdate(
            nombre="Nombre Actualizado",
            descripcion="Descripción Actualizada",
            estado=EstadoProyecto.COMPLETADO,
        )
        resultado = proyecto_service.actualizar_proyecto(1, data, usuario_id=1)

        assert resultado.nombre == "Nombre Actualizado"
        assert resultado.estado == EstadoProyecto.COMPLETADO
        mock_proyecto_repo.update.assert_called_once()

    def test_eliminar_proyecto(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test eliminar proyecto."""
        proyecto = Proyecto(
            id=1,
            nombre="Proyecto",
            descripcion="Descripción",
            usuario_id=1,
            estado=EstadoProyecto.ACTIVO,
        )
        mock_proyecto_repo.get_by_id.return_value = proyecto
        mock_proyecto_repo.delete.return_value = True

        resultado = proyecto_service.eliminar_proyecto(1, usuario_id=1)

        assert resultado is True
        mock_proyecto_repo.delete.assert_called_once_with(1)

    def test_contar_proyectos(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test contar proyectos."""
        mock_proyecto_repo.count.return_value = 5

        total = proyecto_service.contar_proyectos()

        assert total == 5
        mock_proyecto_repo.count.assert_called_once()

    def test_contar_proyectos_por_usuario(
        self, proyecto_service, mock_proyecto_repo
    ):
        """Test contar proyectos de un usuario específico."""
        proyectos = [
            Proyecto(id=1, nombre="P1", usuario_id=1, estado=EstadoProyecto.ACTIVO),
            Proyecto(id=2, nombre="P2", usuario_id=1, estado=EstadoProyecto.ACTIVO),
            Proyecto(id=3, nombre="P3", usuario_id=1, estado=EstadoProyecto.ACTIVO),
        ]
        mock_proyecto_repo.get_by_usuario.return_value = proyectos

        total = proyecto_service.contar_proyectos(usuario_id=1)

        assert total == 3
        mock_proyecto_repo.get_by_usuario.assert_called_once_with(1)


# =============================================================================
# TESTS DE TAREA SERVICE
# =============================================================================

class TestTareaService:
    """Tests para TareaService."""

    def test_crear_tarea_exitoso(
        self, tarea_service, mock_tarea_repo, tarea_data
    ):
        """Test crear tarea exitosamente."""
        tarea_creada = Tarea(
            id=1,
            titulo=tarea_data["titulo"],
            descripcion=tarea_data["descripcion"],
            prioridad=tarea_data["prioridad"],
            proyecto_id=tarea_data["proyecto_id"],
            asignado_a=tarea_data["asignado_a"],
            creada_por=1,
            estado=EstadoTarea.PENDIENTE,
        )
        mock_tarea_repo.create.return_value = tarea_creada

        data = TareaCreate(**tarea_data)
        tarea = tarea_service.crear_tarea(data, creada_por=1)

        assert tarea.id is not None
        assert tarea.titulo == "Nueva Tarea"
        assert tarea.estado == EstadoTarea.PENDIENTE
        assert tarea.prioridad == PrioridadTarea.ALTA
        mock_tarea_repo.create.assert_called_once()

    def test_marcar_completada(self, tarea_service, mock_tarea_repo):
        """Test marcar tarea como completada."""
        tarea = Tarea(
            id=1,
            titulo="Tarea",
            proyecto_id=1,
            creada_por=1,
            estado=EstadoTarea.PENDIENTE,
        )
        mock_tarea_repo.get_by_id.return_value = tarea

        tarea_completada = Tarea(
            id=1,
            titulo="Tarea",
            proyecto_id=1,
            creada_por=1,
            estado=EstadoTarea.COMPLETADA,
            completada_en=datetime.now(),
        )
        mock_tarea_repo.update.return_value = tarea_completada

        resultado = tarea_service.marcar_completada(1)

        assert resultado.estado == EstadoTarea.COMPLETADA
        assert resultado.completada_en is not None
        mock_tarea_repo.update.assert_called_once()

    def test_iniciar_tarea(self, tarea_service, mock_tarea_repo):
        """Test iniciar tarea (cambiar a EN_PROGRESO)."""
        tarea = Tarea(
            id=1,
            titulo="Tarea",
            proyecto_id=1,
            creada_por=1,
            estado=EstadoTarea.PENDIENTE,
        )
        mock_tarea_repo.get_by_id.return_value = tarea

        tarea_en_progreso = Tarea(
            id=1,
            titulo="Tarea",
            proyecto_id=1,
            creada_por=1,
            estado=EstadoTarea.EN_PROGRESO,
        )
        mock_tarea_repo.update.return_value = tarea_en_progreso

        resultado = tarea_service.iniciar_tarea(1)

        assert resultado.estado == EstadoTarea.EN_PROGRESO
        mock_tarea_repo.update.assert_called_once()

    def test_cancelar_tarea(self, tarea_service, mock_tarea_repo):
        """Test cancelar tarea."""
        tarea = Tarea(
            id=1,
            titulo="Tarea",
            proyecto_id=1,
            creada_por=1,
            estado=EstadoTarea.PENDIENTE,
        )
        mock_tarea_repo.get_by_id.return_value = tarea

        tarea_cancelada = Tarea(
            id=1,
            titulo="Tarea",
            proyecto_id=1,
            creada_por=1,
            estado=EstadoTarea.CANCELADA,
        )
        mock_tarea_repo.update.return_value = tarea_cancelada

        resultado = tarea_service.cancelar_tarea(1)

        assert resultado.estado == EstadoTarea.CANCELADA
        mock_tarea_repo.update.assert_called_once()

    def test_actualizar_tarea(self, tarea_service, mock_tarea_repo):
        """Test actualizar tarea."""
        tarea = Tarea(
            id=1,
            titulo="Tarea Original",
            descripcion="Descripción Original",
            proyecto_id=1,
            creada_por=1,
            estado=EstadoTarea.PENDIENTE,
            prioridad=PrioridadTarea.MEDIA,
        )
        mock_tarea_repo.get_by_id.return_value = tarea

        tarea_actualizada = Tarea(
            id=1,
            titulo="Tarea Actualizada",
            descripcion="Descripción Actualizada",
            proyecto_id=1,
            creada_por=1,
            estado=EstadoTarea.EN_PROGRESO,
            prioridad=PrioridadTarea.ALTA,
        )
        mock_tarea_repo.update.return_value = tarea_actualizada

        data = TareaUpdate(
            titulo="Tarea Actualizada",
            descripcion="Descripción Actualizada",
            estado=EstadoTarea.EN_PROGRESO,
            prioridad=PrioridadTarea.ALTA,
        )
        resultado = tarea_service.actualizar_tarea(1, data)

        assert resultado.titulo == "Tarea Actualizada"
        assert resultado.estado == EstadoTarea.EN_PROGRESO
        assert resultado.prioridad == PrioridadTarea.ALTA
        mock_tarea_repo.update.assert_called_once()

    def test_obtener_tarea_existente(self, tarea_service, mock_tarea_repo):
        """Test obtener tarea existente por ID."""
        tarea = Tarea(
            id=1,
            titulo="Tarea Test",
            proyecto_id=1,
            creada_por=1,
        )
        mock_tarea_repo.get_by_id.return_value = tarea

        resultado = tarea_service.obtener_tarea(1)

        assert resultado is not None
        assert resultado.titulo == "Tarea Test"
        mock_tarea_repo.get_by_id.assert_called_once_with(1)

    def test_obtener_tarea_inexistente_falla(self, tarea_service, mock_tarea_repo):
        """Test obtener tarea inexistente falla."""
        mock_tarea_repo.get_by_id.return_value = None

        with pytest.raises(ValueError) as exc:
            tarea_service.obtener_tarea(999)

        assert "no encontrada" in str(exc.value)

    def test_listar_tareas_sin_filtros(self, tarea_service, mock_tarea_repo):
        """Test listar tareas sin filtros."""
        tareas = [
            Tarea(id=1, titulo="Tarea 1", proyecto_id=1, creada_por=1),
            Tarea(id=2, titulo="Tarea 2", proyecto_id=1, creada_por=1),
        ]
        mock_tarea_repo.get_all.return_value = tareas

        resultado = tarea_service.listar_tareas()

        assert len(resultado) == 2
        mock_tarea_repo.get_all.assert_called_once()

    def test_listar_tareas_con_filtro_proyecto(
        self, tarea_service, mock_tarea_repo
    ):
        """Test listar tareas filtradas por proyecto."""
        # El servicio filtra después de obtener todas las tareas
        tareas = [
            Tarea(id=1, titulo="Tarea P1", proyecto_id=1, creada_por=1),
            Tarea(id=2, titulo="Tarea P2", proyecto_id=2, creada_por=1),
        ]
        mock_tarea_repo.get_all.return_value = tareas

        resultado = tarea_service.listar_tareas(proyecto_id=1)

        assert len(resultado) == 1
        assert resultado[0].proyecto_id == 1

    def test_listar_tareas_con_filtro_estado(
        self, tarea_service, mock_tarea_repo
    ):
        """Test listar tareas filtradas por estado."""
        tareas = [
            Tarea(id=1, titulo="Tarea P1", proyecto_id=1, creada_por=1, estado=EstadoTarea.PENDIENTE),
            Tarea(id=2, titulo="Tarea P2", proyecto_id=1, creada_por=1, estado=EstadoTarea.COMPLETADA),
        ]
        mock_tarea_repo.get_all.return_value = tareas

        resultado = tarea_service.listar_tareas(estado=EstadoTarea.PENDIENTE)

        assert len(resultado) == 1
        assert resultado[0].estado == EstadoTarea.PENDIENTE

    def test_listar_vencidas(self, tarea_service, mock_tarea_repo):
        """Test listar tareas vencidas."""
        tareas = [
            Tarea(
                id=1,
                titulo="Vencida",
                proyecto_id=1,
                creada_por=1,
                fecha_limite=date.today() - timedelta(days=5),
                estado=EstadoTarea.PENDIENTE,
            ),
        ]
        mock_tarea_repo.get_vencidas.return_value = tareas

        resultado = tarea_service.listar_vencidas()

        assert len(resultado) == 1
        mock_tarea_repo.get_vencidas.assert_called_once()

    def test_listar_por_vencer(self, tarea_service, mock_tarea_repo):
        """Test listar tareas próximas a vencer."""
        tareas = [
            Tarea(
                id=1,
                titulo="Por vencer",
                proyecto_id=1,
                creada_por=1,
                fecha_limite=date.today() + timedelta(days=3),
                estado=EstadoTarea.PENDIENTE,
            ),
        ]
        mock_tarea_repo.get_por_vencer.return_value = tareas

        resultado = tarea_service.listar_por_vencer(dias=7)

        assert len(resultado) == 1
        mock_tarea_repo.get_por_vencer.assert_called_once_with(7)

    def test_listar_tareas_proyecto(self, tarea_service, mock_tarea_repo):
        """Test listar todas las tareas de un proyecto."""
        tareas = [
            Tarea(id=1, titulo="T1", proyecto_id=1, creada_por=1),
            Tarea(id=2, titulo="T2", proyecto_id=1, creada_por=1),
        ]
        mock_tarea_repo.get_by_proyecto.return_value = tareas

        resultado = tarea_service.listar_tareas_proyecto(1)

        assert len(resultado) == 2
        assert all(t.proyecto_id == 1 for t in resultado)
        mock_tarea_repo.get_by_proyecto.assert_called_once_with(1)

    def test_listar_tareas_asignadas(self, tarea_service, mock_tarea_repo):
        """Test listar tareas asignadas a un usuario."""
        tareas = [
            Tarea(id=1, titulo="T1", proyecto_id=1, creada_por=1, asignado_a=2),
            Tarea(id=2, titulo="T2", proyecto_id=1, creada_por=1, asignado_a=2),
        ]
        mock_tarea_repo.get_by_asignado.return_value = tareas

        resultado = tarea_service.listar_tareas_asignadas(2)

        assert len(resultado) == 2
        assert all(t.asignado_a == 2 for t in resultado)
        mock_tarea_repo.get_by_asignado.assert_called_once_with(2)

    def test_listar_tareas_creadas(self, tarea_service, mock_tarea_repo):
        """Test listar tareas creadas por un usuario."""
        tareas = [
            Tarea(id=1, titulo="T1", proyecto_id=1, creada_por=1),
            Tarea(id=2, titulo="T2", proyecto_id=1, creada_por=1),
        ]
        mock_tarea_repo.get_by_creador.return_value = tareas

        resultado = tarea_service.listar_tareas_creadas(1)

        assert len(resultado) == 2
        assert all(t.creada_por == 1 for t in resultado)
        mock_tarea_repo.get_by_creador.assert_called_once_with(1)

    def test_obtener_estadisticas_proyecto(self, tarea_service, mock_tarea_repo):
        """Test obtener estadísticas de tareas de un proyecto."""
        tareas = [
            Tarea(id=1, titulo="T1", proyecto_id=1, creada_por=1, estado=EstadoTarea.PENDIENTE, prioridad=PrioridadTarea.ALTA),
            Tarea(id=2, titulo="T2", proyecto_id=1, creada_por=1, estado=EstadoTarea.EN_PROGRESO, prioridad=PrioridadTarea.MEDIA),
            Tarea(id=3, titulo="T3", proyecto_id=1, creada_por=1, estado=EstadoTarea.COMPLETADA, prioridad=PrioridadTarea.BAJA),
            Tarea(id=4, titulo="T4", proyecto_id=1, creada_por=1, estado=EstadoTarea.COMPLETADA, prioridad=PrioridadTarea.BAJA),
        ]
        mock_tarea_repo.get_by_proyecto.return_value = tareas

        stats = tarea_service.obtener_estadisticas_proyecto(1)

        assert stats['total'] == 4
        assert stats['pendientes'] == 1
        assert stats['en_progreso'] == 1
        assert stats['completadas'] == 2
        assert stats['por_prioridad']['alta'] == 1
        assert stats['por_prioridad']['media'] == 1
        assert stats['por_prioridad']['baja'] == 2
        mock_tarea_repo.get_by_proyecto.assert_called_once_with(1)

    def test_contar_tareas(self, tarea_service, mock_tarea_repo):
        """Test contar el total de tareas."""
        mock_tarea_repo.count.return_value = 10

        total = tarea_service.contar_tareas()

        assert total == 10
        mock_tarea_repo.count.assert_called_once()

    def test_contar_tareas_por_proyecto(self, tarea_service, mock_tarea_repo):
        """Test contar tareas de un proyecto específico."""
        tareas = [
            Tarea(id=1, titulo="T1", proyecto_id=1, creada_por=1),
            Tarea(id=2, titulo="T2", proyecto_id=1, creada_por=1),
            Tarea(id=3, titulo="T3", proyecto_id=1, creada_por=1),
        ]
        mock_tarea_repo.get_by_proyecto.return_value = tareas

        total = tarea_service.contar_tareas(proyecto_id=1)

        assert total == 3
        mock_tarea_repo.get_by_proyecto.assert_called_once_with(1)

    def test_listar_tareas_pendientes(self, tarea_service, mock_tarea_repo):
        """Test listar tareas pendientes."""
        tareas = [
            Tarea(id=1, titulo="T1", proyecto_id=1, creada_por=1, estado=EstadoTarea.PENDIENTE),
            Tarea(id=2, titulo="T2", proyecto_id=1, creada_por=1, estado=EstadoTarea.PENDIENTE),
        ]
        mock_tarea_repo.get_pendientes.return_value = tareas

        resultado = tarea_service.listar_tareas_pendientes()

        assert len(resultado) == 2
        assert all(t.esta_pendiente() for t in resultado)
        mock_tarea_repo.get_pendientes.assert_called_once()

    def test_listar_tareas_en_progreso(self, tarea_service, mock_tarea_repo):
        """Test listar tareas en progreso."""
        tareas = [
            Tarea(id=1, titulo="T1", proyecto_id=1, creada_por=1, estado=EstadoTarea.EN_PROGRESO),
        ]
        mock_tarea_repo.get_en_progreso.return_value = tareas

        resultado = tarea_service.listar_tareas_en_progreso()

        assert len(resultado) == 1
        assert all(t.esta_en_progreso() for t in resultado)
        mock_tarea_repo.get_en_progreso.assert_called_once()

    def test_listar_tareas_pendientes_por_proyecto(
        self, tarea_service, mock_tarea_repo
    ):
        """Test listar tareas pendientes de un proyecto."""
        tareas = [
            Tarea(id=1, titulo="T1", proyecto_id=1, creada_por=1, estado=EstadoTarea.PENDIENTE),
        ]
        mock_tarea_repo.get_by_proyecto_y_estado.return_value = tareas

        resultado = tarea_service.listar_tareas_pendientes(proyecto_id=1)

        assert len(resultado) == 1
        mock_tarea_repo.get_by_proyecto_y_estado.assert_called_once_with(1, EstadoTarea.PENDIENTE)
