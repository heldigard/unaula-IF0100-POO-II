"""
Routes package - TaskFlow API

Unidad: 3.5 - CRUD completo con FastAPI
Unidad: 3.7 - Servicios HTML con FastAPI

Este paquete contiene todas las rutas de la API REST y del frontend HTML del sistema TaskFlow.
Cada archivo de rutas define los endpoints para una entidad específica.

Estructura:
- auth.py: Rutas de autenticación (login, registro, refresh token)
- usuarios.py: Rutas de gestión de usuarios
- proyectos.py: Rutas de gestión de proyectos
- tareas.py: Rutas de gestión de tareas
- comentarios.py: Rutas de gestión de comentarios
- frontend.py: Rutas que renderizan templates HTML (separación API/Frontend)

Patrones utilizados:
- APIRouter de FastAPI para modularidad
- Inyección de dependencias para servicios y autenticación
- Response models con Pydantic para validación
- Códigos de estado HTTP apropiados
- Manejo de errores con HTTPException
- Separación: API JSON vs HTML responses
"""

from .auth import router as auth_router
from .usuarios import router as usuarios_router
from .proyectos import router as proyectos_router
from .tareas import router as tareas_router
from .frontend import router as frontend_router

__all__ = [
    "auth_router",
    "usuarios_router",
    "proyectos_router",
    "tareas_router",
    "frontend_router",
]
