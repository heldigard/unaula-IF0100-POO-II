"""TaskFlow FastAPI application."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from taskflow.core.config import settings
from taskflow.core.exceptions import TaskFlowException
from taskflow.infrastructure.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Application lifespan manager.

    Handles startup and shutdown events.
    """
    # Startup
    init_db()
    yield
    # Shutdown - cleanup if needed


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Task Management API with clean architecture",
    lifespan=lifespan
)


@app.exception_handler(TaskFlowException)
async def taskflow_exception_handler(
    request: Any,
    exc: TaskFlowException
) -> JSONResponse:
    """
    Handle TaskFlow custom exceptions.

    Args:
        request: Request object
        exc: TaskFlow exception

    Returns:
        JSON error response
    """
    return JSONResponse(
        status_code=400 if exc.details else 404,
        content={
            "error": exc.message,
            "details": exc.details
        }
    )


@app.get("/")
async def root() -> dict[str, str]:
    """
    Root endpoint.

    Returns:
        API information
    """
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "status": "running"
    }


@app.get("/health")
async def health() -> dict[str, str]:
    """
    Health check endpoint.

    Returns:
        Health status
    """
    return {"status": "healthy"}


# Import routers after app creation to avoid circular imports
# from taskflow.api.routers import tasks, projects, users
# app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])
# app.include_router(projects.router, prefix="/api/v1/projects", tags=["projects"])
# app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
