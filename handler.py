import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=2, backoff=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    if attempt == retries:
                        break
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            
            logger.error(f"All {retries + 1} attempts failed for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator