import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(retries=3, delay=1.0, backoff=2.0):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {current_delay}s...")
                    
                    if attempt < retries:
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error("Max retries reached.")
            
            raise last_exception
        return wrapper
    return decorator

@with_retry(retries=3, delay=2)
def network_request(url):
    """Example of a network operation handler."""
    # Simulating actual network call logic
    logger.info(f"Fetching data from {url}")
    return {"status": 200, "data": "sample"}