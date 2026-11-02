from typing import Any, Iterable, Optional

def flatten_list(nested_list: Iterable[Any]) -> list[Any]:
    """Recursively flatten a nested list structure into a single list."""
    flat: list[Any] = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def chunk_iterable(data: Iterable[Any], size: int) -> Iterable[list[Any]]:
    """Split an iterable into smaller chunks of a specified size."""
    chunk: list[Any] = []
    for item in data:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def get_nested_key(data: dict[str, Any], keys: list[str], default: Any = None) -> Any:
    """Retrieve a value from a nested dictionary using a list of keys."""
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default