from typing import Any, Dict, List, Optional


class ValidationError(Exception):
    """Custom exception raised when input record validation fails."""
    pass


def validate_record(record: Any) -> Dict[str, Any]:
    """Validate raw input record structure and data types."""
    if not isinstance(record, dict):
        raise ValidationError(f"Expected dict record, got {type(record).__name__}")
    
    if "id" not in record or not isinstance(record["id"], (int, str)):
        raise ValidationError("Missing or invalid 'id' field")
    
    if "value" not in record:
        raise ValidationError("Missing required 'value' field")
    
    try:
        record["value"] = float(record["value"])
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid numeric value: {record.get('value')}")
    
    return record


def process_batch(items: List[Any]) -> List[Dict[str, Any]]:
    """Process a batch of records with input validation in the main loop."""
    processed_results: List[Dict[str, Any]] = []
    
    for index, raw_item in enumerate(items):
        try:
            # Validate input before attempting business logic
            valid_item = validate_record(raw_item)
            
            # Processing logic for valid items
            result = {
                "id": valid_item["id"],
                "processed_value": round(valid_item["value"] * 1.15, 2),
                "status": "success"
            }
            processed_results.append(result)
            
        except ValidationError as err:
            # Record invalid input details without interrupting batch processing
            processed_results.append({
                "index": index,
                "error": str(err),
                "status": "skipped"
            })
            
    return processed_results


if __name__ == "__main__":
    sample_data = [
        {"id": 101, "value": "42.5"},
        {"id": 102},  # missing value
        "not_a_dict",  # invalid type
        {"id": 103, "value": "invalid_num"}
    ]
    output = process_batch(sample_data)
    print(f"Processed {len(output)} records.")
