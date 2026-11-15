import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class DataHandler:
    """Handles data processing and lifecycle management."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.is_active = True

    def process_payload(self, data: Any) -> Optional[Dict[str, Any]]:
        """Validates and transforms raw input data."""
        if not self.is_active:
            logger.warning("Handler inactive; skipping processing")
            return None

        try:
            result = {"status": "success", "data": data}
            return result
        except Exception as e:
            logger.error(f"Processing failed: {e}")
            return {"status": "error", "message": str(e)}

    def shutdown(self) -> None:
        """Graceful cleanup of handler resources."""
        self.is_active = False
        logger.info("Handler resources released")

def initialize_handler(settings: Dict[str, Any]) -> DataHandler:
    """Factory function for handler instantiation."""
    return DataHandler(config=settings)