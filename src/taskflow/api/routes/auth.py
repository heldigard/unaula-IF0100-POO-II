"""
Rutas de autenticación - TaskFlow API
Unidad: 3.6 - Autenticación JWT

Este módulo contiene los endpoints para autenticación de usuarios:
- POST /api/auth/register - Registrar nuevo usuario
- POST /api/auth/login - Iniciar sesión (OAuth2)
- GET /api/auth/me - Obtener perfil del usuario autenticado
"""

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from ...models import Usuario
from ...schemas import (
    RegisterRequest,
    LoginRequest,
    LoginResponse,
    UsuarioResponse,
)
from ...services.usuario_service import UsuarioService
from ...repositories import UsuarioRepository
from ..dependencies import get_usuario_repo, get_current_active_user
from ..security import create_access_token, verify_password
from ..config import settings


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


@router.post("/register", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registro(
    data: RegisterRequest,
    repo: UsuarioRepository = Depends(get_usuario_repo),
):
    """
    Registra un nuevo usuario en el sistema.

    - **username**: Nombre de usuario único (3-50 caracteres)
    - **email**: Correo electrónico válido
    - **password**: Mínimo 8 caracteres
    - **nombre_completo**: Opcional
    """
    service = UsuarioService(repo)

    try:
        usuario = service.crear_usuario(data)
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
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/login", response_model=LoginResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    repo: UsuarioRepository = Depends(get_usuario_repo),
):
    """
    Inicia sesión con username y password.

    Retorna un token JWT de acceso.
    """
    service = UsuarioService(repo)

    try:
        usuario = service.autenticar(form_data.username, form_data.password)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Crear token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": usuario.username},
        expires_delta=access_token_expires,
    )

    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        usuario=UsuarioResponse(
            id=usuario.id,
            username=usuario.username,
            email=usuario.email,
            nombre_completo=usuario.nombre_completo,
            estado=usuario.estado,
            creado_en=usuario.creado_en,
        )
    )


@router.get("/me", response_model=UsuarioResponse)
def profile(
    current_user: Usuario = Depends(get_current_active_user),
):
    """Obtiene el perfil del usuario autenticado."""
    return UsuarioResponse(
        id=current_user.id,
        username=current_user.username,
        email=current_user.email,
        nombre_completo=current_user.nombre_completo,
        estado=current_user.estado,
        creado_en=current_user.creado_en,
    )
