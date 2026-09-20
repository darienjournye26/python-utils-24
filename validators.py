from typing import Any, Dict, Optional

def validate_schema(data: Any, schema: Dict[str, type], strict: bool = False) -> bool:
    """Validates dictionary structure against a type schema."""
    if not isinstance(data, dict):
        return False

    if strict and set(data.keys()) != set(schema.keys()):
        return False

    for key, expected_type in schema.items():
        value = data.get(key)
        if value is None or not isinstance(value, expected_type):
            return False

    return True

def sanitize_input(data: str, max_length: int = 255) -> str:
    """Cleans strings for general input handling."""
    if not isinstance(data, str):
        return ""
    return data.strip()[:max_length]

def is_non_empty(data: Optional[Any]) -> bool:
    """Checks if container or string has content."""
    if data is None:
        return False
    if isinstance(data, (str, list, dict, set)):
        return len(data) > 0
    return True