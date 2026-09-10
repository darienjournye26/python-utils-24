"""General utility helper functions for common data manipulation tasks."""

from typing import Any, Dict, Generator, Iterable, List, Type, TypeVar

T = TypeVar("T")


def chunk_iterable(iterable: Iterable[T], size: int) -> Generator[List[T], None, None]:
    """Yield successive chunks of specified size from an iterable."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than 0")
    
    chunk: List[T] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries into a new dictionary."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten a nested dictionary structure using a separator for keys."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def safe_cast(value: Any, to_type: Type[T], default: T = None) -> T:
    """Safely convert a value to a target type, returning default on failure."""
    try:
        return to_type(value)
    except (ValueError, TypeError):
        return default
