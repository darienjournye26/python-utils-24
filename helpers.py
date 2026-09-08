from typing import List, Optional, Any, Callable

def filter_by_key(data: List[dict], key: str, value: Any) -> List[dict]:
    """
    Filter a list of dictionaries based on a specific key-value pair.

    Args:
        data: List of dictionaries to filter.
        key: The dictionary key to check.
        value: The target value to match.

    Returns:
        A filtered list of dictionaries.
    """
    return [item for item in data if item.get(key) == value]

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """
    Split a list into smaller sub-lists of a specified size.

    Args:
        items: The list to be partitioned.
        size: The maximum size of each chunk.

    Returns:
        A list containing the partitioned sub-lists.
    """
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [items[i:i + size] for i in range(0, len(items), size)]

def safe_apply(func: Callable, val: Any, default: Any = None) -> Any:
    """
    Execute a function on a value, returning a default on failure.

    Args:
        func: The function to execute.
        val: The input value for the function.
        default: Value to return if execution raises an exception.

    Returns:
        Result of the function or the default value.
    """
    try:
        return func(val)
    except Exception:
        return default