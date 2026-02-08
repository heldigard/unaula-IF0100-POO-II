"""
Repository de Tarea - TaskFlow
Unidad: 2.6 - DDD: Repositorios
"""

from typing import Optional, List
from datetime import datetime, date

from .base import Repository
from ..models import Tarea, EstadoTarea, PrioridadTarea


class TareaRepository(Repository[Tarea]):
    """
    Repository para la entidad Tarea.

    Implementa un repositorio en memoria para gestión de tareas.
    En producción, esto se reemplazaría con una implementación de base de datos.

    Attributes:
        _tareas: Diccionario interno de tareas (id -> tarea)
        _next_id: Contador para generar IDs auto-incrementales

    Example:
        >>> repo = TareaRepository()
        >>> tarea = Tarea(titulo="Implementar API", proyecto_id=1, creada_por=1)
        >>> creada = repo.create(tarea)
        >>> assert creada.id == 1
    """

    def __init__(self) -> None:
        """Inicializa el repositorio con almacenamiento en memoria."""
        self._tareas: dict[int, Tarea] = {}
        self._next_id: int = 1

    def create(self, entity: Tarea) -> Tarea:
        """
        Crea una nueva tarea.

        Args:
            entity: Tarea a crear

        Returns:
            Tarea creada con ID asignado
        """
        entity.id = self._next_id
        entity.creada_en = datetime.now()
        entity.actualizada_en = datetime.now()

        self._tareas[entity.id] = entity
        self._next_id += 1

        return entity

    def get_by_id(self, id: int) -> Optional[Tarea]:
        """
        Obtiene una tarea por su ID.

        Args:
            id: ID de la tarea

        Returns:
            Tarea encontrada o None
        """
        return self._tareas.get(id)

    def get_all(self) -> List[Tarea]:
        """
        Obtiene todas las tareas.

        Returns:
            Lista de todas las tareas
        """
        return list(self._tareas.values())

    def update(self, entity: Tarea) -> Optional[Tarea]:
        """
        Actualiza una tarea existente.

        Args:
            entity: Tarea con datos actualizados

        Returns:
            Tarea actualizada o None si no existe
        """
        if entity.id is None or entity.id not in self._tareas:
            return None

        entity.actualizada_en = datetime.now()
        self._tareas[entity.id] = entity
        return entity

    def delete(self, id: int) -> bool:
        """
        Elimina una tarea por ID.

        Args:
            id: ID de la tarea a eliminar

        Returns:
            True si se eliminó, False si no existe
        """
        if id in self._tareas:
            del self._tareas[id]
            return True
        return False

    def count(self) -> int:
        """
        Cuenta el total de tareas.

        Returns:
            Número total de tareas
        """
        return len(self._tareas)

    def exists(self, id: int) -> bool:
        """
        Verifica si existe una tarea por ID.

        Args:
            id: ID de la tarea

        Returns:
            True si existe, False en caso contrario
        """
        return id in self._tareas

    def get_by_proyecto(self, proyecto_id: int) -> List[Tarea]:
        """
        Obtiene todas las tareas de un proyecto.

        Args:
            proyecto_id: ID del proyecto

        Returns:
            Lista de tareas del proyecto
        """
        return [
            t for t in self._tareas.values()
            if t.proyecto_id == proyecto_id
        ]

    def get_by_asignado(self, usuario_id: int) -> List[Tarea]:
        """
        Obtiene todas las tareas asignadas a un usuario.

        Args:
            usuario_id: ID del usuario asignado

        Returns:
            Lista de tareas asignadas
        """
        return [
            t for t in self._tareas.values()
            if t.asignado_a == usuario_id
        ]

    def get_by_creador(self, usuario_id: int) -> List[Tarea]:
        """
        Obtiene todas las tareas creadas por un usuario.

        Args:
            usuario_id: ID del usuario creador

        Returns:
            Lista de tareas creadas
        """
        return [
            t for t in self._tareas.values()
            if t.creada_por == usuario_id
        ]

    def get_by_estado(self, estado: EstadoTarea) -> List[Tarea]:
        """
        Obtiene tareas por estado.

        Args:
            estado: Estado a filtrar

        Returns:
            Lista de tareas con el estado dado
        """
        return [
            t for t in self._tareas.values()
            if t.estado == estado
        ]

    def get_by_prioridad(self, prioridad: PrioridadTarea) -> List[Tarea]:
        """
        Obtiene tareas por prioridad.

        Args:
            prioridad: Prioridad a filtrar

        Returns:
            Lista de tareas con la prioridad dada
        """
        return [
            t for t in self._tareas.values()
            if t.prioridad == prioridad
        ]

    def get_pendientes(self) -> List[Tarea]:
        """Obtiene todas las tareas pendientes."""
        return self.get_by_estado(EstadoTarea.PENDIENTE)

    def get_en_progreso(self) -> List[Tarea]:
        """Obtiene todas las tareas en progreso."""
        return self.get_by_estado(EstadoTarea.EN_PROGRESO)

    def get_completadas(self) -> List[Tarea]:
        """Obtiene todas las tareas completadas."""
        return self.get_by_estado(EstadoTarea.COMPLETADA)

    def get_vencidas(self) -> List[Tarea]:
        """
        Obtiene todas las tareas vencidas.

        Returns:
            Lista de tareas con fecha límite pasada y no completadas
        """
        hoy = date.today()
        return [
            t for t in self._tareas.values()
            if t.fecha_limite and t.fecha_limite < hoy and t.estado != EstadoTarea.COMPLETADA
        ]

    def get_por_vencer(self, dias: int = 3) -> List[Tarea]:
        """
        Obtiene tareas que vencerán pronto.

        Args:
            dias: Días de margen (default: 3)

        Returns:
            Lista de tareas próximas a vencer y no completadas
        """
        from datetime import timedelta

        limite = date.today() + timedelta(days=dias)
        return [
            t for t in self._tareas.values()
            if t.fecha_limite and t.fecha_limite <= limite
            and t.estado != EstadoTarea.COMPLETADA
        ]

    def get_by_proyecto_y_estado(
        self, proyecto_id: int, estado: EstadoTarea
    ) -> List[Tarea]:
        """
        Obtiene tareas de un proyecto filtradas por estado.

        Args:
            proyecto_id: ID del proyecto
            estado: Estado a filtrar

        Returns:
            Lista de tareas que cumplen ambos criterios
        """
        return [
            t for t in self._tareas.values()
            if t.proyecto_id == proyecto_id and t.estado == estado
        ]
