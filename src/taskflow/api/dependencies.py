"""
Dependencias de FastAPI - TaskFlow
Unidad: 3.3 - Inyección de Dependencias
"""

from typing import Generator, Optional
from fastapi import Depends, Header, HTTPException, status
from jose import jwt, JWTError

from ..models import Usuario
from ..repositories import UsuarioRepository
from .config import settings


# Repositorios (en memoria por ahora, después será SQLAlchemy)
_usuario_repo = UsuarioRepository()


def get_usuario_repo() -> UsuarioRepository:
    """Obtiene el repositorio de usuarios."""
    return _usuario_repo


def get_current_user(
    authorization: Optional[str] = Header(None),
    repo: UsuarioRepository = Depends(get_usuario_repo),
) -> Usuario:
    """
    Obtiene el usuario autenticado desde el token JWT.

    Dependency inyectable en endpoints protegidos.
    """
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se proporcionó token de autenticación",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Extraer token (format: "Bearer <token>")
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Esquema de autenticación inválido",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Formato de token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Decodificar token
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Obtener usuario
    usuario = repo.get_by_username(username)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not usuario.esta_activo():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo"
        )

    return usuario


def get_current_active_user(
    current_user: Usuario = Depends(get_current_user),
) -> Usuario:
    """Verifica que el usuario esté activo."""
    if not current_user.esta_activo():
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return current_user
