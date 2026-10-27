import functools
from typing import Callable, Any, Dict

# internal cache for heavy computational results
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function results with single argument input"""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if kwargs:
            return func(*args, **kwargs)
        
        key = (func.__name__, args)
        if key not in _CACHE:
            _CACHE[key] = func(*args)
        return _CACHE[key]
    return wrapper

class BatchProcessor:
    def __init__(self, data: list):
        self.data = data

    def process_data(self, transform_func: Callable) -> list:
        """Optimized batch processing using list comprehension"""
        return [transform_func(item) for item in self.data]

    def clear_cache(self) -> None:
        """Reset shared cache state"""
        global _CACHE
        _CACHE.clear()