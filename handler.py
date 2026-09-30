"""Data processing handler with input validation."""

from typing import Any, Dict, List, Tuple


def validate_record(record: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate a single data record before processing.
    
    Returns a tuple of (is_valid, error_message).
    """
    if not isinstance(record, dict):
        return False, "Record must be a dictionary"
    
    required_fields = ["id", "action", "payload"]
    for field in required_fields:
        if field not in record:
            return False, f"Missing required field: {field}"
            
    if not isinstance(record["id"], (int, str)) or not str(record["id"]).strip():
        return False, "Field 'id' must be a non-empty string or integer"
        
    if not isinstance(record["payload"], dict):
        return False, "Field 'payload' must be a dictionary"
        
    return True, ""


def process_batch(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Process a batch of records with strict input validation in the main loop."""
    results: Dict[str, List[Dict[str, Any]]] = {"successful": [], "failed": []}

    for index, record in enumerate(records):
        # Validate record structure and types before processing
        is_valid, error_msg = validate_record(record)
        if not is_valid:
            results["failed"].append({
                "index": index,
                "record": record,
                "reason": error_msg
            })
            continue

        # Process valid record
        record_id = record["id"]
        action_type = record["action"]
        
        results["successful"].append({
            "id": record_id,
            "status": "processed",
            "action": action_type
        })

    return results
