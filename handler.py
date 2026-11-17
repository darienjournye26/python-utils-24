import functools
import time
import logging
from typing import Callable, Any, Dict

# Configure logger for performance monitoring
logger = logging.getLogger('python-utils-24.handler')

# Cache to store expensive function results
_memoization_cache: Dict[str, Any] = {}

def memoize_with_ttl(ttl_seconds: int = 300):
    """Decorator for result caching with TTL expiry."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
            now = time.time()
            
            if key in _memoization_cache:
                result, timestamp = _memoization_cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            _memoization_cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(items: list, chunk_size: int = 100):
    """Generator to yield chunks for efficient memory usage."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

@memoize_with_ttl(ttl_seconds=60)
def compute_heavy_task(data_id: int):
    """Simulated heavy computation core task."""
    time.sleep(1)  # Simulate I/O or CPU latency
    return f"Processed data for {data_id}"