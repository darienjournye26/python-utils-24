import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)


class BatchProcessor:
    """Processes batches of incoming data records with input validation."""

    def __init__(self, required_keys: List[str]):
        self.required_keys = required_keys

    def validate_record(self, record: Any) -> Tuple[bool, str]:
        """Validate structure and content of a single input record."""
        if not isinstance(record, dict):
            return False, "Record must be a dictionary"

        for key in self.required_keys:
            if key not in record:
                return False, f"Missing required field: '{key}'"
            if record[key] is None:
                return False, f"Field '{key}' cannot be None"

        if "age" in record and isinstance(record["age"], (int, float)):
            if record["age"] < 0 or record["age"] > 150:
                return False, "Field 'age' out of valid range (0-150)"

        return True, ""

    def process_batch(self, items: List[Any]) -> Dict[str, Any]:
        """Process a list of items with validation in the main loop."""
        processed = []
        skipped = []

        for index, item in enumerate(items):
            is_valid, error_msg = self.validate_record(item)
            if not is_valid:
                logger.warning(f"Item at index {index} rejected: {error_msg}")
                skipped.append({"index": index, "item": item, "reason": error_msg})
                continue

            # Transform or process valid item
            processed_item = dict(item)
            processed_item["status"] = "processed"
            processed.append(processed_item)

        return {
            "total": len(items),
            "processed_count": len(processed),
            "skipped_count": len(skipped),
            "processed": processed,
            "skipped": skipped,
        }
