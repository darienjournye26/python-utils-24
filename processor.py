from typing import Any, Dict, List, Optional

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionary structures into single level."""
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_by_keys(data: Dict[str, Any], allowed_keys: List[str]) -> Dict[str, Any]:
    """Extracts specific keys from a dictionary if present."""
    return {k: v for k, v in data.items() if k in allowed_keys}

def safe_get(data: Dict[str, Any], path: str, default: Any = None, sep: str = '.') -> Any:
    """Retrieves nested values using dot notation."""
    keys = path.split(sep)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current