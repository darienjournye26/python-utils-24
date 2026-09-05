import functools
from typing import Callable, Any, Dict

# global cache for exception handling performance
_EXCEPTION_CACHE: Dict[str, Exception] = {}

class PerformanceBaseException(Exception):
    """Base exception class with cached stack trace suppression."""
    pass

def fast_exception(cls: type) -> Callable:
    """Decorator to optimize exception instantiation by caching common errors."""
    @functools.wraps(cls)
    def wrapper(*args: Any, **kwargs: Any) -> Exception:
        key = f"{cls.__name__}:{args}:{kwargs}"
        if key not in _EXCEPTION_CACHE:
            _EXCEPTION_CACHE[key] = cls(*args, **kwargs)
        return _EXCEPTION_CACHE[key]
    return wrapper

@fast_exception
class ConfigurationError(PerformanceBaseException):
    """Raised when configuration constraints are violated."""
    pass

@fast_exception
class ProcessingError(PerformanceBaseException):
    """Raised during core data processing failures."""
    pass

def clear_exception_cache() -> None:
    """Memory management for the exception cache."""
    _EXCEPTION_CACHE.clear()