"""TaskFlow FastAPI dependencies."""

from collections.abc import Generator
from typing import Annotated

from fastapi import Depends

from taskflow.application.services import TaskService
from taskflow.infrastructure.database import get_db
from taskflow.infrastructure.repositories import TaskRepository


def get_task_repository(
    db: Annotated[Generator, Depends(get_db)]
) -> TaskRepository:
    """
    Dependency for TaskRepository.

    Args:
        db: Database session

    Returns:
        TaskRepository instance
    """
    return TaskRepository(db)


def get_task_service(
    repository: Annotated[TaskRepository, Depends(get_task_repository)]
) -> TaskService:
    """
    Dependency for TaskService.

    Args:
        repository: Task repository

    Returns:
        TaskService instance
    """
    return TaskService(repository)
