import json
from typing import Any, Dict, Optional

def deep_update(source: Dict[Any, Any], overrides: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merge two dictionaries."""
    for key, value in overrides.items():
        if isinstance(value, dict) and value:
            source[key] = deep_update(source.get(key, {}), value)
        else:
            source[key] = value
    return source

def safe_load_json(file_path: str) -> Optional[Dict[Any, Any]]:
    """Safe loading and parsing of json files."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def sanitize_data(data: Any) -> Any:
    """Convert non-serializable objects to string representations."""
    if isinstance(data, dict):
        return {str(k): sanitize_data(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_data(i) for i in data]
    if isinstance(data, (int, float, str, bool, type(None))):
        return data
    return str(data)

def format_as_json(data: Any, indent: int = 4) -> str:
    """Stringify data into clean json format."""
    return json.dumps(sanitize_data(data), indent=indent)