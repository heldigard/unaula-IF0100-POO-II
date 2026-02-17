"""
Schemas de Autenticación - TaskFlow (Pydantic)
Unidad: 3.2 - Pydantic y Validación
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class RegisterRequest(BaseModel):
    """Schema para registro de usuario."""

    username: str = Field(..., min_length=3, max_length=50, description="Nombre de usuario único")
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100, description="Password del usuario")
    nombre_completo: Optional[str] = Field(None, max_length=100, description="Nombre completo del usuario")


class LoginRequest(BaseModel):
    """Schema para solicitud de login."""

    username: str = Field(..., min_length=3, description="Nombre de usuario")
    password: str = Field(..., min_length=8, description="Password del usuario")


class LoginResponse(BaseModel):
    """Schema para respuesta de login."""

    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"
    expires_in: int
    usuario: "UsuarioResponse"


class TokenRefreshRequest(BaseModel):
    """Schema para refresh token."""

    refresh_token: str


class TokenResponse(BaseModel):
    """Schema para respuesta de token."""

    access_token: str
    token_type: str = "bearer"
    expires_in: int


class PasswordResetRequest(BaseModel):
    """Schema para solicitud de reset de password."""

    email: EmailStr


class PasswordResetConfirm(BaseModel):
    """Schema para confirmación de reset de password."""

    token: str
    new_password: str = Field(..., min_length=8, max_length=100)


# Para evitar import circular, importamos UsuarioResponse aquí
from .usuario import UsuarioResponse

# Actualizar las referencias forward
LoginResponse.model_rebuild()
