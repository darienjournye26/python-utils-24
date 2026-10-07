import functools
import time
import logging

# Configure logger for core operations
logger = logging.getLogger(__name__)

def memoize_with_expiry(ttl_seconds=300):
    """Decorator for caching results with time-based invalidation."""
    def decorator(func):
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            now = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

class DataHandler:
    """Optimized processing handler for core data operations."""
    def __init__(self):
        self._buffer = []

    @memoize_with_expiry(ttl_seconds=60)
    def process_heavy_computation(self, data_id: int) -> dict:
        """Simulated expensive operation with caching."""
        # Simulating processing latency
        time.sleep(0.5)
        return {"id": data_id, "status": "processed", "timestamp": time.time()}

    def batch_process(self, items: list) -> list:
        """List comprehension implementation for efficiency."""
        return [self.process_heavy_computation(i) for i in items]
