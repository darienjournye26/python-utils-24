from typing import Any, Optional, Union

def validate_email(email: str) -> bool:
    """
    Validates the format of an email address.

    Args:
        email: The email string to validate.

    Returns:
        True if the email contains an @ symbol and a period, False otherwise.
    """
    return bool(email and '@' in email and '.' in email.split('@')[-1])

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """
    Checks if a number falls within a specific range inclusive.

    Args:
        value: The number to check.
        min_val: The inclusive lower bound.
        max_val: The inclusive upper bound.

    Returns:
        True if within range, False otherwise.
    """
    return min_val <= value <= max_val

def validate_not_empty(data: Optional[str]) -> bool:
    """
    Checks if a string is neither None nor empty.

    Args:
        data: The string to validate.

    Returns:
        True if string contains characters, False otherwise.
    """
    return isinstance(data, str) and len(data.strip()) > 0

def validate_type(obj: Any, expected_type: type) -> bool:
    """
    Verifies that an object is an instance of a specific type.

    Args:
        obj: The object to inspect.
        expected_type: The type class to check against.

    Returns:
        True if match, False otherwise.
    """
    return isinstance(obj, expected_type)