from typing import Any, Dict, Optional, Callable

class DataHandler:
    """Utility class for processing dictionary data with validation."""

    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        self.config = config or {}

    def process_payload(self, payload: Dict[str, Any], callback: Optional[Callable[[Any], Any]] = None) -> Dict[str, Any]:
        """
        Processes input payload and executes an optional callback.

        Args:
            payload: The dictionary to be processed.
            callback: A transformation function to apply to values.

        Returns:
            Processed dictionary with updated values.
        """
        processed: Dict[str, Any] = {}
        for key, value in payload.items():
            if callback:
                processed[key] = callback(value)
            else:
                processed[key] = value
        return processed

    def validate_keys(self, payload: Dict[str, Any], required_keys: list[str]) -> bool:
        """
        Checks if all required keys exist in the payload.

        Args:
            payload: The dictionary to inspect.
            required_keys: A list of keys that must be present.

        Returns:
            True if all keys are found, False otherwise.
        """
        return all(key in payload for key in required_keys)