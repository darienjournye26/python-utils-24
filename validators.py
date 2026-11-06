import re
from typing import Any, Optional

# regex patterns for validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class ValidationError(Exception):
    """Custom exception for validation failures."""
    pass

def validate_email(email: str) -> bool:
    """Checks if provided string is a valid email address."""
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))

def validate_range(value: Any, min_val: float, max_val: float) -> bool:
    """Ensures numeric value stays within defined boundaries."""
    try:
        return min_val <= float(value) <= max_val
    except (ValueError, TypeError):
        return False

def clean_string(value: Any, default: str = "") -> str:
    """Strips whitespace and returns default if input is invalid."""
    if not isinstance(value, str):
        return default
    return value.strip()

def validate_required(value: Any) -> bool:
    """Checks if value is not empty or None."""
    if value is None:
        return False
    if isinstance(value, str):
        return len(value.strip()) > 0
    return True