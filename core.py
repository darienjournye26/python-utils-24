import time
import random
import functools
from typing import Callable, Any, Optional

def retry_network_op(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """
    Decorator to retry network operations with exponential backoff.
    
    :param max_attempts: Maximum number of retries.
    :param delay: Initial delay in seconds.
    :param backoff: Multiplier for the delay after each failure.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            current_delay = delay
            
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    
                    time.sleep(current_delay)
                    current_delay *= backoff
            
        return wrapper
    return decorator

def perform_request(url: str):
    """Example usage of retry logic for network requests."""
    print(f"Fetching {url}...")
    # Simulation of network flakiness
    if random.random() < 0.7:
        raise ConnectionError("Temporary network failure")
    return "Success"

# Example usage:
# @retry_network_op(max_attempts=3)
# def unstable_fetch():
#     return perform_request("https://api.example.com")