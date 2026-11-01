import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_payload(data: Any, required_keys: list) -> bool:
    """Validates dictionary structure and presence of required fields."""
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dict, got {type(data).__name__}")

    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required field: {key}")
        if data[key] is None:
            raise ValidationError(f"Field cannot be null: {key}")
            
    return True

def process_main_loop(items: list, schema: list):
    """Main processing loop with integrated input validation."""
    for index, item in enumerate(items):
        try:
            if validate_payload(item, schema):
                logger.info(f"Processing item {index}")
                # Execute core business logic here
        except ValidationError as e:
            logger.error(f"Skipping item {index}: {e}")
            continue
        except Exception as e:
            logger.critical(f"Unexpected error at {index}: {e}")
            raise