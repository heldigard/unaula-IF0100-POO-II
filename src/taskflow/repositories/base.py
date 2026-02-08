"""
Repository base - TaskFlow
Unidad: 1.5 - Interfaces y ABCs
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")


class Repository(Generic[T], ABC):
    """
    Repository base genérico usando ABC.

    Esta clase abstracta define la interfaz común para todos los repositorios
    del sistema, implementando el patrón Repository de Domain-Driven Design.

    Type Parameters:
        T: Tipo de entidad que maneja el repositorio

    Example:
        >>> class UsuarioRepository(Repository[Usuario]):
        ...     def create(self, entity: Usuario) -> Usuario:
        ...         # implementación
        ...         pass
    """

    @abstractmethod
    def create(self, entity: T) -> T:
        """
        Crea una nueva entidad.

        Args:
            entity: Entidad a crear

        Returns:
            Entidad creada con ID asignado

        Raises:
            ValueError: Si la entidad es inválida
        """
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        """
        Obtiene una entidad por su ID.

        Args:
            id: Identificador de la entidad

        Returns:
            Entidad encontrada o None si no existe
        """
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """
        Obtiene todas las entidades.

        Returns:
            Lista de todas las entidades
        """
        pass

    @abstractmethod
    def update(self, entity: T) -> Optional[T]:
        """
        Actualiza una entidad existente.

        Args:
            entity: Entidad con los datos actualizados

        Returns:
            Entidad actualizada o None si no existe

        Raises:
            ValueError: Si la entidad es inválida o no tiene ID
        """
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        """
        Elimina una entidad por su ID.

        Args:
            id: Identificador de la entidad a eliminar

        Returns:
            True si se eliminó, False si no existe
        """
        pass

    @abstractmethod
    def count(self) -> int:
        """
        Cuenta el total de entidades.

        Returns:
            Número total de entidades
        """
        pass

    @abstractmethod
    def exists(self, id: int) -> bool:
        """
        Verifica si existe una entidad por su ID.

        Args:
            id: Identificador de la entidad

        Returns:
            True si existe, False en caso contrario
        """
        pass
