"""
Rutas Frontend - TaskFlow
Unidad: 3.7 - Servicios HTML con FastAPI

Este modulo contiene todas las rutas que renderizan templates HTML.
Mantiene separacion entre rutas API (JSON) y rutas frontend (HTML).

Rutas Publicas (no requieren autenticacion):
- GET / -> Pagina de inicio
- GET /login -> Formulario de login
- GET /registro -> Formulario de registro

Rutas Privadas (requieren autenticacion):
- GET /dashboard -> Dashboard principal
- GET /proyectos -> Lista de proyectos
- GET /proyectos/nuevo -> Formulario crear proyecto
- GET /proyectos/{id} -> Detalle de proyecto
- GET /tareas -> Lista de tareas
- GET /tareas/nueva -> Formulario crear tarea
- GET /tareas/{id} -> Detalle de tarea
- GET /perfil -> Perfil de usuario
"""

from typing import Optional
from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from ...models import Usuario
from ...repositories import UsuarioRepository, ProyectoRepository, TareaRepository
from ..dependencies import get_current_user, get_current_active_user
from ..config import settings


# Router de frontend
router = APIRouter(tags=["Frontend"])

# Configuracion de templates Jinja2
templates = Jinja2Templates(directory="src/taskflow/templates")

# Repositorios (en memoria por ahora)
_usuario_repo = UsuarioRepository()
_proyecto_repo = ProyectoRepository()
_tarea_repo = TareaRepository()


# ============================================================================
# RUTAS PUBLICAS (sin autenticacion)
# ============================================================================

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Pagina de inicio de TaskFlow."""
    # Obtener usuario actual desde cookie (opcional)
    current_user = _get_user_from_cookie(request)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "current_user": current_user,
        }
    )


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Pagina de login."""
    # Si ya esta autenticado, redirigir al dashboard
    current_user = _get_user_from_cookie(request)
    if current_user:
        return RedirectResponse(url="/dashboard", status_code=303)

    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "current_user": None,
        }
    )


@router.get("/registro", response_class=HTMLResponse)
async def registro_page(request: Request):
    """Pagina de registro."""
    # Si ya esta autenticado, redirigir al dashboard
    current_user = _get_user_from_cookie(request)
    if current_user:
        return RedirectResponse(url="/dashboard", status_code=303)

    return templates.TemplateResponse(
        "usuarios/registro.html",
        {
            "request": request,
            "current_user": None,
        }
    )


# ============================================================================
# RUTAS PRIVADAS (requieren autenticacion)
# ============================================================================

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
    """Dashboard principal del usuario."""
    # Calcular estadisticas del usuario
    proyectos = _proyecto_repo.get_by_usuario(current_user.id)
    tareas = _tarea_repo.get_by_asignado(current_user.id)

    stats = {
        "total_proyectos": len([p for p in proyectos if p.estado.value == "activo"]),
        "total_tareas": len(tareas),
        "tareas_pendientes": len([t for t in tareas if t.estado.value == "pendiente"]),
        "tareas_completadas": len([t for t in tareas if t.estado.value == "completada"]),
    }

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "current_user": current_user,
            "stats": stats,
        }
    )


