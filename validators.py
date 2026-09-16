from typing import Any, Optional, Union

def validate_email(email: str) -> bool:
    """Validate the format of an email address string."""
    if not isinstance(email, str) or "@" not in email:
        return False
    return email.count("@") == 1 and "." in email.split("@")[1]

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Check if a numeric value falls within inclusive range."""
    return min_val <= value <= max_val

def validate_not_empty(data: Any) -> bool:
    """Check if the input object contains data elements."""
    if data is None:
        return False
    if isinstance(data, (str, list, dict, set)):
        return len(data) > 0
    return True

def sanitize_input(value: Optional[str]) -> str:
    """Remove whitespace and return empty string if None."""
    if value is None:
        return ""
    return str(value).strip()

def validate_type(value: Any, expected_type: type) -> bool:
    """Check if a value matches the provided type."""
    return isinstance(value, expected_type)