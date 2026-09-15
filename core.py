import os
import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, directory: str = "./data"):
        self.directory = directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def clean_key(self, key: str) -> str:
        """Sanitize input keys for file system safety."""
        return "".join(c for c in key if c.isalnum() or c in ("_", "-")).strip()

    def write_data(self, key: str, value: Any) -> bool:
        """Persists content to local storage directory."""
        safe_key = self.clean_key(key)
        if not safe_key:
            logger.error("Invalid key provided for storage")
            return False

        path = os.path.join(self.directory, f"{safe_key}.txt")
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(str(value))
            return True
        except IOError as e:
            logger.error(f"Disk write failure: {e}")
            return False

    def get_data(self, key: str) -> Optional[str]:
        """Retrieves content from local storage."""
        path = os.path.join(self.directory, f"{self.clean_key(key)}.txt")
        try:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return f.read()
        except IOError as e:
            logger.warning(f"Read access error: {e}")
        return None