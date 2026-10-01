import logging
from typing import Any, Dict, Generator, List, Tuple

logger = logging.getLogger("python-utils-24.processor")


class BatchProcessor:
    """Processes batch inputs with strict validation on each record."""

    def __init__(self, required_keys: List[str] = None):
        self.required_keys = required_keys or ["id", "action", "payload"]

    def validate_record(self, record: Any) -> Tuple[bool, str]:
        """Validates a single record structure and types."""
        if not isinstance(record, dict):
            return False, "Record must be a dictionary"

        for key in self.required_keys:
            if key not in record:
                return False, f"Missing required key: '{key}'"

        if not isinstance(record["id"], (int, str)) or not str(record["id"]).strip():
            return False, "Key 'id' must be a non-empty string or integer"

        if not isinstance(record["payload"], dict):
            return False, "Key 'payload' must be a dictionary"

        return True, ""

    def process_queue(self, items: List[Any]) -> Generator[Dict[str, Any], None, None]:
        """Main processing loop with input validation safety rails."""
        for index, item in enumerate(items):
            is_valid, error_msg = self.validate_record(item)
            if not is_valid:
                logger.warning(
                    f"Skipping invalid item at index {index}: {error_msg}"
                )
                continue

            try:
                # Standardize action key and extract payload keys for downstream use
                processed_payload = {
                    f"processed_{k}": v for k, v in item["payload"].items()
                }
                yield {
                    "id": item["id"],
                    "action": str(item["action"]).lower().strip(),
                    "payload": processed_payload,
                    "status": "success",
                }
            except Exception as exc:
                logger.error(
                    f"Processing failure for item {item.get('id', index)}: {exc}"
                )
