"""
Repository de Usuario - TaskFlow
Unidad: 2.6 - DDD: Repositorios
"""

from typing import Optional, List
from datetime import datetime

from .base import Repository
from ..models import Usuario


class UsuarioRepository(Repository[Usuario]):
    """
    Repository para la entidad Usuario.

    Implementa un repositorio en memoria para gestión de usuarios.
    En producción, esto se reemplazaría con una implementación de base de datos.

    Attributes:
        _usuarios: Diccionario interno de usuarios (id -> usuario)
        _next_id: Contador para generar IDs auto-incrementales

    Example:
        >>> repo = UsuarioRepository()
        >>> usuario = Usuario(username="jdoe", email="john@example.com")
        >>> creado = repo.create(usuario)
        >>> assert creado.id == 1
    """

    def __init__(self) -> None:
        """Inicializa el repositorio con almacenamiento en memoria."""
        self._usuarios: dict[int, Usuario] = {}
        self._next_id: int = 1

    def create(self, entity: Usuario) -> Usuario:
        """
        Crea un nuevo usuario.

        Args:
            entity: Usuario a crear

        Returns:
            Usuario creado con ID asignado

        Raises:
            ValueError: Si el username o email ya existen
        """
        # Verificar username único
        if self._get_by_username(entity.username):
            raise ValueError(f"Username '{entity.username}' ya existe")

        # Verificar email único
        if self._get_by_email(entity.email):
            raise ValueError(f"Email '{entity.email}' ya existe")

        # Asignar ID y timestamps
        entity.id = self._next_id
        entity.creado_en = datetime.now()
        entity.actualizado_en = datetime.now()

        # Guardar
        self._usuarios[entity.id] = entity
        self._next_id += 1

        return entity

    def get_by_id(self, id: int) -> Optional[Usuario]:
        """
        Obtiene un usuario por su ID.

        Args:
            id: ID del usuario

        Returns:
            Usuario encontrado o None
        """
        return self._usuarios.get(id)

    def get_all(self) -> List[Usuario]:
        """
        Obtiene todos los usuarios.

        Returns:
            Lista de todos los usuarios
        """
        return list(self._usuarios.values())

    def update(self, entity: Usuario) -> Optional[Usuario]:
        """
        Actualiza un usuario existente.

        Args:
            entity: Usuario con datos actualizados

        Returns:
            Usuario actualizado o None si no existe

        Raises:
            ValueError: Si el username/email ya existen en otro usuario
        """
        if entity.id is None or entity.id not in self._usuarios:
            return None

        # Verificar username único (excluyendo al propio usuario)
        existing = self._get_by_username(entity.username)
        if existing and existing.id != entity.id:
            raise ValueError(f"Username '{entity.username}' ya existe")

        # Verificar email único (excluyendo al propio usuario)
        existing = self._get_by_email(entity.email)
        if existing and existing.id != entity.id:
            raise ValueError(f"Email '{entity.email}' ya existe")

        # Actualizar timestamp
        entity.actualizado_en = datetime.now()

        self._usuarios[entity.id] = entity
        return entity

    def delete(self, id: int) -> bool:
        """
        Elimina un usuario por ID.

        Args:
            id: ID del usuario a eliminar

        Returns:
            True si se eliminó, False si no existe
        """
        if id in self._usuarios:
            del self._usuarios[id]
            return True
        return False

    def count(self) -> int:
        """
        Cuenta el total de usuarios.

        Returns:
            Número total de usuarios
        """
        return len(self._usuarios)

    def exists(self, id: int) -> bool:
        """
        Verifica si existe un usuario por ID.

        Args:
            id: ID del usuario

        Returns:
            True si existe, False en caso contrario
        """
        return id in self._usuarios

    def get_by_username(self, username: str) -> Optional[Usuario]:
        """
        Obtiene un usuario por username.

        Args:
            username: Nombre de usuario único

        Returns:
            Usuario encontrado o None
        """
        return self._get_by_username(username)

    def get_by_email(self, email: str) -> Optional[Usuario]:
        """
        Obtiene un usuario por email.

        Args:
            email: Correo electrónico único

        Returns:
            Usuario encontrado o None
        """
        return self._get_by_email(email)

    def get_activos(self) -> List[Usuario]:
        """
        Obtiene todos los usuarios activos.

        Returns:
            Lista de usuarios con estado=activo
        """
        from ..models import EstadoUsuario
        return [u for u in self._usuarios.values() if u.esta_activo()]

    # Métodos privados

    def _get_by_username(self, username: str) -> Optional[Usuario]:
        """Búsqueda interna por username."""
        for usuario in self._usuarios.values():
            if usuario.username == username:
                return usuario
        return None

    def _get_by_email(self, email: str) -> Optional[Usuario]:
        """Búsqueda interna por email."""
        for usuario in self._usuarios.values():
            if usuario.email == email:
                return usuario
        return None
