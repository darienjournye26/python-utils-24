import json
from typing import Any, Dict, List, Optional

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller chunks of a fixed size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [data[i:i + size] for i in range(0, len(data), size)]

def safe_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieves a nested value using dot notation string."""
    keys = path.split('.')
    val = data
    try:
        for key in keys:
            val = val[key]
        return val
    except (KeyError, TypeError, AttributeError):
        return default

def unique_by_key(items: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
    """Filters a list of dictionaries by unique key values."""
    seen = set()
    result = []
    for item in items:
        val = item.get(key)
        if val not in seen:
            seen.add(val)
            result.append(item)
    return result