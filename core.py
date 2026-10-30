import functools
import time
from typing import Callable, Any, Dict

# Cache for compute-heavy operations to reduce redundant processing
_LRU_CACHE_SIZE = 128
_RESULT_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _RESULT_CACHE:
            if len(_RESULT_CACHE) >= _LRU_CACHE_SIZE:
                _RESULT_CACHE.pop(next(iter(_RESULT_CACHE)))
            _RESULT_CACHE[key] = func(*args, **kwargs)
        return _RESULT_CACHE[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Generator for memory-efficient chunked list processing."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class PerformanceTracker:
    """Utility for measuring execution time of critical paths."""
    def __init__(self, label: str):
        self.label = label
        self.start = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"[PERF] {self.label}: {elapsed:.6f}s")