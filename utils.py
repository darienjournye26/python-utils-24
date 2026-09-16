import time
import logging
import functools
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)


def retry(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries a function call with exponential backoff.

    :param max_retries: Maximum number of retry attempts.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplicative factor applied to delay after each failure.
    :param exceptions: Tuple of exception classes to catch and retry on.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Execution failed for '{func.__name__}' after {max_retries} attempts: {err}"
                        )
                        raise

                    logger.warning(
                        f"Attempt {attempt}/{max_retries} failed for '{func.__name__}': {err}. "
                        f"Retrying in {current_delay:.2f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper
    return decorator
