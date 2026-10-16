import json
from typing import Any, Dict, Optional, Union

def sanitize_data(data: Any) -> Any:
    """Recursively clean dictionary keys and handle basic types."""
    if isinstance(data, dict):
        return {str(k): sanitize_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data(i) for i in data]
    elif isinstance(data, (int, float, str, bool, type(None))):
        return data
    return str(data)

def format_json_response(data: Any, indent: int = 2) -> str:
    """Format data into a clean JSON string."""
    try:
        sanitized = sanitize_data(data)
        return json.dumps(sanitized, indent=indent)
    except (TypeError, ValueError) as e:
        return json.dumps({"error": "serialization failed", "details": str(e)})

def safe_extract(data: Dict[str, Any], keys: list, default: Any = None) -> Any:
    """Deep extraction of nested dictionary values."""
    current = data
    try:
        for key in keys:
            if not isinstance(current, dict):
                return default
            current = current.get(key, default)
        return current
    except Exception:
        return default