"""TaskFlow custom exceptions."""


class TaskFlowException(Exception):
    """Base exception for all TaskFlow errors."""

    def __init__(self, message: str, details: dict | None = None) -> None:
        """
        Initialize TaskFlow exception.

        Args:
            message: Human-readable error message
            details: Additional error context (optional)
        """
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class NotFoundError(TaskFlowException):
    """Raised when a requested resource is not found."""

    def __init__(
        self,
        resource_type: str,
        resource_id: str | int,
        details: dict | None = None
    ) -> None:
        """
        Initialize NotFoundError.

        Args:
            resource_type: Type of resource (e.g., "Task", "User")
            resource_id: Identifier of the resource
            details: Additional error context (optional)
        """
        self.resource_type = resource_type
        self.resource_id = resource_id
        message = f"{resource_type} with id '{resource_id}' not found"
        super().__init__(message, details)


class ValidationError(TaskFlowException):
    """Raised when input validation fails."""

    def __init__(
        self,
        message: str,
        field: str | None = None,
        details: dict | None = None
    ) -> None:
        """
        Initialize ValidationError.

        Args:
            message: Validation error message
            field: Field that failed validation (optional)
            details: Additional error context (optional)
        """
        self.field = field
        super().__init__(message, details)


class ConflictError(TaskFlowException):
    """Raised when a conflict with existing data occurs."""

    def __init__(
        self,
        message: str,
        conflicting_resource: str | None = None,
        details: dict | None = None
    ) -> None:
        """
        Initialize ConflictError.

        Args:
            message: Conflict error message
            conflicting_resource: Resource causing the conflict (optional)
            details: Additional error context (optional)
        """
        self.conflicting_resource = conflicting_resource
        super().__init__(message, details)


class AuthenticationError(TaskFlowException):
    """Raised when authentication fails."""

    pass


class AuthorizationError(TaskFlowException):
    """Raised when user lacks permission for an action."""

    pass
