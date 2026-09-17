import logging
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("processor")

class BatchProcessor:
    """Processes batches of input data with robust validation."""

    def __init__(self, required_keys: List[str]):
        self.required_keys = required_keys

    def validate_payload(self, payload: Any) -> Dict[str, Any]:
        """Validates that payload is a dictionary and contains all required keys."""
        if not isinstance(payload, dict):
            raise TypeError(f"Payload must be a dictionary, got {type(payload).__name__}")

        for key in self.required_keys:
            if key not in payload:
                raise KeyError(f"Missing required validation key: '{key}'")

        for key, val in payload.items():
            if val is None or (isinstance(val, (str, list, dict)) and not val):
                raise ValueError(f"Value for field '{key}' cannot be empty or null")

        return payload

    def process_batch(self, items: List[Any]) -> List[Dict[str, Any]]:
        """Iterates through items, applying validation in the main loop."""
        processed_items = []

        for index, item in enumerate(items):
            try:
                logger.info("Processing item at index %d", index)
                validated_item = self.validate_payload(item)
                validated_item["processed"] = True
                processed_items.append(validated_item)
            except (TypeError, KeyError, ValueError) as err:
                logger.error("Validation failed for item %d: %s", index, str(err))
                continue

        return processed_items