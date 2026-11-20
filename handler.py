import json
from typing import Any, Optional, Dict

def safe_load_json(file_path: str, default: Optional[Dict] = None) -> Dict:
    """Reads and parses a JSON file with error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        return default if default is not None else {}

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionaries into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_by_keys(data: Dict[str, Any], keys: list) -> Dict[str, Any]:
    """Returns a dictionary subset containing only specified keys."""
    return {k: v for k, v in data.items() if k in keys}

def sanitize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}