@router.get("/proyectos", response_class=HTMLResponse)
async def proyectos_lista(
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
    """Lista de proyectos del usuario."""
    return templates.TemplateResponse(
        "proyectos/lista.html",
        {
            "request": request,
            "current_user": current_user,
        }
    )


@router.get("/proyectos/nuevo", response_class=HTMLResponse)
async def proyecto_nuevo(
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
    """Formulario para crear nuevo proyecto."""
    return templates.TemplateResponse(
        "proyectos/form.html",
        {
            "request": request,
            "current_user": current_user,
            "accion": "Crear",
            "boton_texto": "Crear Proyecto",
            "action_url": "/api/proyectos/",
            "proyecto": None,
        }
    )


@router.get("/proyectos/{proyecto_id}", response_class=HTMLResponse)
async def proyecto_detalle(
    proyecto_id: int,
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
    """Detalle de un proyecto especifico."""
    proyecto = _proyecto_repo.get_by_id(proyecto_id)

    # Verificar que el proyecto existe y pertenece al usuario
    if not proyecto or proyecto.usuario_id != current_user.id:
        return RedirectResponse(url="/proyectos", status_code=303)

    return templates.TemplateResponse(
        "proyectos/detalle.html",
        {
            "request": request,
            "current_user": current_user,
            "proyecto": proyecto,
        }
    )


@router.get("/proyectos/{proyecto_id}/editar", response_class=HTMLResponse)
async def proyecto_editar(
    proyecto_id: int,
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
    """Formulario para editar un proyecto."""
    proyecto = _proyecto_repo.get_by_id(proyecto_id)

    # Verificar que el proyecto existe y pertenece al usuario
    if not proyecto or proyecto.usuario_id != current_user.id:
        return RedirectResponse(url="/proyectos", status_code=303)

    return templates.TemplateResponse(
        "proyectos/form.html",
        {
            "request": request,
            "current_user": current_user,
            "accion": "Editar",
            "boton_texto": "Guardar Cambios",
            "action_url": f"/api/proyectos/{proyecto_id}",
            "proyecto": proyecto,
        }
    )


@router.get("/tareas", response_class=HTMLResponse)
async def tareas_lista(
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
    """Lista de tareas del usuario."""
    return templates.TemplateResponse(
        "tareas/lista.html",
        {
            "request": request,
            "current_user": current_user,
        }
    )


@router.get("/tareas/nueva", response_class=HTMLResponse)
async def tarea_nueva(
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
    """Formulario para crear nueva tarea."""
    # Obtener proyectos del usuario para el selector
    proyectos = _proyecto_repo.get_by_usuario(current_user.id)

    return templates.TemplateResponse(
        "tareas/form.html",
        {
            "request": request,
            "current_user": current_user,
            "accion": "Crear",
            "boton_texto": "Crear Tarea",
            "action_url": "/api/tareas/",
            "tarea": None,
            "proyectos": proyectos,
        }
    )


@router.get("/tareas/{tarea_id}", response_class=HTMLResponse)
async def tarea_detalle(
    tarea_id: int,
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
    """Detalle de una tarea especifica."""
    tarea = _tarea_repo.get_by_id(tarea_id)

    # Verificar que la tarea existe y pertenece al usuario
    if not tarea or tarea.asignado_a != current_user.id:
        return RedirectResponse(url="/tareas", status_code=303)

    return templates.TemplateResponse(
        "tareas/detalle.html",
        {
            "request": request,
            "current_user": current_user,
            "tarea": tarea,
        }
    )


@router.get("/tareas/{tarea_id}/editar", response_class=HTMLResponse)
async def tarea_editar(
    tarea_id: int,
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
    """Formulario para editar una tarea."""
    tarea = _tarea_repo.get_by_id(tarea_id)

    # Verificar que la tarea existe y pertenece al usuario
    if not tarea or tarea.asignado_a != current_user.id:
        return RedirectResponse(url="/tareas", status_code=303)

    # Obtener proyectos del usuario para el selector
    proyectos = _proyecto_repo.get_by_usuario(current_user.id)

    return templates.TemplateResponse(
        "tareas/form.html",
        {
            "request": request,
            "current_user": current_user,
            "accion": "Editar",
            "boton_texto": "Guardar Cambios",
            "action_url": f"/api/tareas/{tarea_id}",
            "tarea": tarea,
            "proyectos": proyectos,
        }
    )


@router.get("/perfil", response_class=HTMLResponse)
async def perfil(
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
    """Perfil del usuario actual."""
    # Calcular estadisticas del usuario
    tareas = _tarea_repo.get_by_asignado(current_user.id)
    proyectos = _proyecto_repo.get_by_usuario(current_user.id)

    tareas_completadas = len([t for t in tareas if t.estado == "completada"])
    tareas_pendientes = len([t for t in tareas if t.estado != "completada"])
    tasa_completacion = int((tareas_completadas / len(tareas) * 100) if tareas else 0)

    stats = {
        "proyectos": len(proyectos),
        "tareas_completadas": tareas_completadas,
        "tareas_pendientes": tareas_pendientes,
        "tasa_completacion": tasa_completacion,
    }

    return templates.TemplateResponse(
        "usuarios/perfil.html",
        {
            "request": request,
            "current_user": current_user,
            "usuario": current_user,
            "stats": stats,
        }
    )


# ============================================================================
# RUTAS ADICIONALES
# ============================================================================

@router.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    """Cierra la sesion del usuario y redirige al login."""
    response = RedirectResponse(url="/login", status_code=303)
    # Eliminar cookie de autenticacion
    response.delete_cookie(key="access_token")
    return response


# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def _get_user_from_cookie(request: Request) -> Optional[Usuario]:
    """
    Obtiene el usuario desde la cookie de autenticacion.

    Esta funcion auxiliar permite mostrar informacion del usuario
    en templates publicos sin requerir autenticacion completa.
    """
    # Intentar obtener token desde cookie
    token = request.cookies.get("access_token")
    if not token:
        return None

    # Token viene con formato "Bearer <token>", extraer solo el token
    if token.startswith("Bearer "):
        token = token[7:]

    # Decodificar token y obtener usuario
    try:
        from ..config import settings
        from ..security import verify_password
        from jose import jwt

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username:
            usuario = _usuario_repo.get_by_username(username)
            if usuario and usuario.esta_activo():
                return usuario
    except Exception:
        pass

    return None
