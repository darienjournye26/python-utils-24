import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None) -> Any:
    """
    executes a function safely with error handling
    returns the default value on failure
    """
    try:
        return func(*args)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"safe execution failed for {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"unexpected system error: {e}")
        raise

def parse_int(value: Any, fallback: int = 0) -> int:
    """
    converts input to integer with edge case handling
    """
    try:
        if value is None:
            return fallback
        return int(value)
    except (ValueError, TypeError):
        return fallback

def get_nested_key(data: dict, keys: list, default: Any = None) -> Any:
    """
    retrieves value from nested dict safely
    """
    if not isinstance(data, dict):
        return default
    
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default