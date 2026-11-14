import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, backoff=2.0):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            delay = 1.0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Failed after {max_attempts} attempts: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed, retrying in {delay}s...")
                    time.sleep(delay)
                    delay *= backoff
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, backoff=2.0)
def fetch_data(url):
    """Example network call wrapper."""
    # Placeholder for actual socket or requests logic
    logger.info(f"Fetching from {url}")
    return True