"""
Repository de Proyecto - TaskFlow
Unidad: 2.6 - DDD: Repositorios
"""

from typing import Optional, List
from datetime import datetime

from .base import Repository
from ..models import Proyecto, EstadoProyecto


class ProyectoRepository(Repository[Proyecto]):
    """
    Repository para la entidad Proyecto.

    Implementa un repositorio en memoria para gestión de proyectos.
    En producción, esto se reemplazaría con una implementación de base de datos.

    Attributes:
        _proyectos: Diccionario interno de proyectos (id -> proyecto)
        _next_id: Contador para generar IDs auto-incrementales

    Example:
        >>> repo = ProyectoRepository()
        >>> proyecto = Proyecto(nombre="TaskFlow", usuario_id=1)
        >>> creado = repo.create(proyecto)
        >>> assert creado.id == 1
    """

    def __init__(self) -> None:
        """Inicializa el repositorio con almacenamiento en memoria."""
        self._proyectos: dict[int, Proyecto] = {}
        self._next_id: int = 1

    def create(self, entity: Proyecto) -> Proyecto:
        """
        Crea un nuevo proyecto.

        Args:
            entity: Proyecto a crear

        Returns:
            Proyecto creado con ID asignado
        """
        entity.id = self._next_id
        entity.creado_en = datetime.now()
        entity.actualizado_en = datetime.now()

        self._proyectos[entity.id] = entity
        self._next_id += 1

        return entity

    def get_by_id(self, id: int) -> Optional[Proyecto]:
        """
        Obtiene un proyecto por su ID.

        Args:
            id: ID del proyecto

        Returns:
            Proyecto encontrado o None
        """
        return self._proyectos.get(id)

    def get_all(self) -> List[Proyecto]:
        """
        Obtiene todos los proyectos.

        Returns:
            Lista de todos los proyectos
        """
        return list(self._proyectos.values())

    def update(self, entity: Proyecto) -> Optional[Proyecto]:
        """
        Actualiza un proyecto existente.

        Args:
            entity: Proyecto con datos actualizados

        Returns:
            Proyecto actualizado o None si no existe
        """
        if entity.id is None or entity.id not in self._proyectos:
            return None

        entity.actualizado_en = datetime.now()
        self._proyectos[entity.id] = entity
        return entity

    def delete(self, id: int) -> bool:
        """
        Elimina un proyecto por ID.

        Args:
            id: ID del proyecto a eliminar

        Returns:
            True si se eliminó, False si no existe
        """
        if id in self._proyectos:
            del self._proyectos[id]
            return True
        return False

    def count(self) -> int:
        """
        Cuenta el total de proyectos.

        Returns:
            Número total de proyectos
        """
        return len(self._proyectos)

    def exists(self, id: int) -> bool:
        """
        Verifica si existe un proyecto por ID.

        Args:
            id: ID del proyecto

        Returns:
            True si existe, False en caso contrario
        """
        return id in self._proyectos

    def get_by_usuario(self, usuario_id: int) -> List[Proyecto]:
        """
        Obtiene todos los proyectos de un usuario.

        Args:
            usuario_id: ID del usuario propietario

        Returns:
            Lista de proyectos del usuario
        """
        return [
            p for p in self._proyectos.values()
            if p.usuario_id == usuario_id
        ]

    def get_by_estado(self, estado: EstadoProyecto) -> List[Proyecto]:
        """
        Obtiene proyectos por estado.

        Args:
            estado: Estado a filtrar

        Returns:
            Lista de proyectos con el estado dado
        """
        return [
            p for p in self._proyectos.values()
            if p.estado == estado
        ]

    def get_activos(self) -> List[Proyecto]:
        """
        Obtiene todos los proyectos activos.

        Returns:
            Lista de proyectos con estado=activo
        """
        return self.get_by_estado(EstadoProyecto.ACTIVO)

    def get_archivados(self) -> List[Proyecto]:
        """
        Obtiene todos los proyectos archivados.

        Returns:
            Lista de proyectos con estado=archivado
        """
        return self.get_by_estado(EstadoProyecto.ARCHIVADO)

    def get_completados(self) -> List[Proyecto]:
        """
        Obtiene todos los proyectos completados.

        Returns:
            Lista de proyectos con estado=completado
        """
        return self.get_by_estado(EstadoProyecto.COMPLETADO)

    def get_by_usuario_y_estado(
        self, usuario_id: int, estado: EstadoProyecto
    ) -> List[Proyecto]:
        """
        Obtiene proyectos de un usuario filtrados por estado.

        Args:
            usuario_id: ID del usuario propietario
            estado: Estado a filtrar

        Returns:
            Lista de proyectos que cumplen ambos criterios
        """
        return [
            p for p in self._proyectos.values()
            if p.usuario_id == usuario_id and p.estado == estado
        ]
