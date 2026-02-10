"""
Service de Usuario - TaskFlow
Unidad: 2.6 - DDD: Servicios

Este módulo implementa la lógica de negocio relacionada con los usuarios,
actuando como una capa de coordinación entre los modelos y repositorios.
"""

from typing import Optional, List
from datetime import datetime
import bcrypt

from ..models import Usuario, EstadoUsuario
from ..repositories import UsuarioRepository
from ..schemas import UsuarioCreate, UsuarioUpdate


class UsuarioService:
    """
    Service con lógica de negocio de usuarios.

    Este service encapsula las reglas de negocio relacionadas con usuarios,
    como autenticación, validaciones de unicidad, y gestión de passwords.

    Attributes:
        repo: Instancia de UsuarioRepository para acceso a datos

    Example:
        >>> repo = UsuarioRepository()
        >>> service = UsuarioService(repo)
        >>> data = UsuarioCreate(username="jdoe", email="john@example.com", password="pass123")
        >>> usuario = service.crear_usuario(data)
    """

    def __init__(self, repo: UsuarioRepository) -> None:
        """
        Inicializa el service con un repositorio inyectado.

        Args:
            repo: Repositorio de usuarios a utilizar
        """
        self.repo = repo

    def crear_usuario(self, data: UsuarioCreate) -> Usuario:
        """
        Crea un nuevo usuario con validaciones de negocio.

        Valida que el username y email sean únicos antes de crear el usuario.
        También hashea el password utilizando bcrypt.

        Args:
            data: DTO con los datos del usuario a crear

        Returns:
            Usuario creado con ID asignado

        Raises:
            ValueError: Si el username o email ya existen
            ValueError: Si el usuario no pasa las validaciones del modelo

        Example:
            >>> data = UsuarioCreate(
            ...     username="jdoe",
            ...     email="john@example.com",
            ...     password="securepass123",
            ...     nombre_completo="John Doe"
            ... )
            >>> usuario = service.crear_usuario(data)
            >>> assert usuario.id is not None
        """
        # Validar username único
        if self.repo.get_by_username(data.username):
            raise ValueError(f"Username '{data.username}' ya existe")

        # Validar email único
        if self.repo.get_by_email(data.email):
            raise ValueError(f"Email '{data.email}' ya está registrado")

        # Hash password
        password_hash = self._hash_password(data.password)

        # Crear usuario
        usuario = Usuario(
            username=data.username,
            email=data.email,
            password_hash=password_hash,
            nombre_completo=data.nombre_completo,
            estado=EstadoUsuario.ACTIVO,
            creado_en=datetime.now(),
        )

        # Validar modelo
        errores = usuario.validar()
        if errores:
            raise ValueError(f"Usuario inválido: {', '.join(errores)}")

        return self.repo.create(usuario)

    def autenticar(self, username: str, password: str) -> Usuario:
        """
        Autentica un usuario por username/password.

        Verifica las credenciales del usuario y que esté en estado activo.

        Args:
            username: Nombre de usuario
            password: Password en texto plano

        Returns:
            Usuario autenticado

        Raises:
            ValueError: Si las credenciales son inválidas
            ValueError: Si el usuario no está activo

        Example:
            >>> usuario = service.autenticar("jdoe", "mipassword123")
            >>> assert usuario.esta_activo()
        """
        usuario = self.repo.get_by_username(username)
        if not usuario:
            raise ValueError("Credenciales inválidas")

        if not self._verify_password(password, usuario.password_hash):
            raise ValueError("Credenciales inválidas")

        if not usuario.esta_activo():
            raise ValueError("Usuario inactivo o suspendido")

        return usuario

    def obtener_usuario(self, id: int) -> Usuario:
        """
        Obtiene un usuario por ID.

        Args:
            id: ID del usuario

        Returns:
            Usuario encontrado

        Raises:
            ValueError: Si el usuario no existe

        Example:
            >>> usuario = service.obtener_usuario(1)
            >>> print(usuario.username)
        """
        usuario = self.repo.get_by_id(id)
        if not usuario:
            raise ValueError(f"Usuario con ID {id} no encontrado")
        return usuario

    def actualizar_usuario(self, id: int, data: UsuarioUpdate) -> Usuario:
        """
        Actualiza un usuario.

        Permite actualizar el nombre completo y el estado del usuario.

        Args:
            id: ID del usuario a actualizar
            data: DTO con los datos a actualizar

        Returns:
            Usuario actualizado

        Raises:
            ValueError: Si el usuario no existe

        Example:
            >>> data = UsuarioUpdate(
            ...     nombre_completo="John Updated Doe",
            ...     estado=EstadoUsuario.ACTIVO
            ... )
            >>> usuario = service.actualizar_usuario(1, data)
        """
        usuario = self.obtener_usuario(id)

        if data.nombre_completo is not None:
            usuario.nombre_completo = data.nombre_completo

        if data.estado is not None:
            usuario.estado = data.estado

        usuario.actualizado_en = datetime.now()

        return self.repo.update(usuario)

    def cambiar_password(
        self, id: int, password_actual: str, password_nuevo: str
    ) -> None:
        """
        Cambia el password de un usuario.

        Valida el password actual antes de cambiarlo por el nuevo.

        Args:
            id: ID del usuario
            password_actual: Password actual para verificar
            password_nuevo: Nuevo password a establecer

        Raises:
            ValueError: Si el usuario no existe
            ValueError: Si el password actual es incorrecto
            ValueError: Si el nuevo password no cumple requisitos

        Example:
            >>> service.cambiar_password(1, "viejo123", "nuevo123")
        """
        usuario = self.obtener_usuario(id)

        if not self._verify_password(password_actual, usuario.password_hash):
            raise ValueError("Password actual incorrecto")

        if len(password_nuevo) < 8:
            raise ValueError("Nuevo password debe tener 8+ caracteres")

        usuario.password_hash = self._hash_password(password_nuevo)
        usuario.actualizado_en = datetime.now()
        self.repo.update(usuario)

    def listar_activos(self) -> List[Usuario]:
        """
        Lista todos los usuarios activos.

        Returns:
            Lista de usuarios con estado=ACTIVO

        Example:
            >>> activos = service.listar_activos()
            >>> all(u.esta_activo() for u in activos)
            True
        """
        return self.repo.get_activos()

    def listar_todos(self) -> List[Usuario]:
        """
        Lista todos los usuarios sin filtrar.

        Returns:
            Lista de todos los usuarios

        Example:
            >>> todos = service.listar_todos()
            >>> len(todos) > 0
        """
        return self.repo.get_all()

    def _hash_password(self, password: str) -> str:
        """
        Hashea un password con bcrypt.

        Utiliza bcrypt con un salt generado automáticamente para
        almacenar passwords de forma segura.

        Args:
            password: Password en texto plano

        Returns:
            Hash del password como string

        Note:
            Nunca almacenar passwords en texto plano. Siempre usar hash.
        """
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def _verify_password(self, password: str, password_hash: str) -> bool:
        """
        Verifica un password contra su hash almacenado.

        Args:
            password: Password en texto plano a verificar
            password_hash: Hash almacenado del password

        Returns:
            True si el password coincide con el hash

        Note:
            Usa bcrypt que es seguro contra timing attacks.
        """
        return bcrypt.checkpw(
            password.encode('utf-8'),
            password_hash.encode('utf-8')
        )
