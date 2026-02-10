"""
Rutas de usuarios - TaskFlow API
Unidad: 3.5 - CRUD completo con FastAPI

Este módulo contiene los endpoints para gestión de usuarios:
- GET /api/usuarios - Listar todos los usuarios
- GET /api/usuarios/{id} - Obtener usuario por ID
- PATCH /api/usuarios/{id} - Actualizar usuario
- DELETE /api/usuarios/{id} - Eliminar usuario
- PATCH /api/usuarios/{id}/activar - Activar usuario
- PATCH /api/usuarios/{id}/desactivar - Desactivar usuario
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from ...models import Usuario
from ...schemas import UsuarioResponse, UsuarioUpdate
from ...services.usuario_service import UsuarioService
from ...repositories import UsuarioRepository
from ..dependencies import get_usuario_repo, get_current_active_user


router = APIRouter()


@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios(
    solo_activos: bool = False,
    repo: UsuarioRepository = Depends(get_usuario_repo),
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Lista todos los usuarios (solo administradores).

    - **solo_activos**: Si es True, solo retorna usuarios activos
    """
    # TODO: Verificar que sea admin
    service = UsuarioService(repo)
    usuarios = service.listar_usuarios(solo_activos=solo_activos)
    return [
        UsuarioResponse(
            id=u.id,
            username=u.username,
            email=u.email,
            nombre_completo=u.nombre_completo,
            estado=u.estado,
            creado_en=u.creado_en,
        )
        for u in usuarios
    ]


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(
    usuario_id: int,
    repo: UsuarioRepository = Depends(get_usuario_repo),
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Obtiene un usuario por ID.

    Cualquier usuario puede ver su propio perfil.
    Los administradores pueden ver cualquier perfil.
    """
    service = UsuarioService(repo)

    # TODO: Verificar permisos (solo propio o admin)

    try:
        usuario = service.obtener_usuario(usuario_id)
        return UsuarioResponse(
            id=usuario.id,
            username=usuario.username,
            email=usuario.email,
            nombre_completo=usuario.nombre_completo,
            estado=usuario.estado,
            creado_en=usuario.creado_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.patch("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(
    usuario_id: int,
    data: UsuarioUpdate,
    repo: UsuarioRepository = Depends(get_usuario_repo),
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Actualiza un usuario (solo el propio o admin).

    - **nombre_completo**: Nombre completo del usuario
    - **estado**: Estado del usuario (solo admin)
    """
    service = UsuarioService(repo)

    # TODO: Verificar permisos

    try:
        usuario = service.actualizar_usuario(usuario_id, data)
        return UsuarioResponse(
            id=usuario.id,
            username=usuario.username,
            email=usuario.email,
            nombre_completo=usuario.nombre_completo,
            estado=usuario.estado,
            creado_en=usuario.creado_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(
    usuario_id: int,
    repo: UsuarioRepository = Depends(get_usuario_repo),
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Elimina un usuario (solo administradores).

    - **usuario_id**: ID del usuario a eliminar
    """
    # TODO: Verificar que sea admin
    service = UsuarioService(repo)

    try:
        service.eliminar_usuario(usuario_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.patch("/{usuario_id}/activar", response_model=UsuarioResponse)
def activar_usuario(
    usuario_id: int,
    repo: UsuarioRepository = Depends(get_usuario_repo),
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Activa un usuario (solo administradores).
    """
    # TODO: Verificar que sea admin
    service = UsuarioService(repo)

    try:
        usuario = service.activar_usuario(usuario_id)
        return UsuarioResponse(
            id=usuario.id,
            username=usuario.username,
            email=usuario.email,
            nombre_completo=usuario.nombre_completo,
            estado=usuario.estado,
            creado_en=usuario.creado_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.patch("/{usuario_id}/desactivar", response_model=UsuarioResponse)
def desactivar_usuario(
    usuario_id: int,
    repo: UsuarioRepository = Depends(get_usuario_repo),
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Desactiva un usuario (solo administradores).
    """
    # TODO: Verificar que sea admin
    service = UsuarioService(repo)

    try:
        usuario = service.desactivar_usuario(usuario_id)
        return UsuarioResponse(
            id=usuario.id,
            username=usuario.username,
            email=usuario.email,
            nombre_completo=usuario.nombre_completo,
            estado=usuario.estado,
            creado_en=usuario.creado_en,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
