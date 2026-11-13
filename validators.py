import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def validate_payload(data: Any) -> bool:
    """
    Validates that the input data is a dictionary
    containing the required 'id' and 'value' keys.
    """
    if not isinstance(data, dict):
        logger.error("Invalid input type: expected dict")
        return False

    required_keys = {'id', 'value'}
    if not required_keys.issubset(data.keys()):
        logger.error(f"Missing keys in payload: {required_keys - data.keys()}")
        return False

    if not isinstance(data.get('id'), int):
        logger.error("Invalid 'id' type: expected int")
        return False

    return True

def sanitize_input(value: Any) -> Optional[str]:
    """
    Ensures input values are strings and cleaned
    of potential whitespace issues.
    """
    try:
        return str(value).strip()
    except (ValueError, TypeError):
        logger.warning(f"Failed to sanitize value: {value}")
        return None