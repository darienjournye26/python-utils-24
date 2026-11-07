import functools
import time
from typing import Callable, Any, Dict

# Cache for storing expensive function results to optimize performance
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function return values."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

@memoize
def compute_intensive_data(n: int) -> int:
    """Simulates a resource-heavy calculation with memoization."""
    time.sleep(1)
    return sum(i * i for i in range(n))

def clear_cache() -> None:
    """Manual memory management for the cache."""
    _CACHE.clear()

if __name__ == '__main__':
    start = time.perf_counter()
    compute_intensive_data(1000)
    first_run = time.perf_counter() - start
    
    start = time.perf_counter()
    compute_intensive_data(1000)
    second_run = time.perf_counter() - start
    
    print(f'First run: {first_run:.4f}s, Cached run: {second_run:.4f}s')