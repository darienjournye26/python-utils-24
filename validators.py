from typing import Any, Optional, Union

def validate_email(email: str) -> bool:
    """Verify if a string follows standard email format."""
    if not isinstance(email, str) or "@" not in email:
        return False
    return email.count("@") == 1 and "." in email.split("@")[1]

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Check if numeric value resides within defined boundaries."""
    return min_val <= value <= max_val

def sanitize_input(data: Any, default: Optional[Any] = None) -> Any:
    """Clean input data or return provided default value."""
    if data is None or data == "":
        return default
    return str(data).strip()

def is_truthy(value: Any) -> bool:
    """Determine boolean status of various input types."""
    normalized = str(value).lower()
    return normalized in ("true", "1", "t", "y", "yes")