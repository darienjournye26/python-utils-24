"""Custom exceptions and safe execution handlers for edge cases."""

import logging
from typing import Any, Callable, Optional, Type, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


class BaseUtilError(Exception):
    """Base exception class for all python-utils-24 operations."""

    pass


class ValidationError(BaseUtilError):
    """Raised when input data validation fails edge case checks."""

    pass


class ResourceNotFoundError(BaseUtilError):
    """Raised when a required key, file, or resource is missing."""

    pass


class ProcessingError(BaseUtilError):
    """Raised when an internal operation fails unexpectedly."""

    pass


def safe_execute(
    func: Callable[..., T],
    *args: Any,
    default: Optional[T] = None,
    expected_exceptions: Type[Exception] = Exception,
    **kwargs: Any,
) -> Optional[T]:
    """Execute a callable safely, returning a default value on expected errors."""
    try:
        return func(*args, **kwargs)
    except expected_exceptions as err:
        logger.warning("Handled expected exception during %s: %s", func.__name__, err)
        return default
    except Exception as err:
        logger.error("Unexpected error caught during %s: %s", func.__name__, err)
        raise ProcessingError(f"Operation '{func.__name__}' failed: {err}") from err
