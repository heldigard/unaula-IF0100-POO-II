"""
Schemas de Usuario - TaskFlow (Pydantic)
Unidad: 3.2 - Pydantic y Validación
"""

from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime
from typing import Optional

# Enums
from ..models import EstadoUsuario


class UsuarioBase(BaseModel):
    """Base schema para Usuario."""

    username: str = Field(..., min_length=3, max_length=50, description="Nombre de usuario único")
    email: EmailStr
    nombre_completo: Optional[str] = Field(None, max_length=100, description="Nombre completo del usuario")


class UsuarioCreate(UsuarioBase):
    """Schema para crear usuario."""

    password: str = Field(..., min_length=8, max_length=100, description="Password del usuario")

    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        """Valida que el username solo contenga caracteres alfanuméricos, guiones y guiones bajos."""
        if not v.replace("-", "").replace("_", "").isalnum():
            raise ValueError('Username solo puede contener letras, números, guiones y guiones bajos')
        return v


class UsuarioUpdate(BaseModel):
    """Schema para actualizar usuario."""

    nombre_completo: Optional[str] = Field(None, max_length=100)
    estado: Optional[EstadoUsuario] = None


class UsuarioResponse(UsuarioBase):
    """Schema para respuesta de usuario."""

    id: int
    estado: EstadoUsuario
    creado_en: datetime

    class Config:
        from_attributes = True


class UsuarioLogin(BaseModel):
    """Schema para login."""

    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=8)


class UsuarioChangePassword(BaseModel):
    """Schema para cambio de password."""

    current_password: str = Field(..., min_length=8, description="Password actual")
    new_password: str = Field(..., min_length=8, max_length=100, description="Nuevo password")
