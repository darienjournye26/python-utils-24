import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Verify email format using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def ensure_list(data: Any) -> list:
    """Convert input to a list if not already one."""
    if data is None:
        return []
    if isinstance(data, list):
        return data
    return [data]

def sanitize_string(value: Optional[str], default: str = "") -> str:
    """Strip whitespace and return default if empty."""
    if not value or not isinstance(value, str):
        return default
    return value.strip()

def is_non_empty_dict(data: Any) -> bool:
    """Check if input is a non-empty dictionary."""
    return isinstance(data, dict) and len(data) > 0

def safe_get(data: dict, key: str, default: Any = None) -> Any:
    """Retrieve value from dict with fallback."""
    return data.get(key, default) if isinstance(data, dict) else default