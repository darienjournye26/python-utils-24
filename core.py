import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_network_operation(
    max_retries: int = 3, 
    delay: float = 1.0, 
    exceptions: Tuple[Type[Exception], ...] = (ConnectionError, TimeoutError)
):
    """Decorator to retry network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(
                        f"Attempt {attempt + 1} failed for {func.__name__}: {e}. "
                        f"Retrying in {delay}s..."
                    )
                    time.sleep(delay)
            
            logger.error(f"All {max_retries} retries exhausted for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=2.0)
def fetch_data(url: str):
    """Example network call wrapper."""
    # Simulating actual network logic
    pass