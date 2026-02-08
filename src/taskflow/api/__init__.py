"""
API package - TaskFlow
Unidad: 3.1 - Introducción a FastAPI

Este paquete contiene la aplicación FastAPI principal y todos los
componentes relacionados con la API REST:

- config.py: Configuración de la aplicación
- security.py: Utilidades de seguridad (JWT, password hashing)
- dependencies.py: Dependencias inyectables de FastAPI
- app.py: Aplicación FastAPI principal
- routes/: Endpoints de la API
"""

from .app import app, create_app
from .config import settings
from .security import create_access_token, verify_password, get_password_hash
from .dependencies import get_usuario_repo, get_current_user, get_current_active_user

__all__ = [
    # App
    "app",
    "create_app",
    # Config
    "settings",
    # Security
    "create_access_token",
    "verify_password",
    "get_password_hash",
    # Dependencies
    "get_usuario_repo",
    "get_current_user",
    "get_current_active_user",
]
