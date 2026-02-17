"""
Service de Proyecto - TaskFlow
Unidad: 2.6 - DDD: Servicios

Este módulo implementa la lógica de negocio relacionada con los proyectos,
actuando como una capa de coordinación entre los modelos y repositorios.
"""

from typing import List, Optional
from datetime import datetime

from ..models import Proyecto, EstadoProyecto
from ..repositories import ProyectoRepository
from ..schemas import ProyectoCreate, ProyectoUpdate


class ProyectoService:
    """
    Service con lógica de negocios de proyectos.

    Este service encapsula las reglas de negocio relacionadas con proyectos,
    como validaciones, permisos de usuario y gestión de estados.

    Attributes:
        repo: Instancia de ProyectoRepository para acceso a datos

    Example:
        >>> repo = ProyectoRepository()
        >>> service = ProyectoService(repo)
        >>> data = ProyectoCreate(nombre="Mi Proyecto", descripcion="Descripción")
        >>> proyecto = service.crear_proyecto(1, data)
    """

    def __init__(self, repo: ProyectoRepository) -> None:
        """
        Inicializa el service con un repositorio inyectado.

        Args:
            repo: Repositorio de proyectos a utilizar
        """
        self.repo = repo

    def crear_proyecto(
        self, usuario_id: int, data: ProyectoCreate
    ) -> Proyecto:
        """
        Crea un nuevo proyecto para un usuario.

        Valida los datos del proyecto antes de crearlo.

        Args:
            usuario_id: ID del usuario propietario del proyecto
            data: DTO con los datos del proyecto a crear

        Returns:
            Proyecto creado con ID asignado

        Raises:
            ValueError: Si el proyecto no pasa las validaciones del modelo

        Example:
            >>> data = ProyectoCreate(
            ...     nombre="TaskFlow",
            ...     descripcion="Sistema de gestión de tareas"
            ... )
            >>> proyecto = service.crear_proyecto(1, data)
            >>> assert proyecto.usuario_id == 1
        """
        proyecto = Proyecto(
            nombre=data.nombre,
            descripcion=data.descripcion,
            usuario_id=usuario_id,
            estado=EstadoProyecto.ACTIVO,
            creado_en=datetime.now(),
        )

        errores = proyecto.validar()
        if errores:
            raise ValueError(f"Proyecto inválido: {', '.join(errores)}")

        return self.repo.create(proyecto)

    def obtener_proyecto(
        self, id: int, usuario_id: Optional[int] = None
    ) -> Proyecto:
        """
        Obtiene un proyecto por ID con verificación de permiso opcional.

        Args:
            id: ID del proyecto
            usuario_id: ID del usuario para verificar permiso (opcional)

        Returns:
            Proyecto encontrado

        Raises:
            ValueError: Si el proyecto no existe
            ValueError: Si usuario_id es proporcionado y no coincide con el propietario

        Example:
            >>> proyecto = service.obtener_proyecto(1, usuario_id=1)
            >>> assert proyecto.usuario_id == 1
        """
        proyecto = self.repo.get_by_id(id)
        if not proyecto:
            raise ValueError(f"Proyecto con ID {id} no encontrado")

        if usuario_id is not None and proyecto.usuario_id != usuario_id:
            raise ValueError("No tienes permiso para ver este proyecto")

        return proyecto

    def listar_proyectos(
        self, usuario_id: Optional[int] = None
    ) -> List[Proyecto]:
        """
        Lista proyectos con filtro opcional por usuario.

        Args:
            usuario_id: ID del usuario para filtrar sus proyectos (opcional)

        Returns:
            Lista de proyectos (filtrados por usuario si se proporciona usuario_id)

        Example:
            >>> todos = service.listar_proyectos()
            >>> mis_proyectos = service.listar_proyectos(usuario_id=1)
        """
        if usuario_id:
            return self.repo.get_by_usuario(usuario_id)
        return self.repo.get_all()

    def actualizar_proyecto(
        self, id: int, data: ProyectoUpdate, usuario_id: Optional[int] = None
    ) -> Proyecto:
        """
        Actualiza un proyecto existente.

        Permite actualizar nombre, descripción y estado del proyecto.

        Args:
            id: ID del proyecto a actualizar
            data: DTO con los datos a actualizar
            usuario_id: ID del usuario para verificar permiso (opcional)

        Returns:
            Proyecto actualizado

        Raises:
            ValueError: Si el proyecto no existe
            ValueError: Si usuario_id es proporcionado y no coincide con el propietario

        Example:
            >>> data = ProyectoUpdate(
            ...     nombre="Nombre Actualizado",
            ...     estado=EstadoProyecto.COMPLETADO
            ... )
            >>> proyecto = service.actualizar_proyecto(1, data, usuario_id=1)
        """
        proyecto = self.obtener_proyecto(id, usuario_id)

        if data.nombre is not None:
            proyecto.nombre = data.nombre

        if data.descripcion is not None:
            proyecto.descripcion = data.descripcion

        if data.estado is not None:
            proyecto.estado = data.estado

        proyecto.actualizado_en = datetime.now()

        return self.repo.update(proyecto)

    def archivar_proyecto(self, id: int, usuario_id: int) -> Proyecto:
        """
        Archiva un proyecto (solo si pertenece al usuario).

        Cambia el estado del proyecto a ARCHIVADO.

        Args:
            id: ID del proyecto a archivar
            usuario_id: ID del usuario que solicita la acción

        Returns:
            Proyecto archivado

        Raises:
            ValueError: Si el proyecto no existe
            ValueError: Si el proyecto no pertenece al usuario

        Example:
            >>> proyecto = service.archivar_proyecto(1, usuario_id=1)
            >>> assert proyecto.estado == EstadoProyecto.ARCHIVADO
        """
        proyecto = self.obtener_proyecto(id, usuario_id)
        proyecto.archivar()
        proyecto.actualizado_en = datetime.now()
        return self.repo.update(proyecto)

    def reactivar_proyecto(self, id: int, usuario_id: int) -> Proyecto:
        """
        Reactiva un proyecto archivado o completado.

        Cambia el estado del proyecto a ACTIVO.

        Args:
            id: ID del proyecto a reactivar
            usuario_id: ID del usuario que solicita la acción

        Returns:
            Proyecto reactivado

        Raises:
            ValueError: Si el proyecto no existe o no pertenece al usuario

        Example:
            >>> proyecto = service.reactivar_proyecto(1, usuario_id=1)
            >>> assert proyecto.estado == EstadoProyecto.ACTIVO
        """
        proyecto = self.obtener_proyecto(id, usuario_id)
        proyecto.reactivar()
        proyecto.actualizado_en = datetime.now()
        return self.repo.update(proyecto)

    def completar_proyecto(self, id: int, usuario_id: int) -> Proyecto:
        """
        Marca un proyecto como completado.

        Cambia el estado del proyecto a COMPLETADO.

        Args:
            id: ID del proyecto a completar
            usuario_id: ID del usuario que solicita la acción

        Returns:
            Proyecto completado

        Raises:
            ValueError: Si el proyecto no existe o no pertenece al usuario

        Example:
            >>> proyecto = service.completar_proyecto(1, usuario_id=1)
            >>> assert proyecto.estado == EstadoProyecto.COMPLETADO
        """
        proyecto = self.obtener_proyecto(id, usuario_id)
        proyecto.completar()
        proyecto.actualizado_en = datetime.now()
        return self.repo.update(proyecto)

    def eliminar_proyecto(self, id: int, usuario_id: int) -> bool:
        """
        Elimina un proyecto (solo si pertenece al usuario).

        Args:
            id: ID del proyecto a eliminar
            usuario_id: ID del usuario que solicita la acción

        Returns:
            True si se eliminó correctamente

        Raises:
            ValueError: Si el proyecto no existe
            ValueError: Si el proyecto no pertenece al usuario

        Example:
            >>> eliminado = service.eliminar_proyecto(1, usuario_id=1)
            >>> assert eliminado is True
        """
        proyecto = self.obtener_proyecto(id, usuario_id)
        return self.repo.delete(id)

    def listar_proyectos_activos(self, usuario_id: Optional[int] = None) -> List[Proyecto]:
        """
        Lista solo los proyectos activos.

        Args:
            usuario_id: ID del usuario para filtrar (opcional)

        Returns:
            Lista de proyectos con estado=ACTIVO

        Example:
            >>> activos = service.listar_proyectos_activos(usuario_id=1)
            >>> all(p.esta_activo() for p in activos)
            True
        """
        proyectos = self.repo.get_activos()
        if usuario_id:
            return [p for p in proyectos if p.usuario_id == usuario_id]
        return proyectos

    def listar_proyectos_archivados(self, usuario_id: Optional[int] = None) -> List[Proyecto]:
        """
        Lista solo los proyectos archivados.

        Args:
            usuario_id: ID del usuario para filtrar (opcional)

        Returns:
            Lista de proyectos con estado=ARCHIVADO

        Example:
            >>> archivados = service.listar_proyectos_archivados(usuario_id=1)
            >>> all(p.estado == EstadoProyecto.ARCHIVADO for p in archivados)
            True
        """
        proyectos = self.repo.get_archivados()
        if usuario_id:
            return [p for p in proyectos if p.usuario_id == usuario_id]
        return proyectos

    def contar_proyectos(self, usuario_id: Optional[int] = None) -> int:
        """
        Cuenta el total de proyectos (filtrados por usuario si se especifica).

        Args:
            usuario_id: ID del usuario para filtrar (opcional)

        Returns:
            Número total de proyectos

        Example:
            >>> total = service.contar_proyectos(usuario_id=1)
        """
        if usuario_id:
            return len(self.repo.get_by_usuario(usuario_id))
        return self.repo.count()
