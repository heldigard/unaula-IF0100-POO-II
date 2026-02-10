"""TaskFlow application services."""

from typing import Any

from taskflow.core.exceptions import NotFoundError
from taskflow.domain.entities import Task


class TaskService:
    """
    Service for task-related business logic.

    Coordinates between repositories and domain logic.
    """

    def __init__(self, task_repository: Any) -> None:
        """
        Initialize TaskService.

        Args:
            task_repository: Repository for task data access
        """
        self.task_repository = task_repository

    async def create_task(
        self,
        title: str,
        description: str | None = None,
        priority: str = "medium",
        **kwargs: Any
    ) -> Task:
        """
        Create a new task.

        Args:
            title: Task title
            description: Optional task description
            priority: Task priority level
            **kwargs: Additional task attributes

        Returns:
            Created task entity
        """
        task = Task.create(
            title=title,
            description=description,
            priority=priority,
            **kwargs
        )
        return await self.task_repository.save(task)

    async def get_task(self, task_id: str) -> Task:
        """
        Retrieve a task by ID.

        Args:
            task_id: Task identifier

        Returns:
            Task entity

        Raises:
            NotFoundError: If task does not exist
        """
        task = await self.task_repository.find_by_id(task_id)
        if task is None:
            raise NotFoundError("Task", task_id)
        return task

    async def list_tasks(
        self,
        page: int = 1,
        page_size: int = 20,
        **filters: Any
    ) -> list[Task]:
        """
        List tasks with pagination and filtering.

        Args:
            page: Page number (1-indexed)
            page_size: Number of items per page
            **filters: Optional filters (status, priority, etc.)

        Returns:
            List of tasks
        """
        return await self.task_repository.find_all(
            offset=(page - 1) * page_size,
            limit=page_size,
            **filters
        )

    async def update_task(
        self,
        task_id: str,
        **updates: Any
    ) -> Task:
        """
        Update an existing task.

        Args:
            task_id: Task identifier
            **updates: Fields to update

        Returns:
            Updated task entity

        Raises:
            NotFoundError: If task does not exist
        """
        task = await self.get_task(task_id)
        task.update(**updates)
        return await self.task_repository.save(task)

    async def delete_task(self, task_id: str) -> None:
        """
        Delete a task.

        Args:
            task_id: Task identifier

        Raises:
            NotFoundError: If task does not exist
        """
        task = await self.get_task(task_id)
        await self.task_repository.delete(task)
