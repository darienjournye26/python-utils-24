import re
from typing import Any, Optional

def is_email(value: str) -> bool:
    """Validate RFC 5322 compliant email string structure."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, value))

def is_not_empty(value: Any) -> bool:
    """Check if input is not None and not an empty container."""
    if value is None:
        return False
    if isinstance(value, (str, list, dict, set, tuple)):
        return len(value) > 0
    return True

def validate_range(value: float, min_val: float, max_val: float) -> bool:
    """Verify numeric value falls within inclusive boundaries."""
    return min_val <= value <= max_val

def parse_int(value: Any, default: Optional[int] = None) -> Optional[int]:
    """Safely attempt string to integer conversion."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def is_alphanumeric(value: str) -> bool:
    """Check if string contains only alphanumeric characters."""
    return str(value).isalnum()