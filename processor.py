from typing import Any, Dict, Generator, Iterable, List, Tuple


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into a single-level dictionary."""
    items: List[Tuple[str, Any]] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict) and value:
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def unflatten_dict(data: Dict[str, Any], sep: str = ".") -> Dict[str, Any]:
    """Reconstruct a nested dictionary from a flattened single-level dictionary."""
    result: Dict[str, Any] = {}
    for key, value in data.items():
        parts = key.split(sep)
        target = result
        for part in parts[:-1]:
            if part not in target or not isinstance(target[part], dict):
                target[part] = {}
            target = target[part]
        target[parts[-1]] = value
    return result


def chunk_iterable(
    iterable: Iterable[Any], chunk_size: int
) -> Generator[List[Any], None, None]:
    """Yield successive chunks of specified size from an iterable."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")

    chunk: List[Any] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
