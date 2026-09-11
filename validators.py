import re
from typing import Any, Optional

class DataValidator:
    """Utility class for common data format validation."""

    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    @staticmethod
    def is_email(value: Any) -> bool:
        """Check if string is a valid email address."""
        if not isinstance(value, str):
            return False
        return bool(DataValidator.EMAIL_REGEX.match(value))

    @staticmethod
    def is_non_empty_string(value: Any) -> bool:
        """Check if input is a non-empty string."""
        return isinstance(value, str) and len(value.strip()) > 0

    @staticmethod
    def validate_range(value: int, min_val: int, max_val: int) -> bool:
        """Verify integer is within specified boundaries."""
        return isinstance(value, int) and min_val <= value <= max_val

def validate_input_schema(data: dict, schema: dict) -> bool:
    """Basic schema validation for dictionary inputs."""
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True