from typing import Any, Dict, List, Union, Optional

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary with concatenated keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_none(data: Union[List, Dict]) -> Union[List, Dict]:
    """Recursively remove None values from lists and dictionaries."""
    if isinstance(data, dict):
        return {k: filter_none(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [filter_none(item) for item in data if item is not None]
    return data

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of defined size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive integer")
    return [data[i:i + size] for i in range(0, len(data), size)]

def safe_get(data: Dict, path: str, default: Any = None) -> Any:
    """Access nested dictionary keys using dot notation."""
    keys = path.split('.')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return default
    return data if data is not None else default