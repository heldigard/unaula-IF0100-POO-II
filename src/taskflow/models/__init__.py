"""
Models package - TaskFlow

Este paquete contiene todos los modelos de dominio del sistema TaskFlow.
Cada modelo representa una entidad del dominio con sus atributos,
validaciones y métodos de negocio.

Unidades del curso:
- 1.1: Clases y Objetos (Usuario)
- 1.2: Encapsulamiento (Comentario)
- 1.3: Herencia y Composición (Proyecto)
- 1.4: Polimorfismo (Tarea)
"""

# Importar modelos individuales
from .usuario import (
    Usuario,
    UsuarioCreacion,
    UsuarioRespuesta,
    EstadoUsuario,
)
from .proyecto import Proyecto, EstadoProyecto
from .tarea import Tarea, EstadoTarea, PrioridadTarea
from .comentario import Comentario


__all__ = [
    # Enums
    "EstadoUsuario",
    "EstadoProyecto",
    "EstadoTarea",
    "PrioridadTarea",
    # Modelos
    "Usuario",
    "UsuarioCreacion",
    "UsuarioRespuesta",
    "Proyecto",
    "Tarea",
    "Comentario",
]
