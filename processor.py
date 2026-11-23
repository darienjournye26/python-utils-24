import logging

logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary."""
    if not isinstance(data, dict):
        raise ValueError(f"Expected dict, got {type(data).__name__}")
    if not data:
        raise ValueError("Empty input data received")
    return True

def process_stream(data_stream):
    """Main processing loop with input validation."""
    results = []
    for entry in data_stream:
        try:
            if validate_input(entry):
                # Simulate data transformation
                processed = {k: str(v).strip() for k, v in entry.items()}
                results.append(processed)
        except (ValueError, TypeError) as e:
            logger.error(f"Skipping invalid entry: {e}")
            continue
    return results

if __name__ == "__main__":
    sample_data = [{"id": 1, "val": "  test  "}, {}, "invalid", {"id": 2, "val": "data"}]
    output = process_stream(sample_data)
    print(f"Processed {len(output)} records.")