"""
Modelo de Proyecto - TaskFlow
Unidad: 1.3 - Herencia y Composición
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Any
from enum import Enum


class EstadoProyecto(Enum):
    """Estados posibles de un proyecto."""
    ACTIVO = "activo"
    ARCHIVADO = "archivado"
    COMPLETADO = "completado"


@dataclass
class Proyecto:
    """
    Representa un proyecto de tareas en el sistema TaskFlow.

    Attributes:
        id: Identificador único (None para nuevos proyectos)
        nombre: Nombre del proyecto
        descripcion: Descripción del proyecto
        usuario_id: ID del usuario propietario
        estado: Estado del proyecto
        creado_en: Fecha de creación
        actualizado_en: Fecha de última actualización

    Example:
        >>> proyecto = Proyecto(
        ...     nombre="TaskFlow",
        ...     descripcion="Sistema de gestión de tareas",
        ...     usuario_id=1
        ... )
        >>> print(proyecto)
        Proyecto(TaskFlow)
    """

    id: Optional[int] = None
    nombre: str = ""
    descripcion: Optional[str] = None
    usuario_id: Optional[int] = None
    estado: EstadoProyecto = EstadoProyecto.ACTIVO
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    def validar(self) -> List[str]:
        """
        Valida los campos del proyecto.

        Returns:
            Lista de errores de validación (vacía si es válido)
        """
        errores = []

        if not self.nombre or len(self.nombre) < 3:
            errores.append("Nombre debe tener al menos 3 caracteres")

        if len(self.nombre) > 100:
            errores.append("Nombre no puede exceder 100 caracteres")

        if self.descripcion and len(self.descripcion) > 1000:
            errores.append("Descripción no puede exceder 1000 caracteres")

        return errores

    def es_valido(self) -> bool:
        """Verifica si el proyecto es válido."""
        return len(self.validar()) == 0

    def agregar_tarea(self, tarea: Any) -> Any:
        """
        Agrega una tarea al proyecto (composición).

        Este método demuestra el concepto de composición donde
        el proyecto "contiene" tareas estableciendo la relación
        mediante el proyecto_id.

        Args:
            tarea: Instancia de Tarea que se agregará al proyecto.

        Returns:
            La misma tarea con el proyecto_id actualizado.

        Example:
            >>> from .tarea import Tarea
            >>> p = Proyecto(id=1, nombre="Mi Proyecto")
            >>> t = Tarea(titulo="Nueva tarea")
            >>> p.agregar_tarea(t)
            >>> t.proyecto_id
            1
        """
        tarea.proyecto_id = self.id
        return tarea

    def esta_activo(self) -> bool:
        """Verifica si el proyecto está activo."""
        return self.estado == EstadoProyecto.ACTIVO

    def esta_completado(self) -> bool:
        """Verifica si el proyecto está completado."""
        return self.estado == EstadoProyecto.COMPLETADO

    def archivar(self) -> None:
        """Archiva el proyecto."""
        self.estado = EstadoProyecto.ARCHIVADO
        self.actualizado_en = datetime.now()

    def completar(self) -> None:
        """Marca el proyecto como completado."""
        self.estado = EstadoProyecto.COMPLETADO
        self.actualizado_en = datetime.now()

    def reactivar(self) -> None:
        """Reactiva un proyecto archivado o completado."""
        self.estado = EstadoProyecto.ACTIVO
        self.actualizado_en = datetime.now()

    def __str__(self) -> str:
        """Representación string del proyecto."""
        return f"Proyecto({self.nombre})"

    def __repr__(self) -> str:
        """Representación para debugging."""
        return f"Proyecto(id={self.id}, nombre={self.nombre}, estado={self.estado.value})"
