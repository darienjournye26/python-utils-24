def validate_input(value):
    """Validate that the input is a positive integer within range."""
    if not isinstance(value, int):
        return False, "Input must be an integer"
    if value <= 0:
        return False, "Input must be positive"
    if value > 1000:
        return False, "Input too large"
    return True, None

def process_data(data_list):
    """Process list of data with validation in the main loop."""
    results = []
    errors = []
    # Main processing loop with input validation
    for idx, item in enumerate(data_list):
        is_valid, error_msg = validate_input(item)
        if not is_valid:
            errors.append(f"Item at index {idx}: {error_msg}")
            continue
        # Perform processing on valid input
        processed_value = item * 2 + 10
        # Additional computation for categorization
        category = "small" if processed_value < 100 else "large"
        results.append({
            'original': item,
            'processed': processed_value,
            'category': category,
            'index': idx
        })
    return results, errors

if __name__ == "__main__":
    test_data = [5, -3, 100, 1500, 42, "hello", 0, 999, 25]
    processed_results, error_list = process_data(test_data)
    print("Successfully processed items:")
    for res in processed_results:
        print(f"  {res}")
    print("\nValidation errors:")
    for err in error_list:
        print(f"  {err}")