import functools
import time
from typing import Callable, Any, Dict

# Cache dictionary for memoization of expensive calls
_LRU_CACHE: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function results to improve speed."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
        if key not in _LRU_CACHE:
            _LRU_CACHE[key] = func(*args, **kwargs)
        return _LRU_CACHE[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Generator for memory-efficient batch processing of lists."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def timed_execution(func: Callable) -> Callable:
    """Decorator to measure execution time for performance tuning."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper