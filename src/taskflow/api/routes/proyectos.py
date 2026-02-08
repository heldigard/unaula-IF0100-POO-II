"""
Rutas de proyectos - TaskFlow API
Unidad: 3.5 - CRUD completo con FastAPI
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from ...models import Usuario
from ...schemas import (
    ProyectoCreate,
    ProyectoUpdate,
    ProyectoResponse,
    ProyectoListResponse,
)
from ...services import ProyectoService
from ...repositories import ProyectoRepository
from ..dependencies import get_current_active_user


router = APIRouter()

# Repo y service (en una app real serían singletons)
_proyecto_repo = ProyectoRepository()
_proyecto_service = ProyectoService(_proyecto_repo)


def get_proyecto_service():
    """Obtiene el service de proyectos."""
    return _proyecto_service


@router.post("/", response_model=ProyectoResponse, status_code=status.HTTP_201_CREATED)
def crear_proyecto(
    data: ProyectoCreate,
    current_user: Usuario = Depends(get_current_active_user),
    service: ProyectoService = Depends(get_proyecto_service),
):
    """
    Crea un nuevo proyecto.

    El proyecto se asocia al usuario autenticado.
    """
    try:
        proyecto = service.crear_proyecto(current_user.id, data)
        return ProyectoResponse(
            id=proyecto.id,
            nombre=proyecto.nombre,
            descripcion=proyecto.descripcion,
            usuario_id=proyecto.usuario_id,
            estado=proyecto.estado,
            creado_en=proyecto.creado_en,
            actualizado_en=proyecto.actualizado_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/", response_model=List[ProyectoListResponse])
def listar_proyectos(
    current_user: Usuario = Depends(get_current_active_user),
    service: ProyectoService = Depends(get_proyecto_service),
):
    """
    Lista los proyectos del usuario autenticado.
    """
    proyectos = service.listar_proyectos(current_user.id)
    return [
        ProyectoListResponse(
            id=p.id,
            nombre=p.nombre,
            estado=p.estado,
            creado_en=p.creado_en,
        )
        for p in proyectos
    ]


@router.get("/{proyecto_id}", response_model=ProyectoResponse)
def obtener_proyecto(
    proyecto_id: int,
    current_user: Usuario = Depends(get_current_active_user),
    service: ProyectoService = Depends(get_proyecto_service),
):
    """
    Obtiene un proyecto por ID (solo si es del usuario).
    """
    try:
        proyecto = service.obtener_proyecto(proyecto_id, current_user.id)
        return ProyectoResponse(
            id=proyecto.id,
            nombre=proyecto.nombre,
            descripcion=proyecto.descripcion,
            usuario_id=proyecto.usuario_id,
            estado=proyecto.estado,
            creado_en=proyecto.creado_en,
            actualizado_en=proyecto.actualizado_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.patch("/{proyecto_id}", response_model=ProyectoResponse)
def actualizar_proyecto(
    proyecto_id: int,
    data: ProyectoUpdate,
    current_user: Usuario = Depends(get_current_active_user),
    service: ProyectoService = Depends(get_proyecto_service),
):
    """
    Actualiza un proyecto (solo si es del usuario).
    """
    try:
        proyecto = service.actualizar_proyecto(
            proyecto_id,
            data,
            current_user.id
        )
        return ProyectoResponse(
            id=proyecto.id,
            nombre=proyecto.nombre,
            descripcion=proyecto.descripcion,
            usuario_id=proyecto.usuario_id,
            estado=proyecto.estado,
            creado_en=proyecto.creado_en,
            actualizado_en=proyecto.actualizado_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.delete("/{proyecto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_proyecto(
    proyecto_id: int,
    current_user: Usuario = Depends(get_current_active_user),
    service: ProyectoService = Depends(get_proyecto_service),
):
    """
    Elimina un proyecto (solo si es del usuario).
    """
    try:
        service.eliminar_proyecto(proyecto_id, current_user.id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
