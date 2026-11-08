import logging

# Configure logger for module tracking
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary."""
    if not isinstance(data, dict):
        return False
    if not data:
        return False
    return True

def process_main_loop(items):
    """Main processing loop with data validation."""
    for index, item in enumerate(items):
        try:
            # Validate current iteration input
            if not validate_input(item):
                logger.warning(f"Skipping invalid input at index {index}")
                continue
            
            # Execute primary business logic
            result = item.get("value", 0) * 2
            logger.info(f"Processed item {index}: result {result}")
            
        except Exception as e:
            logger.error(f"Unexpected error processing item {index}: {e}")

if __name__ == '__main__':
    # Example payload execution
    sample_data = [{"value": 10}, {}, "invalid_type", {"value": 20}]
    process_main_loop(sample_data)