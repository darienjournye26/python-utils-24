import logging
import functools
import time

# global cache for log formatting to avoid redundant object creation
_CACHE = {}

def memoized_logger(func):
    """performance optimization via result caching and lazy instantiation"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

class CoreLogger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self._level = self.logger.level

    def log_performance(self, message: str, start_time: float):
        """calculate duration only when logging is enabled to save cycles"""
        if self.logger.isEnabledFor(logging.INFO):
            duration = time.perf_counter() - start_time
            self.logger.info(f"{message} completed in {duration:.4f}s")

    @memoized_logger
    def get_structured_formatter(self, format_str: str):
        """reuse formatters across multiple logger instances"""
        return logging.Formatter(format_str)

# module level instance for performance
def get_logger(name: str):
    return CoreLogger(name)