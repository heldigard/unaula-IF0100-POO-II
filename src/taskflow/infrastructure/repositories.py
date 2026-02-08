"""TaskFlow repository implementations."""

from typing import Any, Generic, TypeVar

from sqlalchemy.orm import Session

from taskflow.domain.entities import Entity

T = TypeVar("T", bound=Entity)


class Repository(Generic[T]):
    """
    Generic repository base class.

    Provides CRUD operations for entities.
    """

    def __init__(self, session: Session, model_class: type[T]) -> None:
        """
        Initialize repository.

        Args:
            session: Database session
            model_class: Entity model class
        """
        self.session = session
        self.model_class = model_class

    async def save(self, entity: T) -> T:
        """
        Save an entity.

        Args:
            entity: Entity to save

        Returns:
            Saved entity
        """
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    async def find_by_id(self, entity_id: str) -> T | None:
        """
        Find entity by ID.

        Args:
            entity_id: Entity identifier

        Returns:
            Entity if found, None otherwise
        """
        return self.session.query(self.model_class).filter(
            self.model_class.id == entity_id
        ).first()

    async def find_all(
        self,
        offset: int = 0,
        limit: int = 20,
        **filters: Any
    ) -> list[T]:
        """
        Find all entities with pagination and filtering.

        Args:
            offset: Number of items to skip
            limit: Maximum number of items to return
            **filters: Field filters

        Returns:
            List of entities
        """
        query = self.session.query(self.model_class)

        for key, value in filters.items():
            if hasattr(self.model_class, key):
                query = query.filter(getattr(self.model_class, key) == value)

        return query.offset(offset).limit(limit).all()

    async def delete(self, entity: T) -> None:
        """
        Delete an entity.

        Args:
            entity: Entity to delete
        """
        self.session.delete(entity)
        self.session.commit()

    async def count(self, **filters: Any) -> int:
        """
        Count entities matching filters.

        Args:
            **filters: Field filters

        Returns:
            Number of matching entities
        """
        query = self.session.query(self.model_class)

        for key, value in filters.items():
            if hasattr(self.model_class, key):
                query = query.filter(getattr(self.model_class, key) == value)

        return query.count()


class TaskRepository(Repository):
    """Repository for Task entities."""

    def __init__(self, session: Session) -> None:
        """
        Initialize TaskRepository.

        Args:
            session: Database session
        """
        from taskflow.domain.entities import Task
        super().__init__(session, Task)


class ProjectRepository(Repository):
    """Repository for Project entities."""

    def __init__(self, session: Session) -> None:
        """
        Initialize ProjectRepository.

        Args:
            session: Database session
        """
        from taskflow.domain.entities import Project
        super().__init__(session, Project)


class UserRepository(Repository):
    """Repository for User entities."""

    def __init__(self, session: Session) -> None:
        """
        Initialize UserRepository.

        Args:
            session: Database session
        """
        from taskflow.domain.entities import User
        super().__init__(session, User)
