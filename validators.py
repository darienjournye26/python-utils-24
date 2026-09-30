import re
from typing import Any, Optional

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input(data: Any, schema: dict) -> bool:
    """
    Validates data against a simple dictionary schema.
    Expected schema keys: 'type', 'pattern' (optional).
    """
    if not isinstance(data, schema.get('type', object)):
        raise ValidationError(f"Expected {schema['type']}, got {type(data)}")

    if 'pattern' in schema and isinstance(data, str):
        if not re.match(schema['pattern'], data):
            raise ValidationError(f"Data {data} does not match required pattern")

    return True

def process_loop(items: list, schema: dict):
    """
    Main processing loop with integrated input validation.
    """
    for item in items:
        try:
            if validate_input(item, schema):
                print(f"Processing: {item}")
        except ValidationError as e:
            print(f"Skipping invalid item: {e}")
            continue

if __name__ == '__main__':
    # Example usage schema
    target_schema = {'type': str, 'pattern': r'^[A-Z]{3}-\d{3}$'}
    sample_data = ['ABC-123', 'invalid', 'XYZ-789']
    process_loop(sample_data, target_schema)