import functools
import time
from typing import Callable, Any, Dict

# Cache for expensive computation results to optimize core operations
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function return values based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

@memoize
def heavy_computation(data: int) -> int:
    """Simulated intensive task optimized via memoization."""
    time.sleep(1)
    return data * data

class DataProcessor:
    """Performance-tuned processor for data streams."""
    def __init__(self, multiplier: int = 1):
        self.multiplier = multiplier

    def process_batch(self, items: list[int]) -> list[int]:
        """Batch processing using list comprehension for speed."""
        return [i * self.multiplier for i in items]

def clear_cache() -> None:
    """Manual cache invalidation for memory management."""
    _memoization_cache.clear()