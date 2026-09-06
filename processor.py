import time
import functools
import logging

# Configure logging for network operations
logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, backoff_factor=1.0):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Final attempt {attempts} failed: {e}")
                        raise
                    
                    sleep_time = backoff_factor * (2 ** (attempts - 1))
                    logger.warning(f"Attempt {attempts} failed. Retrying in {sleep_time}s...")
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, backoff_factor=0.5)
def fetch_data(url):
    """Example network operation function."""
    # Simulation of a network call
    print(f"Fetching from {url}")
    raise ConnectionError("Server unreachable")