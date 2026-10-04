import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary."""
    if not isinstance(data, dict) or not data:
        raise ValueError("input must be a non-empty dictionary")
    return True

def process_stream(data_stream):
    """
    Main processing loop for utility operations with validation.
    """
    results = []
    for entry in data_stream:
        try:
            validate_input(entry)
            # Perform business logic here
            processed_val = entry.get('value', 0) * 2
            results.append(processed_val)
            logger.info(f"Processed: {processed_val}")
        except (ValueError, TypeError) as e:
            logger.error(f"Skipping invalid entry {entry}: {e}")
            continue
    return results

if __name__ == "__main__":
    sample_data = [{'value': 10}, "invalid", {'value': 20}, {}]
    output = process_stream(sample_data)
    print(f"Final processing result: {output}")