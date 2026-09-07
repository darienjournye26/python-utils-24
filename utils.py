import time
import random
from functools import wraps
from typing import Callable, Any, Type, Tuple

def retry(exceptions: Tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            retries = 0
            current_delay = delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    retries += 1
                    if retries == max_retries:
                        raise
                    
                    # Jitter added to prevent thundering herd problem
                    sleep_time = current_delay + random.uniform(0, 0.1)
                    time.sleep(sleep_time)
                    current_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator