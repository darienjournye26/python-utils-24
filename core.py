import os
from typing import Any, Dict, List, Optional

def get_env(key: str, default: Any = None) -> Any:
    """Retrieve environment variable with optional default value."""
    return os.environ.get(key, default)

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Recursively flatten a nested list structure."""
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def chunk_iterable(iterable: List[Any], size: int) -> List[List[Any]]:
    """Split an iterable into smaller chunks of specific size."""
    return [iterable[i : i + size] for i in range(0, len(iterable), size)]

def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    """Perform deep merge of two dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

def ensure_directory(path: str) -> None:
    """Create directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)