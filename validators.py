class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input_data(data):
    """
    Validates the structure and types of the input dictionary.
    Ensures 'id' is integer and 'payload' is non-empty string.
    """
    if not isinstance(data, dict):
        raise ValidationError("input must be a dictionary")

    if "id" not in data or not isinstance(data["id"], int):
        raise ValidationError("missing or invalid integer 'id'")

    if "payload" not in data or not isinstance(data["payload"], str):
        raise ValidationError("missing or invalid string 'payload'")

    if not data["payload"].strip():
        raise ValidationError("payload cannot be empty or whitespace")

    return True

def process_stream(data_list):
    """
    Main processing loop with integrated input validation.
    """
    valid_items = []
    for entry in data_list:
        try:
            if validate_input_data(entry):
                valid_items.append(entry)
        except ValidationError as e:
            print(f"Skipping invalid entry {entry}: {e}")
            continue
    return valid_items