from typing import Any, Dict, List, Optional, Union

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single-level structure."""
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_data(data: Any, allowed_types: tuple = (str, int, float, bool)) -> Any:
    """Recursively cleans dictionary or list values to allowed types."""
    if isinstance(data, dict):
        return {k: sanitize_data(v, allowed_types) for k, v in data.items() if isinstance(v, allowed_types + (dict, list))}
    elif isinstance(data, list):
        return [sanitize_data(item, allowed_types) for item in data if isinstance(item, allowed_types + (dict, list))]
    return data if isinstance(data, allowed_types) else None

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [data[i:i + size] for i in range(0, len(data), size)]