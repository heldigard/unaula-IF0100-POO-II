"""TaskFlow value objects."""

from dataclasses import dataclass
from enum import Enum


class TaskStatus(str, Enum):
    """Valid task status values."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TaskPriority(str, Enum):
    """Valid task priority levels."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class ProjectStatus(str, Enum):
    """Valid project status values."""

    ACTIVE = "active"
    ARCHIVED = "archived"
    ON_HOLD = "on_hold"


@dataclass(frozen=True)
class Email:
    """Value object for email validation."""

    value: str

    def __post_init__(self) -> None:
        """Validate email format."""
        if "@" not in self.value or "." not in self.value.split("@")[-1]:
            raise ValueError(f"Invalid email format: {self.value}")


@dataclass(frozen=True)
class PaginationLimit:
    """Value object for pagination limit validation."""

    value: int

    def __post_init__(self) -> None:
        """Validate pagination limits."""
        if self.value < 1:
            raise ValueError("Limit must be at least 1")
        if self.value > 100:
            raise ValueError("Limit cannot exceed 100")
