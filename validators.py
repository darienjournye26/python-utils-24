from typing import Any, Union, Optional

def validate_email(email: str) -> bool:
    """Check if string follows standard email format."""
    if not isinstance(email, str) or "@" not in email:
        return False
    parts = email.split("@")
    return len(parts) == 2 and all(parts)

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Verify number is within inclusive bounds."""
    return min_val <= value <= max_val

def validate_non_empty(value: Optional[str]) -> bool:
    """Ensure string is provided and not whitespace only."""
    if value is None:
        return False
    return bool(value.strip())

def sanitize_input(value: Any) -> str:
    """Convert any input to stripped string."""
    if value is None:
        return ""
    return str(value).strip()