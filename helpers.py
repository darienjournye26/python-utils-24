import functools
import time
import logging
from typing import Callable, Any

# Configure logger for core operations
logger = logging.getLogger(__name__)

def memoize(func: Callable) -> Callable:
    """Thread-safe cache decorator for intensive calculations."""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def time_execution(func: Callable) -> Callable:
    """Performance monitor for diagnostic timing."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        logger.debug(f"Execution of {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Memory-efficient generator for large dataset chunks."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class PerformanceProfiler:
    """Resource usage tracker for application bottlenecks."""
    def __init__(self):
        self.stats = {}

    def record(self, label: str, duration: float):
        self.stats[label] = self.stats.get(label, 0) + duration