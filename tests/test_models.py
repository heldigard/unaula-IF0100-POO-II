"""
Tests de modelos - TaskFlow
Unidad: 2.1 - Introducción a TDD

Este módulo contiene pruebas unitarias completas para todos los modelos
del sistema TaskFlow: Usuario, Proyecto, Tarea y Comentario.

Cada clase de prueba sigue el patrón Arrange-Act-Assert y cubre:
- Creación con campos mínimos y completos
- Validaciones de negocio
- Métodos de estado
- Representaciones string (__str__, __repr__)
- Métodos mágicos (__len__, __lt__, etc.)
"""

from datetime import datetime, date, timedelta

import pytest

from src.taskflow.models import (
    Usuario,
    UsuarioCreacion,
    UsuarioRespuesta,
    Proyecto,
    Tarea,
    Comentario,
    EstadoUsuario,
    EstadoProyecto,
    EstadoTarea,
    PrioridadTarea,
)


# =============================================================================
# TESTS DE USUARIO
# =============================================================================

class TestUsuario:
    """Tests para el modelo Usuario."""

    def test_creacion_usuario_minimo(self):
        """Test crear usuario con campos mínimos."""
        # Arrange & Act
        usuario = Usuario(username="jdoe", email="john@example.com")

        # Assert
        assert usuario.username == "jdoe"
        assert usuario.email == "john@example.com"
        assert usuario.id is None
        assert usuario.estado == EstadoUsuario.ACTIVO
        assert usuario.password_hash is None
        assert usuario.nombre_completo is None

    def test_creacion_usuario_completo(self):
        """Test crear usuario con todos los campos."""
        # Arrange
        ahora = datetime.now()

        # Act
        usuario = Usuario(
            id=1,
            username="jdoe",
            email="john@example.com",
            password_hash="hash_secreto",
            nombre_completo="John Doe",
            estado=EstadoUsuario.ACTIVO,
            creado_en=ahora,
            actualizado_en=ahora,
        )

        # Assert
        assert usuario.id == 1
        assert usuario.nombre_completo == "John Doe"
        assert usuario.password_hash == "hash_secreto"
        assert usuario.estado == EstadoUsuario.ACTIVO

    def test_validacion_username_corto(self):
        """Test que username corto falla validación."""
        # Arrange
        usuario = Usuario(username="ab", email="test@example.com")

        # Act
        errores = usuario.validar()

        # Assert
        assert len(errores) > 0
        assert any("Username debe tener al menos 3 caracteres" in e for e in errores)

    def test_validacion_username_vacio(self):
        """Test que username vacío falla validación."""
        # Arrange
        usuario = Usuario(username="", email="test@example.com")

        # Act
        errores = usuario.validar()

        # Assert
        assert any("Username debe tener al menos 3 caracteres" in e for e in errores)

    def test_validacion_username_largo(self):
        """Test que username muy largo falla validación."""
        # Arrange
        usuario = Usuario(username="a" * 51, email="test@example.com")

        # Act
        errores = usuario.validar()

        # Assert
        assert any("Username no puede exceder 50 caracteres" in e for e in errores)

    def test_validacion_email_invalido(self):
        """Test que email inválido falla validación."""
        # Arrange
        usuario = Usuario(username="test", email="invalido")

        # Act
        errores = usuario.validar()

        # Assert
        assert any("Email inválido" in e for e in errores)

    def test_validacion_email_vacio(self):
        """Test que email vacío falla validación."""
        # Arrange
        usuario = Usuario(username="testuser", email="")

        # Act
        errores = usuario.validar()

        # Assert
        assert any("Email inválido" in e for e in errores)

    def test_validacion_email_valido(self):
        """Test que email válido pasa validación."""
        # Arrange
        usuario = Usuario(username="test", email="test@example.com")

        # Act
        errores = usuario.validar()

        # Assert
        assert not any("Email" in e for e in errores)

    def test_validacion_nombre_completo_largo(self):
        """Test que nombre completo muy largo falla validación."""
        # Arrange
        usuario = Usuario(
            username="test",
            email="test@example.com",
            nombre_completo="a" * 101
        )

        # Act
        errores = usuario.validar()

        # Assert
        assert any("Nombre completo no puede exceder 100 caracteres" in e for e in errores)

    def test_es_valido_true(self):
        """Test método es_valido retorna True para usuario válido."""
        # Arrange
        usuario = Usuario(username="testuser", email="test@example.com")

        # Act & Assert
        assert usuario.es_valido() is True

    def test_es_valido_false(self):
        """Test método es_valido retorna False para usuario inválido."""
        # Arrange
        usuario = Usuario(username="ab", email="test@example.com")

        # Act & Assert
        assert usuario.es_valido() is False

    def test_activar(self):
        """Test activar usuario."""
        # Arrange
        usuario = Usuario(
            username="test",
            email="test@example.com",
            estado=EstadoUsuario.INACTIVO
        )

        # Act
        usuario.activar()

        # Assert
        assert usuario.estado == EstadoUsuario.ACTIVO
        assert usuario.actualizado_en is not None

    def test_desactivar(self):
        """Test desactivar usuario."""
        # Arrange
        usuario = Usuario(
            username="test",
            email="test@example.com",
            estado=EstadoUsuario.ACTIVO
        )

        # Act
        usuario.desactivar()

        # Assert
        assert usuario.estado == EstadoUsuario.INACTIVO
        assert usuario.actualizado_en is not None

    def test_suspender(self):
        """Test suspender usuario."""
        # Arrange
        usuario = Usuario(
            username="test",
            email="test@example.com",
            estado=EstadoUsuario.ACTIVO
        )

        # Act
        usuario.suspender()

        # Assert
        assert usuario.estado == EstadoUsuario.SUSPENDIDO
        assert usuario.actualizado_en is not None

    def test_esta_activo_true(self):
        """Test esta_activo retorna True cuando usuario está activo."""
        # Arrange
        usuario = Usuario(
            username="test",
            email="test@example.com",
            estado=EstadoUsuario.ACTIVO
        )

        # Act & Assert
        assert usuario.esta_activo() is True

    def test_esta_activo_false(self):
        """Test esta_activo retorna False cuando usuario no está activo."""
        # Arrange
        usuario = Usuario(
            username="test",
            email="test@example.com",
            estado=EstadoUsuario.INACTIVO
        )

        # Act & Assert
        assert usuario.esta_activo() is False

    def test_str_repr(self):
        """Test representaciones string."""
        # Arrange
        usuario = Usuario(id=1, username="jdoe", email="john@example.com")

        # Act & Assert
        assert str(usuario) == "Usuario(jdoe)"
        assert "jdoe" in repr(usuario)
        assert "john@example.com" in repr(usuario)
        assert "id=1" in repr(usuario)


# =============================================================================
# TESTS DE PROYECTO
# =============================================================================

class TestProyecto:
    """Tests para el modelo Proyecto."""

    def test_creacion_proyecto_minimo(self):
        """Test crear proyecto con campos mínimos."""
        # Arrange & Act
        proyecto = Proyecto(nombre="Mi Proyecto")

        # Assert
        assert proyecto.nombre == "Mi Proyecto"
        assert proyecto.id is None
        assert proyecto.estado == EstadoProyecto.ACTIVO
        assert proyecto.descripcion is None
        assert proyecto.usuario_id is None

    def test_creacion_proyecto_completo(self):
        """Test crear proyecto con todos los campos."""
        # Arrange
        ahora = datetime.now()

        # Act
        proyecto = Proyecto(
            id=1,
            nombre="TaskFlow",
            descripcion="Sistema de gestión de tareas",
            usuario_id=1,
            estado=EstadoProyecto.ACTIVO,
            creado_en=ahora,
            actualizado_en=ahora,
        )

        # Assert
        assert proyecto.id == 1
        assert proyecto.descripcion == "Sistema de gestión de tareas"
        assert proyecto.usuario_id == 1

    def test_validacion_nombre_corto(self):
        """Test que nombre corto falla validación."""
        # Arrange
        proyecto = Proyecto(nombre="ab")

        # Act
        errores = proyecto.validar()

        # Assert
        assert len(errores) > 0
        assert any("Nombre debe tener al menos 3 caracteres" in e for e in errores)

    def test_validacion_nombre_vacio(self):
        """Test que nombre vacío falla validación."""
        # Arrange
        proyecto = Proyecto(nombre="")

        # Act
        errores = proyecto.validar()

        # Assert
        assert any("Nombre debe tener al menos 3 caracteres" in e for e in errores)

    def test_validacion_nombre_largo(self):
        """Test que nombre muy largo falla validación."""
        # Arrange
        proyecto = Proyecto(nombre="a" * 101)

        # Act
        errores = proyecto.validar()

        # Assert
        assert any("Nombre no puede exceder 100 caracteres" in e for e in errores)

    def test_validacion_descripcion_larga(self):
        """Test que descripción muy larga falla validación."""
        # Arrange
        proyecto = Proyecto(
            nombre="Proyecto válido",
            descripcion="a" * 1001
        )

        # Act
        errores = proyecto.validar()

        # Assert
        assert any("Descripción no puede exceder 1000 caracteres" in e for e in errores)

    def test_agregar_tarea_composicion(self):
        """Test agregar tarea (composición)."""
        # Arrange
        proyecto = Proyecto(id=1, nombre="Mi Proyecto")
        tarea = Tarea(id=1, titulo="Tarea 1")

        # Act
        resultado = proyecto.agregar_tarea(tarea)

        # Assert
        assert resultado.proyecto_id == proyecto.id
        assert tarea.proyecto_id == 1
        assert resultado is tarea  # Returns the same task

    def test_archivar(self):
        """Test archivar proyecto."""
        # Arrange
        proyecto = Proyecto(
            nombre="Test",
            estado=EstadoProyecto.ACTIVO
        )

        # Act
        proyecto.archivar()

        # Assert
        assert proyecto.estado == EstadoProyecto.ARCHIVADO
        assert proyecto.actualizado_en is not None

    def test_completar(self):
        """Test completar proyecto."""
        # Arrange
        proyecto = Proyecto(
            nombre="Test",
            estado=EstadoProyecto.ACTIVO
        )

        # Act
        proyecto.completar()

        # Assert
        assert proyecto.estado == EstadoProyecto.COMPLETADO
        assert proyecto.actualizado_en is not None

    def test_reactivar(self):
        """Test reactivar proyecto."""
        # Arrange
        proyecto = Proyecto(
            nombre="Test",
            estado=EstadoProyecto.ARCHIVADO
        )

        # Act
        proyecto.reactivar()

        # Assert
        assert proyecto.estado == EstadoProyecto.ACTIVO
        assert proyecto.actualizado_en is not None

    def test_esta_activo_true(self):
        """Test esta_activo retorna True cuando proyecto está activo."""
        # Arrange
        proyecto = Proyecto(
            nombre="Test",
            estado=EstadoProyecto.ACTIVO
        )

        # Act & Assert
        assert proyecto.esta_activo() is True

    def test_esta_activo_false(self):
        """Test esta_activo retorna False cuando proyecto no está activo."""
        # Arrange
        proyecto = Proyecto(
            nombre="Test",
            estado=EstadoProyecto.ARCHIVADO
        )

        # Act & Assert
        assert proyecto.esta_activo() is False

    def test_esta_completado_true(self):
        """Test esta_completado retorna True cuando proyecto está completado."""
        # Arrange
        proyecto = Proyecto(
            nombre="Test",
            estado=EstadoProyecto.COMPLETADO
        )

        # Act & Assert
        assert proyecto.esta_completado() is True

    def test_str_repr(self):
        """Test representaciones string."""
        # Arrange
        proyecto = Proyecto(id=1, nombre="Mi Proyecto", estado=EstadoProyecto.ACTIVO)

        # Act & Assert
        assert str(proyecto) == "Proyecto(Mi Proyecto)"
        assert "Mi Proyecto" in repr(proyecto)
        assert "activo" in repr(proyecto)
        assert "id=1" in repr(proyecto)


