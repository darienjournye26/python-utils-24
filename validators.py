"""Data validation helpers with robust edge case handling."""

import re
from typing import Any, Optional


def validate_email(email: Any) -> bool:
    """Validate email format with type and edge case checks."""
    if not isinstance(email, str):
        return False
    
    email = email.strip()
    if not email or len(email) > 254:
        return False
        
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_numeric_range(
    value: Any, 
    min_val: Optional[float] = None, 
    max_val: Optional[float] = None
) -> bool:
    """Safely validate numeric bounds, handling string numbers and invalid inputs."""
    if value is None or isinstance(value, bool):
        return False

    try:
        num = float(value)
    except (ValueError, TypeError, OverflowError):
        return False

    if min_val is not None and num < min_val:
        return False
    if max_val is not None and num > max_val:
        return False

    return True


def validate_dict_depth(data: Any, max_depth: int = 5, _current_depth: int = 1) -> bool:
    """Check nested dictionary depth to prevent recursion overflow errors."""
    if not isinstance(data, dict):
        return True
        
    if _current_depth > max_depth:
        return False

    for value in data.values():
        if isinstance(value, dict):
            if not validate_dict_depth(value, max_depth, _current_depth + 1):
                return False
        elif isinstance(value, (list, tuple, set)):
            for item in value:
                if isinstance(item, dict):
                    if not validate_dict_depth(item, max_depth, _current_depth + 1):
                        return False

    return True
