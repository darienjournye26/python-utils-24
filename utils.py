import time
import random
import functools
from typing import Callable, Any

def retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        raise e
                    
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator