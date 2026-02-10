"""
Schemas de Tarea - TaskFlow (Pydantic)
Unidad: 3.2 - Pydantic y Validación
"""

from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from typing import Optional

# Importar enums desde models para mantener consistencia
from ..models import EstadoTarea, PrioridadTarea


class TareaBase(BaseModel):
    """Base schema para Tarea."""

    titulo: str = Field(..., min_length=3, max_length=200, description="Título de la tarea")
    descripcion: Optional[str] = Field(None, max_length=2000, description="Descripción detallada")
    prioridad: PrioridadTarea = Field(default=PrioridadTarea.MEDIA, description="Prioridad de la tarea")
    fecha_limite: Optional[date] = Field(None, description="Fecha límite de entrega")


class TareaCreate(TareaBase):
    """Schema para crear tarea."""

    proyecto_id: int = Field(..., gt=0, description="ID del proyecto")
    asignado_a: Optional[int] = Field(None, gt=0, description="ID del usuario asignado")

    @field_validator('fecha_limite')
    @classmethod
    def fecha_limite_futura(cls, v: Optional[date]) -> Optional[date]:
        """Valida que la fecha límite sea futura o hoy."""
        if v and v < date.today():
            raise ValueError('La fecha límite debe ser hoy o en el futuro')
        return v


class TareaUpdate(BaseModel):
    """Schema para actualizar tarea."""

    titulo: Optional[str] = Field(None, min_length=3, max_length=200)
    descripcion: Optional[str] = Field(None, max_length=2000)
    estado: Optional[EstadoTarea] = None
    prioridad: Optional[PrioridadTarea] = None
    asignado_a: Optional[int] = Field(None, gt=0)
    fecha_limite: Optional[date] = None


class TareaResponse(TareaBase):
    """Schema para respuesta de tarea."""

    id: int
    estado: EstadoTarea
    proyecto_id: int
    creada_por: int
    asignado_a: Optional[int]
    fecha_limite: Optional[date]
    completada_en: Optional[datetime]
    creada_en: datetime
    actualizada_en: datetime

    class Config:
        from_attributes = True


class TareaListResponse(BaseModel):
    """Schema para respuesta de lista de tareas."""

    id: int
    titulo: str
    estado: EstadoTarea
    prioridad: PrioridadTarea
    proyecto_id: int
    asignado_a: Optional[int]
    fecha_limite: Optional[date]

    class Config:
        from_attributes = True


class TareaWithComentarios(TareaResponse):
    """Schema para tarea con comentarios."""

    comentarios: list = []


class TareaBulkUpdate(BaseModel):
    """Schema para actualización masiva de tareas."""

    tarea_ids: list[int] = Field(..., min_length=1, description="Lista de IDs de tareas")
    nuevo_estado: Optional[EstadoTarea] = None
    nueva_prioridad: Optional[PrioridadTarea] = None
