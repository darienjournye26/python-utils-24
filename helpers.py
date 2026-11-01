import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_on_failure(exceptions: tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations on specific exceptions."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries:
                        sleep_time = delay * (2 ** attempt)
                        logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {sleep_time}s...")
                        time.sleep(sleep_time)
            logger.error(f"Operation failed after {max_retries} retries: {last_exception}")
            raise last_exception
        return wrapper
    return decorator

def execute_with_retry(func: Callable, *args, **kwargs) -> Any:
    """Functional wrapper for network call retries."""
    retries = kwargs.pop('_max_retries', 3)
    delay = kwargs.pop('_delay', 1.0)
    
    for attempt in range(retries + 1):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == retries:
                raise e
            time.sleep(delay)
    return None