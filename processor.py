import collections.abc
from typing import Any, Dict, List, Optional

def flatten_dict(data: Dict[str, Any], sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionaries into a single-level dictionary."""
    items = {}
    for key, value in data.items():
        if isinstance(value, dict):
            new_items = flatten_dict(value, sep=sep)
            for n_key, n_value in new_items.items():
                items[f"{key}{sep}{n_key}"] = n_value
        else:
            items[key] = value
    return items

def clean_data(data: Any, allowed_types: Optional[tuple] = None) -> Any:
    """Recursively removes None values from nested structures."""
    if isinstance(data, dict):
        return {k: clean_data(v, allowed_types) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [clean_data(i, allowed_types) for i in data if i is not None]
    return data

def get_nested(data: Dict[str, Any], path: str, sep: str = '.') -> Any:
    """Retrieves value from nested dictionary using dot notation."""
    keys = path.split(sep)
    val = data
    try:
        for key in keys:
            val = val[key]
        return val
    except (KeyError, TypeError):
        return None