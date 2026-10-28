import logging
from typing import Any, Dict, List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataProcessor:
    """Processes data batches with input validation in the main loop."""

    def __init__(self, required_keys: Optional[List[str]] = None) -> None:
        self.required_keys = required_keys or ["id", "payload", "timestamp"]
        self.processed_count = 0
        self.failed_count = 0

    def validate_item(self, item: Any) -> Dict[str, Any]:
        """Validate the structure and types of a single item."""
        if not isinstance(item, dict):
            raise ValueError(f"Expected dict, got {type(item).__name__}")

        missing = [k for k in self.required_keys if k not in item]
        if missing:
            raise ValueError(f"Missing required keys: {', '.join(missing)}")

        if not isinstance(item["id"], (int, str)) or not str(item["id"]).strip():
            raise ValueError("Key 'id' must be a non-empty string or integer")

        if not isinstance(item["timestamp"], (int, float)) or item["timestamp"] <= 0:
            raise ValueError("Key 'timestamp' must be a positive number")

        return item

    def process_batch(self, items: List[Any]) -> List[Dict[str, Any]]:
        """Main loop validating and converting input payload records."""
        results = []

        for index, item in enumerate(items):
            try:
                valid_item = self.validate_item(item)
                processed = {
                    "id": str(valid_item["id"]),
                    "payload": str(valid_item["payload"]).strip(),
                    "processed_at": valid_item["timestamp"],
                    "status": "completed",
                }
                results.append(processed)
                self.processed_count += 1
            except ValueError as err:
                logger.warning("Skipping invalid item at index %d: %s", index, err)
                self.failed_count += 1
            except Exception as err:
                logger.error("Unexpected error at index %d: %s", index, err)
                self.failed_count += 1

        return results
