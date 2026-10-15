class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_payload(data: dict, required_keys: list):
    """Validates that all required keys are present and non-empty.

    Args:
        data: The dictionary to validate.
        required_keys: List of keys that must exist in data.

    Raises:
        ValidationError: If any key is missing or invalid.
    """
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a dictionary")

    for key in required_keys:
        if key not in data or data[key] is None:
            raise ValidationError(f"Missing required field: {key}")

def process_main_loop(items: list):
    """Main processing loop with integrated input validation."""
    required = ['id', 'value']
    results = []

    for item in items:
        try:
            validate_payload(item, required)
            # Processing logic continues here
            results.append(item['value'] * 2)
        except ValidationError as e:
            print(f"Skipping invalid item: {e}")
            continue
    
    return results