import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Validates standard email format using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_length(value: str, min_len: int, max_len: int) -> bool:
    """Checks string length within bounds."""
    return min_len <= len(value) <= max_len

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Checks integer range boundaries."""
    return min_val <= value <= max_val

def sanitize_input(value: Any) -> str:
    """Converts input to stripped string for processing."""
    if value is None:
        return ""
    return str(value).strip()

def validate_identifier(name: str) -> bool:
    """Checks for alphanumeric identifier format."""
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name))