# =============================================================================
# TESTS DE TAREA
# =============================================================================

class TestTarea:
    """Tests para el modelo Tarea."""

    def test_creacion_tarea_minimo(self):
        """Test crear tarea con campos mínimos."""
        # Arrange & Act
        tarea = Tarea(titulo="Mi tarea")

        # Assert
        assert tarea.titulo == "Mi tarea"
        assert tarea.estado == EstadoTarea.PENDIENTE
        assert tarea.prioridad == PrioridadTarea.MEDIA
        assert tarea.id is None

    def test_creacion_tarea_completa(self):
        """Test crear tarea con todos los campos."""
        # Arrange
        ahora = datetime.now()
        fecha_limite = date.today() + timedelta(days=7)

        # Act
        tarea = Tarea(
            id=1,
            titulo="Implementar API",
            descripcion="Crear endpoints REST",
            estado=EstadoTarea.EN_PROGRESO,
            prioridad=PrioridadTarea.ALTA,
            proyecto_id=1,
            asignado_a=2,
            creada_por=1,
            fecha_limite=fecha_limite,
            creada_en=ahora,
            actualizada_en=ahora,
        )

        # Assert
        assert tarea.id == 1
        assert tarea.descripcion == "Crear endpoints REST"
        assert tarea.asignado_a == 2
        assert tarea.fecha_limite == fecha_limite

    def test_validacion_titulo_corto(self):
        """Test que título corto falla validación."""
        # Arrange
        tarea = Tarea(titulo="ab")

        # Act
        errores = tarea.validar()

        # Assert
        assert len(errores) > 0
        assert any("Título debe tener al menos 3 caracteres" in e for e in errores)

    def test_validacion_titulo_largo(self):
        """Test que título muy largo falla validación."""
        # Arrange
        tarea = Tarea(titulo="a" * 201)

        # Act
        errores = tarea.validar()

        # Assert
        assert any("Título no puede exceder 200 caracteres" in e for e in errores)

    def test_validacion_descripcion_larga(self):
        """Test que descripción muy larga falla validación."""
        # Arrange
        tarea = Tarea(
            titulo="Tarea válida",
            descripcion="a" * 2001
        )

        # Act
        errores = tarea.validar()

        # Assert
        assert any("Descripción no puede exceder 2000 caracteres" in e for e in errores)

    def test_es_valida_true(self):
        """Test método es_valida retorna True para tarea válida."""
        # Arrange
        tarea = Tarea(titulo="Tarea válida")

        # Act & Assert
        assert tarea.es_valida() is True

    def test_marcar_completada(self):
        """Test marcar tarea como completada."""
        # Arrange
        tarea = Tarea(
            titulo="Test",
            estado=EstadoTarea.PENDIENTE
        )

        # Act
        tarea.completar()

        # Assert
        assert tarea.estado == EstadoTarea.COMPLETADA
        assert tarea.completada_en is not None

    def test_iniciar_desde_pendiente(self):
        """Test iniciar tarea desde estado pendiente."""
        # Arrange
        tarea = Tarea(
            titulo="Test",
            estado=EstadoTarea.PENDIENTE
        )

        # Act
        tarea.iniciar()

        # Assert
        assert tarea.estado == EstadoTarea.EN_PROGRESO

    def test_iniciar_desde_en_progreso(self):
        """Test iniciar tarea que ya está en progreso (no cambia)."""
        # Arrange
        tarea = Tarea(
            titulo="Test",
            estado=EstadoTarea.EN_PROGRESO
        )

        # Act
        tarea.iniciar()

        # Assert
        assert tarea.estado == EstadoTarea.EN_PROGRESO

    def test_cancelar(self):
        """Test cancelar tarea."""
        # Arrange
        tarea = Tarea(
            titulo="Test",
            estado=EstadoTarea.PENDIENTE
        )

        # Act
        tarea.cancelar()

        # Assert
        assert tarea.estado == EstadoTarea.CANCELADA

    def test_esta_pendiente_true(self):
        """Test esta_pendiente retorna True cuando tarea está pendiente."""
        # Arrange
        tarea = Tarea(
            titulo="Test",
            estado=EstadoTarea.PENDIENTE
        )

        # Act & Assert
        assert tarea.esta_pendiente() is True

    def test_esta_en_progreso_true(self):
        """Test esta_en_progreso retorna True cuando tarea está en progreso."""
        # Arrange
        tarea = Tarea(
            titulo="Test",
            estado=EstadoTarea.EN_PROGRESO
        )

        # Act & Assert
        assert tarea.esta_en_progreso() is True

    def test_esta_completada_true(self):
        """Test esta_completada retorna True cuando tarea está completada."""
        # Arrange
        tarea = Tarea(
            titulo="Test",
            estado=EstadoTarea.COMPLETADA
        )

        # Act & Assert
        assert tarea.esta_completada() is True

    def test_esta_vencida_false_sin_fecha(self):
        """Test esta_vencida retorna False cuando no hay fecha límite."""
        # Arrange
        tarea = Tarea(titulo="Test", fecha_limite=None)

        # Act & Assert
        assert tarea.esta_vencida() is False

    def test_esta_vencida_false_fecha_futura(self):
        """Test esta_vencida retorna False cuando fecha límite es futura."""
        # Arrange
        tarea = Tarea(
            titulo="Test",
            fecha_limite=date.today() + timedelta(days=1)
        )

        # Act & Assert
        assert tarea.esta_vencida() is False

    def test_esta_vencida_true_fecha_pasada(self):
        """Test esta_vencida retorna True cuando fecha límite está pasada."""
        # Arrange
        tarea = Tarea(
            titulo="Test",
            fecha_limite=date.today() - timedelta(days=1)
        )

        # Act & Assert
        assert tarea.esta_vencida() is True

    def test_esta_vencida_false_completada(self):
        """Test esta_vencida retorna False para tarea completada aunque la fecha haya pasado."""
        # Arrange
        tarea = Tarea(
            titulo="Test",
            fecha_limite=date.today() - timedelta(days=1),
            estado=EstadoTarea.COMPLETADA
        )

        # Act & Assert
        assert tarea.esta_vencida() is False

    def test_comparacion_prioridad_lt(self):
        """Test comparación menor que (<) por prioridad."""
        # Arrange
        tarea_baja = Tarea(titulo="Baja", prioridad=PrioridadTarea.BAJA)
        tarea_alta = Tarea(titulo="Alta", prioridad=PrioridadTarea.ALTA)

        # Act & Assert
        assert tarea_baja < tarea_alta
        assert not (tarea_alta < tarea_baja)

    def test_comparacion_prioridad_gt(self):
        """Test comparación mayor que (>) por prioridad."""
        # Arrange
        tarea_baja = Tarea(titulo="Baja", prioridad=PrioridadTarea.BAJA)
        tarea_urgente = Tarea(titulo="Urgente", prioridad=PrioridadTarea.URGENTE)

        # Act & Assert
        assert tarea_urgente > tarea_baja
        assert not (tarea_baja > tarea_urgente)

    def test_comparacion_prioridad_orden_completo(self):
        """Test orden completo de prioridades."""
        # Arrange
        tarea_baja = Tarea(titulo="Baja", prioridad=PrioridadTarea.BAJA)
        tarea_media = Tarea(titulo="Media", prioridad=PrioridadTarea.MEDIA)
        tarea_alta = Tarea(titulo="Alta", prioridad=PrioridadTarea.ALTA)
        tarea_urgente = Tarea(titulo="Urgente", prioridad=PrioridadTarea.URGENTE)

        # Act & Assert - URGENTE > ALTA > MEDIA > BAJA
        assert tarea_baja < tarea_media
        assert tarea_media < tarea_alta
        assert tarea_alta < tarea_urgente
        assert tarea_urgente > tarea_alta
        assert tarea_alta > tarea_media
        assert tarea_media > tarea_baja

    def test_comparacion_prioridad_eq(self):
        """Test comparación de igualdad por prioridad."""
        # Arrange
        tarea1 = Tarea(titulo="Tarea 1", prioridad=PrioridadTarea.ALTA)
        tarea2 = Tarea(titulo="Tarea 2", prioridad=PrioridadTarea.ALTA)

        # Act & Assert
        assert tarea1 == tarea2  # Same priority

    def test_comparacion_prioridad_ne(self):
        """Test comparación de desigualdad por prioridad."""
        # Arrange
        tarea1 = Tarea(titulo="Tarea 1", prioridad=PrioridadTarea.ALTA)
        tarea2 = Tarea(titulo="Tarea 2", prioridad=PrioridadTarea.BAJA)

        # Act & Assert
        assert tarea1 != tarea2  # Different priority

    def test_str_repr(self):
        """Test representaciones string."""
        # Arrange
        tarea = Tarea(
            id=1,
            titulo="Implementar API",
            estado=EstadoTarea.PENDIENTE
        )

        # Act & Assert
        assert str(tarea) == "Tarea(Implementar API)"
        assert "Implementar API" in repr(tarea)
        assert "pendiente" in repr(tarea)
        assert "id=1" in repr(tarea)


