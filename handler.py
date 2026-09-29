import logging

def validate_input(data):
    """Ensures data is a non-empty dictionary."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    return True

def process_payload(payload):
    """Process individual data packets."""
    logging.info(f"Processing: {payload.get('id', 'unknown')}")
    return True

def run_processor(data_stream):
    """Main processing loop with input validation."""
    logging.basicConfig(level=logging.INFO)
    
    for item in data_stream:
        try:
            validate_input(item)
            process_payload(item)
        except (ValueError, TypeError) as e:
            logging.error(f"Validation failed for item {item}: {e}")
            continue

if __name__ == "__main__":
    sample_data = [
        {"id": 1, "val": "data1"},
        {},
        "invalid_type",
        {"id": 2, "val": "data2"}
    ]
    run_processor(sample_data)