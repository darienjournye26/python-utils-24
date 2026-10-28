import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None) -> Any:
    """
    Execute a function safely with comprehensive error handling for edge cases.
    """
    try:
        if not callable(func):
            raise TypeError(f"Expected callable, got {type(func).__name__}")
        return func(*args)
    except (ValueError, TypeError, ZeroDivisionError) as e:
        logger.error(f"Calculation error in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}")
        return default

def validate_input(value: Any, expected_type: type) -> bool:
    """
    Validate input types to prevent downstream processing errors.
    """
    try:
        return isinstance(value, expected_type)
    except Exception:
        return False

def batch_process(data: list, processor: Callable) -> list:
    """
    Process collections while ensuring partial failures do not halt execution.
    """
    results = []
    for item in data:
        try:
            results.append(processor(item))
        except Exception as e:
            logger.warning(f"Skipping item {item} due to error: {e}")
            continue
    return results