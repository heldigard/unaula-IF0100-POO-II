"""TaskFlow domain entities."""

from dataclasses import dataclass
from datetime import datetime
from typing import Any
from uuid import UUID, uuid4


@dataclass
class Entity:
    """
    Base entity class with identity.

    All domain entities inherit from this class.
    """

    id: UUID
    created_at: datetime
    updated_at: datetime

    @classmethod
    def create(cls, **kwargs: Any) -> "Entity":
        """
        Create a new entity with generated ID and timestamps.

        Returns:
            New entity instance with generated values
        """
        now = datetime.utcnow()
        return cls(
            id=uuid4(),
            created_at=now,
            updated_at=now,
            **kwargs
        )

    def update(self, **kwargs: Any) -> None:
        """
        Update entity attributes and refresh updated_at timestamp.

        Args:
            **kwargs: Attributes to update
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                object.__setattr__(self, key, value)
        object.__setattr__(self, "updated_at", datetime.utcnow())


@dataclass
class Task(Entity):
    """Task entity representing a work item."""

    title: str
    description: str | None = None
    status: str = "pending"
    priority: str = "medium"
    due_date: datetime | None = None
    assigned_to: UUID | None = None
    project_id: UUID | None = None


@dataclass
class Project(Entity):
    """Project entity for organizing tasks."""

    name: str
    description: str | None = None
    status: str = "active"
    owner_id: UUID | None = None


@dataclass
class User(Entity):
    """User entity representing system users."""

    username: str
    email: str
    full_name: str | None = None
    is_active: bool = True
