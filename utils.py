import functools
import time
from typing import Callable, Any, Dict

# Cache for performance optimization of expensive function calls
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Generator to process large datasets in memory-efficient chunks."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

@memoize
def heavy_computation(n: int) -> int:
    """Simulates a resource-intensive operation."""
    time.sleep(1)
    return n * n

def clear_cache() -> None:
    """Manual reset for the internal memoization cache."""
    _memoization_cache.clear()