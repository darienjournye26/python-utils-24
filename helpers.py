from typing import Any, Dict, Generator, Iterable, List, TypeVar

T = TypeVar("T")


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge dict2 into dict1 without modifying original dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def chunk_iterable(iterable: Iterable[T], size: int) -> Generator[List[T], None, None]:
    """Yield successive chunks of specified size from an iterable."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    chunk: List[T] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length, adding suffix if truncated."""
    if max_length < len(suffix):
        raise ValueError("max_length must be at least as long as suffix")
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten nested dictionary into single level dictionary with delimited keys."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
