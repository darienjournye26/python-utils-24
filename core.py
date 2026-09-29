import time
from threading import Lock
from typing import Callable, Any, Dict, Tuple

class ThreadSafeTTLCache:
    """A thread-safe in-memory cache with TTL support for performance optimization."""

    def __init__(self, ttl: float = 60.0, max_size: int = 2048):
        self._ttl = ttl
        self._max_size = max_size
        self._store: Dict[Any, Tuple[float, Any]] = {}
        self._lock = Lock()

    def get(self, key: Any) -> Any:
        with self._lock:
            if key not in self._store:
                return None
            expiry, val = self._store[key]
            if time.monotonic() > expiry:
                del self._store[key]
                return None
            return val

    def set(self, key: Any, value: Any) -> None:
        with self._lock:
            now = time.monotonic()
            if len(self._store) >= self._max_size:
                # Clean expired keys first to free up space
                expired = [k for k, (exp, _) in self._store.items() if now > exp]
                for k in expired:
                    del self._store[k]
                # If still over limit, pop oldest item
                if len(self._store) >= self._max_size:
                    oldest_key = next(iter(self._store))
                    del self._store[oldest_key]
            self._store[key] = (now + self._ttl, value)

def memoize(ttl: float = 60.0, max_size: int = 2048):
    """Decorator to cache heavy function results with automatic TTL expiration."""
    cache = ThreadSafeTTLCache(ttl=ttl, max_size=max_size)

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Create a cache-safe representation of arguments
            cache_key = (args, tuple(sorted(kwargs.items())))
            try:
                hash(cache_key)
            except TypeError:
                # Uncacheable arguments fallback directly to computation
                return func(*args, **kwargs)

            cached_res = cache.get(cache_key)
            if cached_res is not None:
                return cached_res

            result = func(*args, **kwargs)
            cache.set(cache_key, result)
            return result
        return wrapper
    return decorator