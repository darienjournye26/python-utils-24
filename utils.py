import time
from typing import Any, Callable, Dict, Optional, TypeVar, List

T = TypeVar('T')

def retry(attempts: int = 3, delay: float = 1.0) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator to retry a function multiple times on failure."""
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args: Any, **kwargs: Any) -> T:
            last_exception: Optional[Exception] = None
            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    time.sleep(delay)
            raise last_exception or RuntimeError("Failed after retries")
        return wrapper
    return decorator

def chunk_list(data: List[T], size: int) -> List[List[T]]:
    """Split a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [data[i : i + size] for i in range(0, len(data), size)]

def format_data(data: Dict[str, Any], prefix: str = "LOG") -> str:
    """Format dictionary items into a consistent string representation."""
    items = [f"{k}={v}" for k, v in data.items()]
    return f"[{prefix}] " + " | ".join(items)