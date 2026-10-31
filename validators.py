import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def validate_input(data: Any, expected_type: type) -> Optional[Any]:
    """Validates input data type and handles edge cases."""
    try:
        if data is None:
            logger.error("Received null input data")
            return None
        
        if not isinstance(data, expected_type):
            logger.warning(f"Type mismatch: expected {expected_type}, got {type(data)}")
            return None
            
        return data
    except Exception as e:
        logger.critical(f"Unexpected validation error: {str(e)}")
        return None

def sanitize_string(value: Any) -> str:
    """Ensures input is a clean string or returns empty."""
    if not isinstance(value, str):
        return ""
    
    stripped = value.strip()
    return stripped if stripped else ""

def check_bounds(value: float, min_val: float, max_val: float) -> bool:
    """Verifies numeric values within defined inclusive range."""
    try:
        return min_val <= float(value) <= max_val
    except (ValueError, TypeError):
        logger.error(f"Invalid range input: {value}")
        return False