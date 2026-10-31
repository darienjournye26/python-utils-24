import logging

# Configure basic logging for the processor
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_input_stream(data_stream):
    """Processes stream and validates inputs before logic."""
    for item in data_stream:
        try:
            # Validate mandatory keys in the input dictionary
            if not isinstance(item, dict):
                raise ValueError(f"Invalid type: expected dict, got {type(item).__name__}")
            
            if "id" not in item or not isinstance(item["id"], int):
                raise ValueError("Missing or invalid key 'id'")
            
            if "payload" not in item:
                raise ValueError("Missing mandatory key 'payload'")

            # Execute main business logic
            result = perform_calculation(item["payload"])
            logger.info(f"Processed item {item['id']}: {result}")

        except (ValueError, TypeError) as e:
            logger.error(f"Validation failure: {e}")
            continue

def perform_calculation(value):
    """Performs simple numeric processing."""
    if not isinstance(value, (int, float)):
        raise TypeError("Payload must be numeric")
    return value * 2

if __name__ == "__main__":
    sample_data = [{"id": 1, "payload": 10}, {"id": 2, "payload": "invalid"}, "bad_item"]
    process_input_stream(sample_data)