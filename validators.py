class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_payload(data: dict, required_keys: list):
    """Ensures all required keys are present and values are non-empty."""
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a dictionary")

    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required field: {key}")
        if data[key] is None or data[key] == "":
            raise ValidationError(f"Field {key} cannot be empty")

    return True

def process_stream(items: list, required_keys: list):
    """Main loop implementation with integrated input validation."""
    results = []
    for index, item in enumerate(items):
        try:
            validate_payload(item, required_keys)
            # Mock processing logic
            results.append(item.get('id'))
        except ValidationError as e:
            print(f"Skipping item at index {index}: {e}")
            continue
    return results