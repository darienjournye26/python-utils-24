import functools
import time
from typing import Callable, Any, Dict

# Cache for storing expensive function results
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100) -> list:
    """Memory-efficient processing of large datasets."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceTracker:
    """Context manager for monitoring execution time."""
    def __init__(self, name: str):
        self.name = name
        self.start = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"[PERF] {self.name}: {elapsed:.4f}s")

def clear_cache() -> None:
    """Reset global cache to free memory."""
    _CACHE.clear()