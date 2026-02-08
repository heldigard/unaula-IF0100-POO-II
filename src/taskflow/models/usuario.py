"""
Modelo de Usuario - TaskFlow
Unidad: 1.1 - Clases y Objetos
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from enum import Enum


class EstadoUsuario(Enum):
    """Estados posibles de un usuario en el sistema."""
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    SUSPENDIDO = "suspendido"


@dataclass
class Usuario:
    """
    Representa un usuario en el sistema TaskFlow.

    Attributes:
        id: Identificador único (None para nuevos usuarios)
        username: Nombre de usuario único
        email: Correo electrónico único
        password_hash: Hash del password (bcrypt)
        nombre_completo: Nombre completo del usuario
        estado: Estado del usuario (activo, inactivo, suspendido)
        creado_en: Fecha de creación
        actualizado_en: Fecha de última actualización

    Example:
        >>> usuario = Usuario(
        ...     username="jdoe",
        ...     email="john@example.com",
        ...     nombre_completo="John Doe"
        ... )
        >>> print(usuario)
        Usuario(jdoe)
    """

    id: Optional[int] = None
    username: str = ""
    email: str = ""
    password_hash: Optional[str] = None
    nombre_completo: Optional[str] = None
    estado: EstadoUsuario = EstadoUsuario.ACTIVO
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    def validar(self) -> List[str]:
        """
        Valida los campos del usuario.

        Returns:
            Lista de errores de validación (vacía si es válido)
        """
        errores = []

        if not self.username or len(self.username) < 3:
            errores.append("Username debe tener al menos 3 caracteres")

        if len(self.username) > 50:
            errores.append("Username no puede exceder 50 caracteres")

        if not self.email or "@" not in self.email:
            errores.append("Email inválido")

        if self.nombre_completo and len(self.nombre_completo) > 100:
            errores.append("Nombre completo no puede exceder 100 caracteres")

        return errores

    def es_valido(self) -> bool:
        """Verifica si el usuario es válido."""
        return len(self.validar()) == 0

    def activar(self) -> None:
        """Activa el usuario."""
        self.estado = EstadoUsuario.ACTIVO
        self.actualizado_en = datetime.now()

    def desactivar(self) -> None:
        """Desactiva el usuario."""
        self.estado = EstadoUsuario.INACTIVO
        self.actualizado_en = datetime.now()

    def suspender(self) -> None:
        """Suspende el usuario."""
        self.estado = EstadoUsuario.SUSPENDIDO
        self.actualizado_en = datetime.now()

    def esta_activo(self) -> bool:
        """Verifica si el usuario está activo."""
        return self.estado == EstadoUsuario.ACTIVO

    def __str__(self) -> str:
        """Representación string del usuario."""
        return f"Usuario({self.username})"

    def __repr__(self) -> str:
        """Representación para debugging."""
        return f"Usuario(id={self.id}, username={self.username}, email={self.email})"


@dataclass
class UsuarioCreacion:
    """DTO para creación de usuario (sin id y timestamps)."""
    username: str
    email: str
    password: str
    nombre_completo: Optional[str] = None


@dataclass
class UsuarioRespuesta:
    """DTO para respuesta de usuario (sin password)."""
    id: int
    username: str
    email: str
    nombre_completo: Optional[str] = None
    activo: bool = True
    creado_en: Optional[datetime] = None
