import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    """Custom exception for edge cases in data processing."""
    pass

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """
    Executes a callable with error handling for edge cases.
    Returns None if an exception occurs.
    """
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, KeyError) as e:
        logger.error(f"Invalid input data in {func.__name__}: {e}")
    except MemoryError:
        logger.critical("Insufficient memory for operation")
    except Exception as e:
        logger.exception(f"Unexpected failure in {func.__name__}: {e}")
    return None

def validate_and_process(data: Any, processor: Callable) -> Optional[Any]:
    """
    Validates data presence before triggering processor.
    """
    if data is None:
        logger.warning("Attempted to process empty data payload")
        return None

    if not isinstance(data, (dict, list)):
        raise ProcessingError(f"Unsupported data format: {type(data)}")

    return safe_execute(processor, data)