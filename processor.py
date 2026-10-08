import logging
from typing import Any, Dict, List, Tuple

# Configure a basic logger for this module
logger = logging.getLogger("processor")


class ProcessingError(Exception):
    """Exception raised when a record fails validation or processing."""
    pass


class BatchProcessor:
    """Processes batches of input data with robust input validation."""

    def __init__(self, required_fields: List[str]) -> None:
        self.required_fields = required_fields

    def validate_record(self, record: Dict[str, Any]) -> None:
        """Validates a single data record against schema requirements."""
        if not isinstance(record, dict):
            raise ProcessingError("Record must be a dictionary")

        for field in self.required_fields:
            if field not in record:
                raise ProcessingError(f"Missing required field: '{field}'")

            value = record[field]
            if value is None:
                raise ProcessingError(f"Field '{field}' cannot be None")

            if isinstance(value, str) and not value.strip():
                raise ProcessingError(f"Field '{field}' cannot be an empty string")

            if isinstance(value, (int, float)) and value < 0:
                raise ProcessingError(f"Field '{field}' cannot be negative")

    def process_batch(
        self, batch: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Processes a batch of records, separating successful runs from failures."""
        successful_records = []
        failed_records = []

        for index, record in enumerate(batch):
            try:
                # Input validation step
                self.validate_record(record)

                # Process the valid record
                processed_record = record.copy()
                processed_record["processed"] = True
                successful_records.append(processed_record)

            except ProcessingError as err:
                logger.warning("Validation failed at index %d: %s", index, str(err))
                failed_records.append({"index": index, "data": record, "error": str(err)})
            except Exception as err:
                logger.error("Unexpected error at index %d: %s", index, str(err))
                failed_records.append({"index": index, "data": record, "error": "Unexpected error"})

        return successful_records, failed_records