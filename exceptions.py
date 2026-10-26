"""Custom exceptions module for python-utils-24.

Provides a clean, unified exception hierarchy for package-wide error handling.
"""

from typing import Any, Dict, Optional


class BaseAppError(Exception):
    """Base exception class for all errors raised by python-utils-24."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Details: {self.details}"
        return self.message


class ValidationError(BaseAppError):
    """Raised when input validation or schema check fails."""

    def __init__(self, message: str, field_name: Optional[str] = None, **kwargs: Any) -> None:
        details = kwargs.pop("details", {})
        if field_name:
            details["field"] = field_name
        super().__init__(message, details=details)


class ProcessingError(BaseAppError):
    """Raised when an error occurs during core data processing operations."""

    pass


class ConfigurationError(BaseAppError):
    """Raised when configuration parameters are invalid or missing."""

    pass


class ResourceNotFoundError(BaseAppError):
    """Raised when a required file or resource cannot be located."""

    pass
