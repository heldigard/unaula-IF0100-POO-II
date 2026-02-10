"""
Repository de Comentario - TaskFlow
Unidad: 2.6 - DDD: Repositorios
"""

from typing import Optional, List
from datetime import datetime

from .base import Repository
from ..models import Comentario


class ComentarioRepository(Repository[Comentario]):
    """
    Repository para la entidad Comentario.

    Implementa un repositorio en memoria para gestión de comentarios.
    En producción, esto se reemplazaría con una implementación de base de datos.

    Attributes:
        _comentarios: Diccionario interno de comentarios (id -> comentario)
        _next_id: Contador para generar IDs auto-incrementales

    Example:
        >>> repo = ComentarioRepository()
        >>> comentario = Comentario(contenido="Por favor revisar", tarea_id=1, usuario_id=1)
        >>> creado = repo.create(comentario)
        >>> assert creado.id == 1
    """

    def __init__(self) -> None:
        """Inicializa el repositorio con almacenamiento en memoria."""
        self._comentarios: dict[int, Comentario] = {}
        self._next_id: int = 1

    def create(self, entity: Comentario) -> Comentario:
        """
        Crea un nuevo comentario.

        Args:
            entity: Comentario a crear

        Returns:
            Comentario creado con ID asignado
        """
        entity.id = self._next_id
        entity.creado_en = datetime.now()

        self._comentarios[entity.id] = entity
        self._next_id += 1

        return entity

    def get_by_id(self, id: int) -> Optional[Comentario]:
        """
        Obtiene un comentario por su ID.

        Args:
            id: ID del comentario

        Returns:
            Comentario encontrado o None
        """
        return self._comentarios.get(id)

    def get_all(self) -> List[Comentario]:
        """
        Obtiene todos los comentarios.

        Returns:
            Lista de todos los comentarios
        """
        return list(self._comentarios.values())

    def update(self, entity: Comentario) -> Optional[Comentario]:
        """
        Actualiza un comentario existente.

        Note:
            Los comentarios normalmente no se editan, pero el método
            existe por consistencia con la interfaz Repository.

        Args:
            entity: Comentario con datos actualizados

        Returns:
            Comentario actualizado o None si no existe
        """
        if entity.id is None or entity.id not in self._comentarios:
            return None

        self._comentarios[entity.id] = entity
        return entity

    def delete(self, id: int) -> bool:
        """
        Elimina un comentario por ID.

        Args:
            id: ID del comentario a eliminar

        Returns:
            True si se eliminó, False si no existe
        """
        if id in self._comentarios:
            del self._comentarios[id]
            return True
        return False

    def count(self) -> int:
        """
        Cuenta el total de comentarios.

        Returns:
            Número total de comentarios
        """
        return len(self._comentarios)

    def exists(self, id: int) -> bool:
        """
        Verifica si existe un comentario por ID.

        Args:
            id: ID del comentario

        Returns:
            True si existe, False en caso contrario
        """
        return id in self._comentarios

    def get_by_tarea(self, tarea_id: int) -> List[Comentario]:
        """
        Obtiene todos los comentarios de una tarea.

        Args:
            tarea_id: ID de la tarea

        Returns:
            Lista de comentarios de la tarea ordenados por fecha (antiguos primero)
        """
        comentarios = [
            c for c in self._comentarios.values()
            if c.tarea_id == tarea_id
        ]
        # Ordenar por fecha de creación (antiguos primero)
        comentarios.sort(key=lambda c: c.creado_en or datetime.min)
        return comentarios

    def get_by_usuario(self, usuario_id: int) -> List[Comentario]:
        """
        Obtiene todos los comentarios de un usuario.

        Args:
            usuario_id: ID del usuario

        Returns:
            Lista de comentarios del usuario
        """
        return [
            c for c in self._comentarios.values()
            if c.usuario_id == usuario_id
        ]

    def count_by_tarea(self, tarea_id: int) -> int:
        """
        Cuenta los comentarios de una tarea.

        Args:
            tarea_id: ID de la tarea

        Returns:
            Número de comentarios de la tarea
        """
        return len(self.get_by_tarea(tarea_id))

    def delete_by_tarea(self, tarea_id: int) -> int:
        """
        Elimina todos los comentarios de una tarea.

        Útil cuando se elimina una tarea en cascada.

        Args:
            tarea_id: ID de la tarea

        Returns:
            Número de comentarios eliminados
        """
        ids_a_eliminar = [
            c.id for c in self._comentarios.values()
            if c.tarea_id == tarea_id and c.id is not None
        ]
        for id in ids_a_eliminar:
            del self._comentarios[id]
        return len(ids_a_eliminar)
