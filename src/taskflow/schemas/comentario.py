"""
Schemas de Comentario - TaskFlow (Pydantic)
Unidad: 3.2 - Pydantic y Validación
"""

from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional


class ComentarioBase(BaseModel):
    """Base schema para Comentario."""

    contenido: str = Field(..., min_length=1, max_length=5000, description="Contenido del comentario")


class ComentarioCreate(ComentarioBase):
    """Schema para crear comentario."""

    tarea_id: int = Field(..., gt=0, description="ID de la tarea")

    @field_validator('contenido')
    @classmethod
    def contenido_no_vacio(cls, v: str) -> str:
        """Valida que el contenido no esté vacío después de trim."""
        contenido_trimmed = v.strip()
        if not contenido_trimmed:
            raise ValueError('El contenido no puede estar vacío')
        return contenido_trimmed


class ComentarioUpdate(BaseModel):
    """Schema para actualizar comentario."""

    contenido: str = Field(..., min_length=1, max_length=5000)


class ComentarioResponse(ComentarioBase):
    """Schema para respuesta de comentario."""

    id: int
    tarea_id: int
    usuario_id: int
    creado_en: datetime

    class Config:
        from_attributes = True


class ComentarioWithUsuario(ComentarioResponse):
    """Schema para comentario con información de usuario."""

    username: str
    nombre_completo: Optional[str] = None
