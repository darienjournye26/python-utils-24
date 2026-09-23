import time
import logging
from typing import Callable, Any, Type, Tuple
import functools

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """Decorator that retries a network operation with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error("Operation %s failed after %d attempts: %s", func.__name__, max_retries, err)
                        raise
                    logger.warning(
                        "Attempt %d/%d for %s failed: %s. Retrying in %.2fs...",
                        attempt, max_retries, func.__name__, err, delay
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator


class NetworkProcessor:
    """Processor class handling retried network operations."""

    def __init__(self, max_retries: int = 3, backoff_factor: float = 2.0):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def execute_with_retry(self, operation: Callable, *args: Any, **kwargs: Any) -> Any:
        """Executes a given callable with configurable retry logic."""
        decorated_op = retry_network_op(
            max_retries=self.max_retries,
            backoff_factor=self.backoff_factor
        )(operation)
        return decorated_op(*args, **kwargs)
