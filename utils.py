import logging

# Configure basic logging for the utility module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary."""
    if not isinstance(data, dict):
        raise ValueError(f"Expected dict, got {type(data).__name__}")
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    return True

def process_data(data_stream):
    """Main processing loop with integrated input validation."""
    for item in data_stream:
        try:
            validate_input(item)
            
            # Simulate core processing logic
            result = item.get("value", 0) * 2
            logger.info(f"Processed item: {result}")
            
        except (ValueError, TypeError) as e:
            logger.error(f"Validation failed for input {item}: {e}")
            continue

if __name__ == "__main__":
    # Example usage for the utility loop
    sample_stream = [{"value": 10}, {}, "invalid_input", {"value": 5}]
    process_data(sample_stream)