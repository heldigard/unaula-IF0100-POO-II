"""
Schemas de Proyecto - TaskFlow (Pydantic)
Unidad: 3.2 - Pydantic y Validación
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Importar enums desde models para mantener consistencia
from ..models import EstadoProyecto


class ProyectoBase(BaseModel):
    """Base schema para Proyecto."""

    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre del proyecto")
    descripcion: Optional[str] = Field(None, max_length=1000, description="Descripción del proyecto")


class ProyectoCreate(ProyectoBase):
    """Schema para crear proyecto."""

    pass


class ProyectoUpdate(BaseModel):
    """Schema para actualizar proyecto."""

    nombre: Optional[str] = Field(None, min_length=3, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=1000)
    estado: Optional[EstadoProyecto] = None


class ProyectoResponse(ProyectoBase):
    """Schema para respuesta de proyecto."""

    id: int
    usuario_id: int
    estado: EstadoProyecto
    creado_en: datetime
    actualizado_en: datetime

    class Config:
        from_attributes = True


class ProyectoListResponse(BaseModel):
    """Schema para respuesta de lista de proyectos."""

    id: int
    nombre: str
    descripcion: Optional[str]
    estado: EstadoProyecto
    creado_en: datetime

    class Config:
        from_attributes = True


class ProyectoWithTareas(ProyectoResponse):
    """Schema para proyecto con conteo de tareas."""

    total_tareas: int = 0
    tareas_completadas: int = 0
    tareas_pendientes: int = 0
    tareas_en_progreso: int = 0
