from typing import Any, Dict, List, Tuple, Type


class ValidationError(Exception):
    """Raised when input data fails validation rules."""
    pass


class RecordValidator:
    """Validates dictionary records against a defined structural schema."""

    def __init__(self, schema: Dict[str, Tuple[Type, bool]]):
        # Schema format: {'field_name': (expected_type, is_required)}
        self.schema = schema

    def validate_record(self, record: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Check a single record against schema rules and collect errors."""
        if not isinstance(record, dict):
            return False, ["Input record must be a dictionary"]

        errors = []
        for field, (expected_type, required) in self.schema.items():
            if field not in record or record[field] is None:
                if required:
                    errors.append(f"Missing required field: '{field}'")
                continue

            val = record[field]
            if not isinstance(val, expected_type):
                actual_type = type(val).__name__
                errors.append(
                    f"Field '{field}' expected {expected_type.__name__}, got {actual_type}"
                )

        return len(errors) == 0, errors


def validate_processing_loop(
    dataset: List[Dict[str, Any]],
    validator: RecordValidator,
    stop_on_first_error: bool = False
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Runs validation across a stream or sequence of input items.
    Returns tuples of (valid_records, failed_records_with_details).
    """
    valid_records = []
    failed_records = []

    for index, item in enumerate(dataset):
        is_valid, errors = validator.validate_record(item)
        if is_valid:
            valid_records.append(item)
        else:
            failure_info = {
                "index": index,
                "item": item,
                "errors": errors
            }
            failed_records.append(failure_info)
            if stop_on_first_error:
                break

    return valid_records, failed_records
