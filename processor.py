import logging

# Configure basic logging for the processor
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_data(items):
    """
    Processes a list of items with mandatory input validation.
    """
    for index, item in enumerate(items):
        try:
            # Validate data integrity
            if not isinstance(item, dict):
                raise ValueError(f"Item at index {index} is not a dictionary")
            
            if 'id' not in item or 'value' not in item:
                raise KeyError(f"Item {index} missing required keys: id, value")
            
            if not isinstance(item['value'], (int, float)):
                raise TypeError(f"Value at index {index} must be numeric")

            # Simulate core processing logic
            result = item['value'] * 2
            logger.info(f"Processed item {item['id']}: result {result}")
            
        except (ValueError, KeyError, TypeError) as e:
            logger.error(f"Validation failure at index {index}: {e}")
            continue

if __name__ == "__main__":
    data_batch = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 'invalid'},
        {'id': 3, 'value': 25},
        "bad_input_type"
    ]
    process_data(data_batch)