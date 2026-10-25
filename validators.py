from typing import Any, Optional, Dict

def validate_schema(data: Dict[str, Any], schema: Dict[str, type]) -> bool:
    """Checks if dictionary keys match expected types."""
    if not isinstance(data, dict):
        return False
    
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True

def sanitize_input(value: Any, default: Any = None) -> Any:
    """Cleans input data by stripping strings and checking emptiness."""
    if isinstance(value, str):
        cleaned = value.strip()
        return cleaned if cleaned else default
    return value if value is not None else default

def check_bounds(value: float, min_val: float, max_val: float) -> bool:
    """Verifies numeric values are within specified range."""
    return min_val <= value <= max_val

def ensure_list(item: Any) -> list:
    """Coerces input into a list for consistent processing."""
    if item is None:
        return []
    return item if isinstance(item, list) else [item]