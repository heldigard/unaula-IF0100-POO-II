"""
Repositories package - TaskFlow
Unidad: 2.6 - DDD: Repositorios

Este paquete implementa el patrón Repository de Domain-Driven Design,
proporcionando una abstracción sobre el almacenamiento de datos.

Cada repository encapsula el acceso a los datos para una entidad del dominio,
permitiendo cambiar la implementación (en memoria, base de datos, API) sin
afectar el resto de la aplicación.
"""

from .base import Repository
from .usuario_repo import UsuarioRepository
from .proyecto_repo import ProyectoRepository
from .tarea_repo import TareaRepository
from .comentario_repo import ComentarioRepository

__all__ = [
    # Base
    "Repository",
    # Implementaciones
    "UsuarioRepository",
    "ProyectoRepository",
    "TareaRepository",
    "ComentarioRepository",
]
