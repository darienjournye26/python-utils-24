import logging
from typing import Any, Callable, Optional, TypeVar, T

logger = logging.getLogger(__name__)

def safe_execute(func: Callable[..., T], *args: Any, default: Optional[T] = None, **kwargs: Any) -> Optional[T]:
    """
    Executes a callable with error catching for edge cases.
    Logs errors and returns a default value on failure.
    """
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError, KeyError) as e:
        logger.error(f"Execution error in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected runtime error: {e}")
        raise

def validate_input(value: Any, expected_type: type) -> bool:
    """
    Checks if input matches expected type and is not None.
    Returns false for malformed edge cases.
    """
    if value is None:
        return False
    if not isinstance(value, expected_type):
        return False
    return True

def normalize_data(data: Any) -> Any:
    """
    Sanitizes inputs to prevent type errors in pipelines.
    """
    if isinstance(data, str):
        return data.strip()
    if isinstance(data, (int, float)):
        return data
    return None