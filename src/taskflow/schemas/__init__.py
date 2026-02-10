"""
Schemas package - TaskFlow

Schemas Pydantic para validación de request/response en FastAPI.
Unidad: 3.2 - Pydantic y Validación
"""

from .usuario import (
    UsuarioBase,
    UsuarioCreate,
    UsuarioUpdate,
    UsuarioResponse,
    UsuarioLogin,
    UsuarioChangePassword,
)

from .proyecto import (
    ProyectoBase,
    ProyectoCreate,
    ProyectoUpdate,
    ProyectoResponse,
    ProyectoListResponse,
    ProyectoWithTareas,
)

from .tarea import (
    TareaBase,
    TareaCreate,
    TareaUpdate,
    TareaResponse,
    TareaListResponse,
    TareaWithComentarios,
    TareaBulkUpdate,
)

from .comentario import (
    ComentarioBase,
    ComentarioCreate,
    ComentarioUpdate,
    ComentarioResponse,
    ComentarioWithUsuario,
)

from .auth import (
    RegisterRequest,
    LoginRequest,
    LoginResponse,
    TokenRefreshRequest,
    TokenResponse,
    PasswordResetRequest,
    PasswordResetConfirm,
)

# Re-exportar enums desde models para conveniencia
from ..models import (
    EstadoUsuario,
    EstadoProyecto,
    EstadoTarea,
    PrioridadTarea,
)

__all__ = [
    # Enums (re-exportados desde models)
    "EstadoUsuario",
    "EstadoProyecto",
    "EstadoTarea",
    "PrioridadTarea",
    # Usuario
    "UsuarioBase",
    "UsuarioCreate",
    "UsuarioUpdate",
    "UsuarioResponse",
    "UsuarioLogin",
    "UsuarioChangePassword",
    # Proyecto
    "ProyectoBase",
    "ProyectoCreate",
    "ProyectoUpdate",
    "ProyectoResponse",
    "ProyectoListResponse",
    "ProyectoWithTareas",
    # Tarea
    "TareaBase",
    "TareaCreate",
    "TareaUpdate",
    "TareaResponse",
    "TareaListResponse",
    "TareaWithComentarios",
    "TareaBulkUpdate",
    # Comentario
    "ComentarioBase",
    "ComentarioCreate",
    "ComentarioUpdate",
    "ComentarioResponse",
    "ComentarioWithUsuario",
    # Auth
    "RegisterRequest",
    "LoginRequest",
    "LoginResponse",
    "TokenRefreshRequest",
    "TokenResponse",
    "PasswordResetRequest",
    "PasswordResetConfirm",
]
