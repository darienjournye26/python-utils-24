import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Optional[Any] = None, **kwargs: Any) -> Any:
    """
    executes a callable with error handling for common runtime exceptions.
    logs failures and returns the provided default value on error.
    """
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, KeyError, IndexError) as e:
        logger.error(f"execution error in {func.__name__}: {str(e)}")
        return default
    except Exception as e:
        logger.critical(f"unexpected system error in {func.__name__}: {str(e)}")
        raise

def validate_input(data: Any, expected_type: type) -> bool:
    """
    validates input data type and structure robustness.
    returns false for none or mismatched types.
    """
    if data is None:
        return False
    if not isinstance(data, expected_type):
        logger.warning(f"input type mismatch: expected {expected_type}, got {type(data)}")
        return False
    return True

def get_nested_key(data: dict, keys: list, default: Any = None) -> Any:
    """
    traverses a nested dictionary using a list of keys safely.
    returns default value if any key path fails.
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