import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data: dict) -> bool:
    """Ensures dictionary contains required keys with valid types."""
    required = {'id': int, 'payload': str}
    for key, expected_type in required.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True

def process_stream(data_stream: list):
    """Main processing loop with integrated input validation."""
    for entry in data_stream:
        try:
            if not isinstance(entry, dict):
                raise ValueError(f"Invalid format: expected dict, got {type(entry)}")
            
            if not validate_input(entry):
                logger.warning(f"Validation failed for entry: {entry}")
                continue
            
            # Simulate core business logic execution
            result = entry['payload'].upper()
            logger.info(f"Processed id {entry['id']}: {result}")
            
        except (ValueError, TypeError) as e:
            logger.error(f"Processing error: {e}")
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}")

if __name__ == '__main__':
    sample_data = [{'id': 1, 'payload': 'hello'}, {'id': 'wrong', 'payload': 123}, {'id': 2, 'payload': 'world'}]
    process_stream(sample_data)