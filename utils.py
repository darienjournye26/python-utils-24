import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts: int = 3, delay: float = 1.0, exceptions: Tuple[Type[Exception], ...] = (Exception,)) -> Callable:
    """Decorator for retrying functions on specific exceptions."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    if attempt < max_attempts:
                        time.sleep(delay)
            
            logger.error(f"All {max_attempts} attempts failed.")
            raise last_exception
        return wrapper
    return decorator

def is_reachable(host: str, timeout: int = 5) -> bool:
    """Check network connectivity with a simple timeout."""
    import socket
    try:
        socket.create_connection((host, 80), timeout=timeout)
        return True
    except (socket.timeout, OSError):
        return False