# =============================================================================
# TESTS DE COMENTARIO
# =============================================================================

class TestComentario:
    """Tests para el modelo Comentario."""

    def test_creacion_comentario_minimo(self):
        """Test crear comentario con campos mínimos."""
        # Arrange & Act
        comentario = Comentario(contenido="Este es un comentario")

        # Assert
        assert comentario.contenido == "Este es un comentario"
        assert comentario.id is None
        assert comentario.tarea_id is None
        assert comentario.usuario_id is None

    def test_creacion_comentario_completo(self):
        """Test crear comentario con todos los campos."""
        # Arrange
        ahora = datetime.now()

        # Act
        comentario = Comentario(
            id=1,
            contenido="Por favor revisar",
            tarea_id=1,
            usuario_id=1,
            creado_en=ahora,
        )

        # Assert
        assert comentario.id == 1
        assert comentario.tarea_id == 1
        assert comentario.usuario_id == 1
        assert comentario.creado_en == ahora

    def test_validacion_contenido_vacio(self):
        """Test que contenido vacío falla validación."""
        # Arrange
        comentario = Comentario(contenido="   ")

        # Act
        errores = comentario.validar()

        # Assert
        assert len(errores) > 0
        assert any("Contenido no puede estar vacío" in e for e in errores)

    def test_validacion_contenido_largo(self):
        """Test que contenido muy largo falla validación."""
        # Arrange
        comentario = Comentario(contenido="a" * 2001)

        # Act
        errores = comentario.validar()

        # Assert
        assert any("Contenido no puede exceder 2000 caracteres" in e for e in errores)

    def test_es_valido_true(self):
        """Test método es_valido retorna True para comentario válido."""
        # Arrange
        comentario = Comentario(contenido="Comentario válido")

        # Act & Assert
        assert comentario.es_valido() is True

    def test_es_valido_false(self):
        """Test método es_valido retorna False para comentario inválido."""
        # Arrange
        comentario = Comentario(contenido="   ")

        # Act & Assert
        assert comentario.es_valido() is False

    def test_contenido_corto_corto(self):
        """Test propiedad contenido_corto retorna contenido sin modificar si es corto."""
        # Arrange
        comentario = Comentario(contenido="Texto corto")

        # Act
        resultado = comentario.contenido_corto

        # Assert
        assert resultado == "Texto corto"
        assert "..." not in resultado

    def test_contenido_corto_largo(self):
        """Test propiedad contenido_corto trunca contenido largo."""
        # Arrange
        comentario = Comentario(
            contenido="Este es un comentario muy largo que supera los 30 caracteres"
        )

        # Act
        resultado = comentario.contenido_corto

        # Assert
        assert len(resultado) <= 33  # 30 + "..."
        assert resultado.endswith("...")
        assert resultado == "Este es un comentario muy larg..."

    def test_contenido_corto_exactamente_30(self):
        """Test propiedad contenido_corto con contenido exactamente de 30 caracteres."""
        # Arrange
        comentario = Comentario(contenido="a" * 30)

        # Act
        resultado = comentario.contenido_corto

        # Assert
        assert len(resultado) == 30
        assert "..." not in resultado

    def test_editar(self):
        """Test editar comentario."""
        # Arrange
        comentario = Comentario(contenido="Original")

        # Act
        comentario.editar("Nuevo contenido")

        # Assert
        assert comentario.contenido == "Nuevo contenido"

    def test_editar_vacio_raise_error(self):
        """Test editar con contenido vacío raises ValueError."""
        # Arrange
        comentario = Comentario(contenido="Original")

        # Act & Assert
        with pytest.raises(ValueError, match="Contenido no puede estar vacío"):
            comentario.editar("")

    def test_editar_espacios_raise_error(self):
        """Test editar con solo espacios raises ValueError."""
        # Arrange
        comentario = Comentario(contenido="Original")

        # Act & Assert
        with pytest.raises(ValueError, match="Contenido no puede estar vacío"):
            comentario.editar("   ")

    def test_len(self):
        """Test __len__ retorna longitud del contenido."""
        # Arrange
        comentario = Comentario(contenido="Test")

        # Act & Assert
        assert len(comentario) == 4

    def test_len_vacio(self):
        """Test __len__ con contenido vacío."""
        # Arrange
        comentario = Comentario(contenido="")

        # Act & Assert
        assert len(comentario) == 0

    def test_str_repr(self):
        """Test representaciones string."""
        # Arrange
        comentario = Comentario(
            id=1,
            contenido="Este es un comentario",
            tarea_id=1,
            usuario_id=1
        )

        # Act & Assert
        assert "Este es un comentario" in str(comentario)
        assert "Comentario(" in str(comentario)
        assert "id=1" in repr(comentario)
        assert "tarea_id=1" in repr(comentario)
        assert "usuario_id=1" in repr(comentario)


# =============================================================================
# TESTS DE DTOs
# =============================================================================

class TestDTOs:
    """Tests para los DTOs de Usuario."""

    def test_usuario_creacion_minimo(self):
        """Test DTO UsuarioCreacion con campos mínimos."""
        # Arrange & Act
        dto = UsuarioCreacion(
            username="jdoe",
            email="john@example.com",
            password="secret123"
        )

        # Assert
        assert dto.username == "jdoe"
        assert dto.email == "john@example.com"
        assert dto.password == "secret123"
        assert dto.nombre_completo is None

    def test_usuario_creacion_completo(self):
        """Test DTO UsuarioCreacion con todos los campos."""
        # Arrange & Act
        dto = UsuarioCreacion(
            username="jdoe",
            email="john@example.com",
            password="secret123",
            nombre_completo="John Doe"
        )

        # Assert
        assert dto.nombre_completo == "John Doe"

    def test_usuario_respuesta(self):
        """Test DTO UsuarioRespuesta."""
        # Arrange
        ahora = datetime.now()

        # Act
        dto = UsuarioRespuesta(
            id=1,
            username="jdoe",
            email="john@example.com",
            nombre_completo="John Doe",
            activo=True,
            creado_en=ahora
        )

        # Assert
        assert dto.id == 1
        assert dto.activo is True
        assert dto.creado_en == ahora


# =============================================================================
# TESTS DE INTEGRACIÓN ENTRE MODELOS
# =============================================================================

class TestIntegracionModelos:
    """Tests de integración entre modelos."""

    def test_proyecto_con_tareas_composicion(self):
        """Test composición Proyecto -> Tarea."""
        # Arrange
        proyecto = Proyecto(id=1, nombre="Mi Proyecto")
        tarea1 = Tarea(titulo="Tarea 1")
        tarea2 = Tarea(titulo="Tarea 2")

        # Act
        proyecto.agregar_tarea(tarea1)
        proyecto.agregar_tarea(tarea2)

        # Assert
        assert tarea1.proyecto_id == 1
        assert tarea2.proyecto_id == 1

    def test_ordenar_tareas_por_prioridad(self):
        """Test ordenar tareas por prioridad usando operadores de comparación."""
        # Arrange
        tareas = [
            Tarea(titulo="Media", prioridad=PrioridadTarea.MEDIA),
            Tarea(titulo="Urgente", prioridad=PrioridadTarea.URGENTE),
            Tarea(titulo="Baja", prioridad=PrioridadTarea.BAJA),
            Tarea(titulo="Alta", prioridad=PrioridadTarea.ALTA),
        ]

        # Act
        tareas_ordenadas = sorted(tareas)

        # Assert
        assert tareas_ordenadas[0].prioridad == PrioridadTarea.BAJA
        assert tareas_ordenadas[1].prioridad == PrioridadTarea.MEDIA
        assert tareas_ordenadas[2].prioridad == PrioridadTarea.ALTA
        assert tareas_ordenadas[3].prioridad == PrioridadTarea.URGENTE

    def test_comentario_con_referencias(self):
        """Test comentario con referencias a tarea y usuario."""
        # Arrange
        usuario = Usuario(id=1, username="jdoe", email="john@example.com")
        proyecto = Proyecto(id=1, nombre="Mi Proyecto")
        tarea = Tarea(id=1, titulo="Tarea 1", proyecto_id=1)

        comentario = Comentario(
            id=1,
            contenido="Por favor revisar",
            tarea_id=tarea.id,
            usuario_id=usuario.id
        )

        # Assert
        assert comentario.tarea_id == tarea.id
        assert comentario.usuario_id == usuario.id
