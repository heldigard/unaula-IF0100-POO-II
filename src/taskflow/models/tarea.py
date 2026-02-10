"""
Modelo de Tarea - TaskFlow
Unidad: 1.4 - Polimorfismo
"""

from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional, List
from enum import Enum


class EstadoTarea(Enum):
    """Estados posibles de una tarea."""
    PENDIENTE = "pendiente"
    EN_PROGRESO = "en_progreso"
    COMPLETADA = "completada"
    CANCELADA = "cancelada"


class PrioridadTarea(Enum):
    """Niveles de prioridad de una tarea."""
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"
    URGENTE = "urgente"


@dataclass
class Tarea:
    """
    Representa una tarea dentro de un proyecto.

    Attributes:
        id: Identificador único (None para nuevas tareas)
        titulo: Título de la tarea
        descripcion: Descripción de la tarea
        estado: Estado de la tarea
        prioridad: Nivel de prioridad
        proyecto_id: ID del proyecto al que pertenece
        asignado_a: ID del usuario asignado
        creada_por: ID del usuario que creó la tarea
        fecha_limite: Fecha límite para completar
        completada_en: Fecha de completitud
        creada_en: Fecha de creación
        actualizada_en: Fecha de última actualización

    Example:
        >>> tarea = Tarea(
        ...     titulo="Implementar API",
        ...     proyecto_id=1,
        ...     creada_por=1
        ... )
        >>> print(tarea)
        Tarea(Implementar API)
    """

    id: Optional[int] = None
    titulo: str = ""
    descripcion: Optional[str] = None
    estado: EstadoTarea = EstadoTarea.PENDIENTE
    prioridad: PrioridadTarea = PrioridadTarea.MEDIA
    proyecto_id: Optional[int] = None
    asignado_a: Optional[int] = None
    creada_por: Optional[int] = None
    fecha_limite: Optional[date] = None
    completada_en: Optional[datetime] = None
    creada_en: Optional[datetime] = None
    actualizada_en: Optional[datetime] = None

    def validar(self) -> List[str]:
        """
        Valida los campos de la tarea.

        Returns:
            Lista de errores de validación (vacía si es válida)
        """
        errores = []

        if not self.titulo or len(self.titulo) < 3:
            errores.append("Título debe tener al menos 3 caracteres")

        if len(self.titulo) > 200:
            errores.append("Título no puede exceder 200 caracteres")

        if self.descripcion and len(self.descripcion) > 2000:
            errores.append("Descripción no puede exceder 2000 caracteres")

        return errores

    def es_valida(self) -> bool:
        """Verifica si la tarea es válida."""
        return len(self.validar()) == 0

    def esta_pendiente(self) -> bool:
        """Verifica si la tarea está pendiente."""
        return self.estado == EstadoTarea.PENDIENTE

    def esta_en_progreso(self) -> bool:
        """Verifica si la tarea está en progreso."""
        return self.estado == EstadoTarea.EN_PROGRESO

    def esta_completada(self) -> bool:
        """Verifica si la tarea está completada."""
        return self.estado == EstadoTarea.COMPLETADA

    def iniciar(self) -> None:
        """Inicia la tarea (cambia estado a en_progreso)."""
        if self.estado == EstadoTarea.PENDIENTE:
            self.estado = EstadoTarea.EN_PROGRESO

    def completar(self) -> None:
        """Marca la tarea como completada."""
        self.estado = EstadoTarea.COMPLETADA
        self.completada_en = datetime.now()

    def cancelar(self) -> None:
        """Cancela la tarea."""
        self.estado = EstadoTarea.CANCELADA

    def esta_vencida(self) -> bool:
        """Verifica si la tarea está vencida (fecha límite pasada)."""
        if self.fecha_limite and self.estado != EstadoTarea.COMPLETADA:
            return date.today() > self.fecha_limite
        return False

    def __str__(self) -> str:
        """Representación string de la tarea."""
        return f"Tarea({self.titulo})"

    def __repr__(self) -> str:
        """Representación para debugging."""
        return f"Tarea(id={self.id}, titulo={self.titulo}, estado={self.estado.value})"

    # Sobrecarga de operadores para comparación por prioridad (polimorfismo)
    def __lt__(self, other: "Tarea") -> bool:
        """
        Compara tareas por prioridad (menor que).

        Permite ordenar tareas de menor a mayor prioridad.
        URGENTE > ALTA > MEDIA > BAJA

        Args:
            other: Otra tarea para comparar.

        Returns:
            True si esta tarea tiene menor prioridad que la otra.

        Example:
            >>> t1 = Tarea(titulo="Baja", prioridad=PrioridadTarea.BAJA)
            >>> t2 = Tarea(titulo="Alta", prioridad=PrioridadTarea.ALTA)
            >>> t1 < t2
            True
        """
        prioridad_order = {
            PrioridadTarea.BAJA: 0,
            PrioridadTarea.MEDIA: 1,
            PrioridadTarea.ALTA: 2,
            PrioridadTarea.URGENTE: 3
        }
        return prioridad_order[self.prioridad] < prioridad_order[other.prioridad]

    def __le__(self, other: "Tarea") -> bool:
        """Compara tareas por prioridad (menor o igual que)."""
        return self.__lt__(other) or self.prioridad == other.prioridad

    def __gt__(self, other: "Tarea") -> bool:
        """Compara tareas por prioridad (mayor que)."""
        return not self.__le__(other)

    def __ge__(self, other: "Tarea") -> bool:
        """Compara tareas por prioridad (mayor o igual que)."""
        return not self.__lt__(other)

    def __eq__(self, other: object) -> bool:
        """Compara si dos tareas tienen la misma prioridad."""
        if not isinstance(other, Tarea):
            return NotImplemented
        return self.prioridad == other.prioridad

    def __ne__(self, other: object) -> bool:
        """Compara si dos tareas tienen distinta prioridad."""
        if not isinstance(other, Tarea):
            return NotImplemented
        return self.prioridad != other.prioridad
