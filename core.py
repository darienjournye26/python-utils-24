import logging
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('python-utils-24')

class DataProcessor:
    """Core processor for data normalization tasks."""
    def __init__(self, settings: Optional[Dict[str, Any]] = None):
        self.settings = settings or {}

    def sanitize(self, data: str) -> str:
        """Remove whitespace and force lowercase."""
        if not isinstance(data, str):
            return ""
        return data.strip().lower()

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Transform dictionary values using sanitization."""
        try:
            return {k: self.sanitize(str(v)) for k, v in payload.items()}
        except Exception as e:
            logger.error(f"processing failure: {e}")
            return {}

def initialize_service(config: Dict[str, Any]) -> DataProcessor:
    """Factory function for processor initialization."""
    logger.info("initializing data processor service")
    return DataProcessor(settings=config)