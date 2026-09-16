import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_on_failure(exceptions: tuple[Type[Exception], ...] = (Exception,), 
                     max_retries: int = 3, 
                     delay: float = 1.0):
    """Decorator to retry network-bound operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Function {func.__name__} failed after {max_retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_on_failure(max_retries=3, delay=2.0)
def fetch_data(url: str):
    """Example usage for network data retrieval."""
    # Placeholder logic for network request simulation
    import random
    if random.random() < 0.7:
        raise ConnectionError("Service unavailable")
    return {"status": "success", "url": url}