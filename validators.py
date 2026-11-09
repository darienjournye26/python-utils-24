"""General input validation utilities for common data types."""

import re
from typing import Any, Dict, List, Optional, Union


def is_valid_email(email: str) -> bool:
    """Validate email address format using standard pattern."""
    if not isinstance(email, str) or not email:
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email.strip()) is not None


def is_valid_url(url: str) -> bool:
    """Check if the provided string is a valid HTTP/HTTPS URL."""
    if not isinstance(url, str) or not url:
        return False
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$"
    return re.match(pattern, url.strip()) is not None


def validate_number_range(
    value: Union[int, float],
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
) -> bool:
    """Check if a numeric value falls within an optional inclusive range."""
    if not isinstance(value, (int, float)):
        return False
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True


def validate_required_keys(data: Dict[str, Any], required_keys: List[str]) -> List[str]:
    """Return a list of missing keys from a dictionary based on required keys list."""
    if not isinstance(data, dict):
        return list(required_keys)
    return [key for key in required_keys if key not in data or data[key] is None]


def sanitize_string(text: str, max_length: Optional[int] = None) -> str:
    """Clean string input by stripping whitespace and enforcing max length."""
    if not isinstance(text, str):
        return ""
    cleaned = text.strip()
    if max_length and len(cleaned) > max_length:
        return cleaned[:max_length]
    return cleaned
