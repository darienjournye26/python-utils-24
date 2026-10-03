"""Data processing module with input validation mechanisms."""

import logging
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


def validate_item(item: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """Validate input payload structure and field values."""
    if not isinstance(item, dict):
        return False, "Item must be a dictionary"

    required_fields = ["id", "action", "value"]
    for field in required_fields:
        if field not in item:
            return False, f"Missing required field: {field}"

    if not isinstance(item["id"], (int, str)) or not str(item["id"]).strip():
        return False, "Field 'id' must be a non-empty string or integer"

    if not isinstance(item["value"], (int, float)) or item["value"] < 0:
        return False, "Field 'value' must be a non-negative number"

    return True, None


def process_batch(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Main processing loop with input validation for item batches."""
    processed_results = []

    for index, raw_item in enumerate(items):
        is_valid, error_msg = validate_item(raw_item)
        if not is_valid:
            logger.warning("Skipping invalid item at index %d: %s", index, error_msg)
            continue

        # Process valid item safely after validation
        result = {
            "id": raw_item["id"],
            "action": str(raw_item["action"]).upper(),
            "processed_value": round(float(raw_item["value"]) * 1.15, 2),
            "status": "success",
        }
        processed_results.append(result)

    return processed_results
