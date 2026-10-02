import time
import random
from functools import wraps
from typing import Callable, Any, Tuple, Type

def retry(
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True
) -> Callable:
    """
    Decorator for retrying a function with exponential backoff and jitter.

    :param exceptions: Tuple of exceptions to catch and retry on.
    :param tries: Total number of attempts.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to delay after each failure.
    :param jitter: If True, introduces randomness to delay to prevent thundering herd.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_delay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        raise e
                    
                    # Calculate next delay with optional jitter
                    current_delay = attempt_delay
                    if jitter:
                        current_delay *= random.uniform(0.5, 1.5)
                    
                    time.sleep(current_delay)
                    attempt_delay *= backoff
        return wrapper
    return decorator
