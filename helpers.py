"""General data handling utilities for python-utils-24."""

from typing import Any, Dict, Generator, Iterable, List


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary using key separation."""
    items: List[tuple[str, Any]] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def get_nested(
    data: Dict[str, Any], path: str, default: Any = None, sep: str = "."
) -> Any:
    """Safely retrieve a value from a deeply nested dictionary."""
    keys = path.split(sep)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def chunk_iterable(iterable: Iterable[Any], size: int) -> Generator[List[Any], None, None]:
    """Yield successive chunks of specified size from an iterable."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")

    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
