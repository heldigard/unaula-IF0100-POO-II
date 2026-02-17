"""
Service de Tarea - TaskFlow
Unidad: 2.6 - DDD: Servicios

Este módulo implementa la lógica de negocio relacionada con las tareas,
actuando como una capa de coordinación entre los modelos y repositorios.
"""

from typing import List, Optional
from datetime import datetime, date, timedelta

from ..models import Tarea, EstadoTarea, PrioridadTarea
from ..repositories import TareaRepository
from ..schemas import TareaCreate, TareaUpdate


class TareaService:
    """
    Service con lógica de negocio de tareas.

    Este service encapsula las reglas de negocio relacionadas con tareas,
    como validaciones, transiciones de estado y consultas especializadas.

    Attributes:
        repo: Instancia de TareaRepository para acceso a datos

    Example:
        >>> repo = TareaRepository()
        >>> service = TareaService(repo)
        >>> data = TareaCreate(
        ...     titulo="Implementar API",
        ...     proyecto_id=1,
        ...     asignado_a=2
        ... )
        >>> tarea = service.crear_tarea(data, creada_por=1)
    """

    def __init__(self, repo: TareaRepository) -> None:
        """
        Inicializa el service con un repositorio inyectado.

        Args:
            repo: Repositorio de tareas a utilizar
        """
        self.repo = repo

    def crear_tarea(self, data: TareaCreate, creada_por: int) -> Tarea:
        """
        Crea una nueva tarea.

        Valida los datos de la tarea antes de crearla.

        Args:
            data: DTO con los datos de la tarea a crear
            creada_por: ID del usuario que crea la tarea

        Returns:
            Tarea creada con ID asignado

        Raises:
            ValueError: Si la tarea no pasa las validaciones del modelo

        Example:
            >>> data = TareaCreate(
            ...     titulo="Implementar login",
            ...     descripcion="Crear endpoint de autenticación",
            ...     prioridad=PrioridadTarea.ALTA,
            ...     proyecto_id=1,
            ...     asignado_a=2,
            ...     fecha_limite=date(2026, 3, 1)
            ... )
            >>> tarea = service.crear_tarea(data, creada_por=1)
        """
        tarea = Tarea(
            titulo=data.titulo,
            descripcion=data.descripcion,
            prioridad=data.prioridad,
            proyecto_id=data.proyecto_id,
            asignado_a=data.asignado_a,
            creada_por=creada_por,
            fecha_limite=data.fecha_limite,
            estado=EstadoTarea.PENDIENTE,
            creada_en=datetime.now(),
        )

        errores = tarea.validar()
        if errores:
            raise ValueError(f"Tarea inválida: {', '.join(errores)}")

        return self.repo.create(tarea)

    def obtener_tarea(self, id: int) -> Tarea:
        """
        Obtiene una tarea por ID.

        Args:
            id: ID de la tarea

        Returns:
            Tarea encontrada

        Raises:
            ValueError: Si la tarea no existe

        Example:
            >>> tarea = service.obtener_tarea(1)
            >>> print(tarea.titulo)
        """
        tarea = self.repo.get_by_id(id)
        if not tarea:
            raise ValueError(f"Tarea con ID {id} no encontrada")
        return tarea

    def listar_tareas(self, **filtros) -> List[Tarea]:
        """
        Lista tareas con filtros opcionales.

        Args:
            **filtros: Filtros opcionales (proyecto_id, asignado_a, estado, etc.)

        Returns:
            Lista de tareas filtradas

        Example:
            >>> tareas = service.listar_tareas(proyecto_id=1, estado=EstadoTarea.PENDIENTE)
        """
        tareas = self.repo.get_all()

        # Aplicar filtros
        if 'proyecto_id' in filtros:
            tareas = [t for t in tareas if t.proyecto_id == filtros['proyecto_id']]

        if 'asignado_a' in filtros:
            tareas = [t for t in tareas if t.asignado_a == filtros['asignado_a']]

        if 'estado' in filtros:
            tareas = [t for t in tareas if t.estado == filtros['estado']]

        if 'prioridad' in filtros:
            tareas = [t for t in tareas if t.prioridad == filtros['prioridad']]

        return tareas

    def actualizar_tarea(self, id: int, data: TareaUpdate) -> Tarea:
        """
        Actualiza una tarea existente.

        Permite actualizar título, descripción, estado, prioridad, asignación y fecha límite.

        Args:
            id: ID de la tarea a actualizar
            data: DTO con los datos a actualizar

        Returns:
            Tarea actualizada

        Raises:
            ValueError: Si la tarea no existe

        Example:
            >>> data = TareaUpdate(
            ...     titulo="Título actualizado",
            ...     estado=EstadoTarea.EN_PROGRESO
            ... )
            >>> tarea = service.actualizar_tarea(1, data)
        """
        tarea = self.obtener_tarea(id)

        if data.titulo is not None:
            tarea.titulo = data.titulo

        if data.descripcion is not None:
            tarea.descripcion = data.descripcion

        if data.estado is not None:
            tarea.estado = data.estado

        if data.prioridad is not None:
            tarea.prioridad = data.prioridad

        if data.asignado_a is not None:
            tarea.asignado_a = data.asignado_a

        if data.fecha_limite is not None:
            tarea.fecha_limite = data.fecha_limite

        tarea.actualizada_en = datetime.now()

        return self.repo.update(tarea)

    def marcar_completada(self, id: int) -> Tarea:
        """
        Marca una tarea como completada.

        Cambia el estado a COMPLETADA y registra la fecha de completitud.

        Args:
            id: ID de la tarea a marcar como completada

        Returns:
            Tarea completada

        Raises:
            ValueError: Si la tarea no existe

        Example:
            >>> tarea = service.marcar_completada(1)
            >>> assert tarea.esta_completada()
            >>> assert tarea.completada_en is not None
        """
        tarea = self.obtener_tarea(id)
        tarea.completar()
        tarea.actualizada_en = datetime.now()
        return self.repo.update(tarea)

    def iniciar_tarea(self, id: int) -> Tarea:
        """
        Inicia una tarea (cambia estado a EN_PROGRESO).

        Args:
            id: ID de la tarea a iniciar

        Returns:
            Tarea en progreso

        Raises:
            ValueError: Si la tarea no existe

        Example:
            >>> tarea = service.iniciar_tarea(1)
            >>> assert tarea.esta_en_progreso()
        """
        tarea = self.obtener_tarea(id)
        tarea.iniciar()
        tarea.actualizada_en = datetime.now()
        return self.repo.update(tarea)

    def cancelar_tarea(self, id: int) -> Tarea:
        """
        Cancela una tarea.

        Args:
            id: ID de la tarea a cancelar

        Returns:
            Tarea cancelada

        Raises:
            ValueError: Si la tarea no existe

        Example:
            >>> tarea = service.cancelar_tarea(1)
            >>> assert tarea.estado == EstadoTarea.CANCELADA
        """
        tarea = self.obtener_tarea(id)
        tarea.cancelar()
        tarea.actualizada_en = datetime.now()
        return self.repo.update(tarea)

    def listar_vencidas(self) -> List[Tarea]:
        """
        Lista tareas vencidas (no completadas y fecha límite pasada).

        Returns:
            Lista de tareas vencidas

        Example:
            >>> vencidas = service.listar_vencidas()
            >>> all(t.esta_vencida() for t in vencidas)
            True
        """
        return self.repo.get_vencidas()

    def listar_por_vencer(self, dias: int = 7) -> List[Tarea]:
        """
        Lista tareas que vencerán en los próximos N días.

        Args:
            dias: Número de días a considerar (default: 7)

        Returns:
            Lista de tareas próximas a vencer

        Example:
            >>> por_vencer = service.listar_por_vencer(dias=3)
            >>> for t in por_vencer:
            ...     print(f"{t.titulo} vence en {t.fecha_limite}")
        """
        return self.repo.get_por_vencer(dias)

    def listar_tareas_proyecto(self, proyecto_id: int) -> List[Tarea]:
        """
        Lista todas las tareas de un proyecto.

        Args:
            proyecto_id: ID del proyecto

        Returns:
            Lista de tareas del proyecto

        Example:
            >>> tareas = service.listar_tareas_proyecto(1)
            >>> all(t.proyecto_id == 1 for t in tareas)
            True
        """
        return self.repo.get_by_proyecto(proyecto_id)

    def listar_tareas_asignadas(self, usuario_id: int) -> List[Tarea]:
        """
        Lista todas las tareas asignadas a un usuario.

        Args:
            usuario_id: ID del usuario asignado

        Returns:
            Lista de tareas asignadas al usuario

        Example:
            >>> tareas = service.listar_tareas_asignadas(2)
            >>> all(t.asignado_a == 2 for t in tareas)
            True
        """
        return self.repo.get_by_asignado(usuario_id)

    def listar_tareas_creadas(self, usuario_id: int) -> List[Tarea]:
        """
        Lista todas las tareas creadas por un usuario.

        Args:
            usuario_id: ID del usuario creador

        Returns:
            Lista de tareas creadas por el usuario

        Example:
            >>> tareas = service.listar_tareas_creadas(1)
            >>> all(t.creada_por == 1 for t in tareas)
            True
        """
        return self.repo.get_by_creador(usuario_id)

    def listar_tareas_pendientes(self, proyecto_id: Optional[int] = None) -> List[Tarea]:
        """
        Lista tareas pendientes (opcionalmente filtradas por proyecto).

        Args:
            proyecto_id: ID del proyecto para filtrar (opcional)

        Returns:
            Lista de tareas con estado=PENDIENTE

        Example:
            >>> pendientes = service.listar_tareas_pendientes(proyecto_id=1)
            >>> all(t.esta_pendiente() for t in pendientes)
            True
        """
        if proyecto_id:
            return self.repo.get_by_proyecto_y_estado(
                proyecto_id, EstadoTarea.PENDIENTE
            )
        return self.repo.get_pendientes()

    def listar_tareas_en_progreso(self, proyecto_id: Optional[int] = None) -> List[Tarea]:
        """
        Lista tareas en progreso (opcionalmente filtradas por proyecto).

        Args:
            proyecto_id: ID del proyecto para filtrar (opcional)

        Returns:
            Lista de tareas con estado=EN_PROGRESO

        Example:
            >>> en_progreso = service.listar_tareas_en_progreso(proyecto_id=1)
            >>> all(t.esta_en_progreso() for t in en_progreso)
            True
        """
        if proyecto_id:
            return self.repo.get_by_proyecto_y_estado(
                proyecto_id, EstadoTarea.EN_PROGRESO
            )
        return self.repo.get_en_progreso()

    def contar_tareas(self, proyecto_id: Optional[int] = None) -> int:
        """
        Cuenta el total de tareas (opcionalmente filtradas por proyecto).

        Args:
            proyecto_id: ID del proyecto para filtrar (opcional)

        Returns:
            Número total de tareas

        Example:
            >>> total = service.contar_tareas(proyecto_id=1)
        """
        if proyecto_id:
            return len(self.repo.get_by_proyecto(proyecto_id))
        return self.repo.count()

    def obtener_estadisticas_proyecto(self, proyecto_id: int) -> dict:
        """
        Obtiene estadísticas de tareas de un proyecto.

        Args:
            proyecto_id: ID del proyecto

        Returns:
            Diccionario con conteos por estado y prioridad

        Example:
            >>> stats = service.obtener_estadisticas_proyecto(1)
            >>> print(f"Total: {stats['total']}, Completadas: {stats['completadas']}")
        """
        tareas = self.repo.get_by_proyecto(proyecto_id)

        return {
            'total': len(tareas),
            'pendientes': len([t for t in tareas if t.esta_pendiente()]),
            'en_progreso': len([t for t in tareas if t.esta_en_progreso()]),
            'completadas': len([t for t in tareas if t.esta_completada()]),
            'canceladas': len([t for t in tareas if t.estado == EstadoTarea.CANCELADA]),
            'vencidas': len([t for t in tareas if t.esta_vencida()]),
            'por_prioridad': {
                'baja': len([t for t in tareas if t.prioridad == PrioridadTarea.BAJA]),
                'media': len([t for t in tareas if t.prioridad == PrioridadTarea.MEDIA]),
                'alta': len([t for t in tareas if t.prioridad == PrioridadTarea.ALTA]),
                'urgente': len([t for t in tareas if t.prioridad == PrioridadTarea.URGENTE]),
            }
        }
