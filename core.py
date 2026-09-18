import logging

def process_data(payload):
    """Validate and process input data within the main loop."""
    if not isinstance(payload, dict):
        raise ValueError(f"Expected dict, got {type(payload).__name__}")
    
    required_keys = {'id', 'value'}
    if not required_keys.issubset(payload.keys()):
        missing = required_keys - payload.keys()
        raise KeyError(f"Missing required keys: {missing}")
        
    if not isinstance(payload['value'], (int, float)):
        raise TypeError("Value must be a number")

    # Process the validated input
    return f"Processed ID {payload['id']}: {payload['value'] * 2}"

def main_loop(data_stream):
    """Main execution loop with input validation."""
    logger = logging.getLogger(__name__)
    for entry in data_stream:
        try:
            result = process_data(entry)
            print(result)
        except (ValueError, KeyError, TypeError) as e:
            logger.error(f"Skipping invalid entry {entry}: {e}")
            continue

if __name__ == "__main__":
    data = [{'id': 1, 'value': 10}, {'id': 2, 'value': 'invalid'}, {'id': 3, 'value': 20}]
    main_loop(data)