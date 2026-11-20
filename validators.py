import re
from typing import Any, Optional

def is_valid_email(email: str) -> bool:
    """Validates email string format using regex."""
    if not email or not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def is_non_empty_string(value: Any) -> bool:
    """Checks if value is a string and contains non-whitespace characters."""
    return isinstance(value, str) and bool(value.strip())

def is_positive_int(value: Any) -> bool:
    """Checks if value is an integer greater than zero."""
    return isinstance(value, int) and not isinstance(value, bool) and value > 0

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Checks if an integer falls within a specific inclusive range."""
    return isinstance(value, int) and min_val <= value <= max_val

def clean_input(value: Any) -> Optional[str]:
    """Returns stripped string or None if input is invalid."""
    if isinstance(value, str):
        return value.strip() if value.strip() else None
    return None