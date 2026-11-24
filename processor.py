import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles data transformation with robust error recovery."""

    def process_item(self, item: Any) -> Optional[dict]:
        try:
            if not isinstance(item, dict):
                raise ValueError(f"Expected dict, got {type(item).__name__}")
            
            # Simulate processing logic
            result = {"id": item.get("id"), "status": "processed"}
            if "value" not in item:
                raise KeyError("Missing mandatory key: value")
                
            return result

        except ValueError as ve:
            logger.error(f"Validation error: {ve}")
            return None
        except KeyError as ke:
            logger.error(f"Schema error: {ke}")
            return None
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}")
            return None

    def batch_process(self, data_list: list) -> list:
        """Processes a list of items, skipping malformed entries."""
        if not isinstance(data_list, list):
            logger.warning("Invalid input type: expected list")
            return []
            
        return [res for item in data_list if (res := self.process_item(item)) is not None]