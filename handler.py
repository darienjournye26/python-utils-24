import logging
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Raised when payload validation fails."""
    pass


def validate_payload(data: Dict[str, Any]) -> None:
    """Validate input payload structure and required fields."""
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a dictionary")

    required_keys = ["id", "action", "timestamp"]
    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required key: '{key}'")
        if data[key] is None:
            raise ValidationError(f"Key '{key}' cannot be None")

    if not isinstance(data["id"], (int, str)) or str(data["id"]).strip() == "":
        raise ValidationError("Invalid or empty 'id' field")

    if not isinstance(data["action"], str) or data["action"].strip() == "":
        raise ValidationError("Action must be a non-empty string")


def process_records(records: List[Dict[str, Any]]) -> Dict[str, int]:
    """Main processing loop with input validation for incoming records."""
    stats = {"processed": 0, "failed": 0}

    for idx, record in enumerate(records):
        try:
            validate_payload(record)
            logger.info("Processing record ID: %s", record["id"])
            stats["processed"] += 1
        except ValidationError as err:
            logger.warning("Validation failed at index %d: %s", idx, err)
            stats["failed"] += 1
        except Exception as err:
            logger.error("Unexpected error at index %d: %s", idx, err)
            stats["failed"] += 1

    return stats
