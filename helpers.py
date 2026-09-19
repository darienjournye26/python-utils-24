import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Executes a function with error handling for edge cases."""
    try:
        if not callable(func):
            raise ValueError(f"Provided object {func} is not callable")
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"Invalid input for operation: {e}")
        return default
    except Exception as e:
        logger.exception(f"Unexpected error during execution: {e}")
        return default

def get_nested_key(data: dict, keys: list, default: Any = None) -> Any:
    """Safely retrieves nested dictionary values."""
    if not isinstance(data, dict):
        return default
    
    current = data
    try:
        for key in keys:
            if not isinstance(current, dict) or key not in current:
                return default
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default

def validate_numeric(value: Any, min_val: float = 0, max_val: float = 1e9) -> Optional[float]:
    """Validates numeric input within bounds."""
    try:
        val = float(value)
        if min_val <= val <= max_val:
            return val
    except (TypeError, ValueError):
        pass
    return None