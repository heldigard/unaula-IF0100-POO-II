"""
Services package - TaskFlow
Unidad: 2.6 - DDD: Servicios

Este paquete contiene los servicios del dominio que implementan
la lógica de negocio del sistema TaskFlow.

Los servicios actúan como una capa de coordinación entre:
- Los modelos (entidades del dominio)
- Los repositorios (acceso a datos)
- Los schemas (DTOs para validación)

Patrón implementado: Domain Service (DDD)
"""

from .usuario_service import UsuarioService
from .proyecto_service import ProyectoService
from .tarea_service import TareaService

__all__ = [
    "UsuarioService",
    "ProyectoService",
    "TareaService",
]
