import re
from typing import Any, Dict, Optional

def validate_payload(data: Dict[str, Any]) -> bool:
    """
    Validates input schema and data integrity for main loop.
    Ensures required fields exist and types match requirements.
    """
    required_fields = {'task_id': int, 'payload': str}
    
    # Validate dictionary structure and keys
    if not isinstance(data, dict):
        return False
        
    for field, expected_type in required_fields.items():
        if field not in data or not isinstance(data[field], expected_type):
            return False
            
    # Validate payload format using regex pattern
    # Ensures alphanumeric content with minimal length constraints
    if not re.match(r'^[a-zA-Z0-9_\-]{4,64}$', data['payload']):
        return False
        
    return True

def sanitize_input(value: str) -> str:
    """
    Removes potentially dangerous characters from string input.
    """
    return re.sub(r'[^a-zA-Z0-9_\-]', '', value)

def get_validated_int(value: Any, default: int = 0) -> int:
    """
    Coerces input to integer with fallback for safety.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default