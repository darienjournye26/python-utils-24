from typing import Any, Dict, List, Optional
import json

def clean_data(data: Any) -> Any:
    """Recursively strip string whitespace from nested data structures."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_data(i) for i in data]
    elif isinstance(data, str):
        return data.strip()
    return data

def safe_load_json(file_path: str, default: Optional[Dict] = None) -> Dict:
    """Read json file with fallback default dictionary."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default if default is not None else {}

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flatten nested dictionary keys using separator."""
    items: List = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)