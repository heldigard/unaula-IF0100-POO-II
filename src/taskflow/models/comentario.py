"""
Modelo de Comentario - TaskFlow
Unidad: 1.2 - Encapsulamiento
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class Comentario:
    """
    Representa un comentario en una tarea.

    Attributes:
        id: Identificador único (None para nuevos comentarios)
        contenido: Contenido del comentario
        tarea_id: ID de la tarea comentada
        usuario_id: ID del usuario que comentó
        creado_en: Fecha de creación

    Example:
        >>> comentario = Comentario(
        ...     contenido="Por favor revisar",
        ...     tarea_id=1,
        ...     usuario_id=1
        ... )
        >>> print(comentario)
        Comentario(1)
    """

    id: Optional[int] = None
    contenido: str = ""
    tarea_id: Optional[int] = None
    usuario_id: Optional[int] = None
    creado_en: Optional[datetime] = None

    def validar(self) -> List[str]:
        """
        Valida los campos del comentario.

        Returns:
            Lista de errores de validación (vacía si es válido)
        """
        errores = []

        if not self.contenido or len(self.contenido.strip()) == 0:
            errores.append("Contenido no puede estar vacío")

        if len(self.contenido) > 2000:
            errores.append("Contenido no puede exceder 2000 caracteres")

        return errores

    def es_valido(self) -> bool:
        """Verifica si el comentario es válido."""
        return len(self.validar()) == 0

    @property
    def contenido_corto(self) -> str:
        """
        Retorna una versión corta del contenido para previsualización.

        Returns:
            Los primeros 30 caracteres del contenido, seguidos de "..."
            si el contenido es más largo.

        Example:
            >>> c = Comentario(contenido="Este es un comentario muy largo")
            >>> c.contenido_corto
            'Este es un comentario muy lar...'
        """
        if len(self.contenido) > 30:
            return self.contenido[:30] + "..."
        return self.contenido

    def editar(self, nuevo_contenido: str) -> None:
        """
        Edita el contenido del comentario.

        Args:
            nuevo_contenido: Nuevo texto del comentario.

        Raises:
            ValueError: Si el nuevo contenido está vacío.
        """
        if not nuevo_contenido or len(nuevo_contenido.strip()) < 1:
            raise ValueError("Contenido no puede estar vacío")
        self.contenido = nuevo_contenido

    def __str__(self) -> str:
        """
        Representación string del comentario.

        Returns:
            String con el contenido acortado entre paréntesis.
        """
        contenido_short = self.contenido_corto
        return f"Comentario({contenido_short})"

    def __repr__(self) -> str:
        """Representación para debugging."""
        return f"Comentario(id={self.id}, contenido={self.contenido_corto}, tarea_id={self.tarea_id}, usuario_id={self.usuario_id})"

    def __len__(self) -> int:
        """
        Retorna la longitud del contenido del comentario.

        Returns:
            Número de caracteres en el contenido.

        Example:
            >>> c = Comentario(contenido="Hola mundo")
            >>> len(c)
            10
        """
        return len(self.contenido)
