"""
Aplicación FastAPI principal - TaskFlow
Unidad: 3.1 - Introducción a FastAPI
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routes import auth, usuarios, proyectos, tareas, frontend


def create_app() -> FastAPI:
    """Crea y configura la aplicación FastAPI."""

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="API del sistema de gestión de tareas TaskFlow",
        debug=settings.DEBUG,
    )

    # Configurar CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Incluir routers API (JSON)
    app.include_router(auth.router, prefix="/api/auth", tags=["Autenticación"])
    app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuarios"])
    app.include_router(proyectos.router, prefix="/api/proyectos", tags=["Proyectos"])
    app.include_router(tareas.router, prefix="/api/tareas", tags=["Tareas"])

    # Incluir router Frontend (HTML)
    app.include_router(frontend.router, tags=["Frontend"])

    @app.get("/api", tags=["API"])
    def api_root():
        """Endpoint raíz de la API."""
        return {
            "nombre": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "docs": "/docs",
            "frontend": "/",
        }

    @app.get("/health")
    def health():
        """Health check."""
        return {"status": "healthy"}

    return app


# Instancia de la aplicación
app = create_app()
