import os
from typing import Any, Dict, Optional

class ConfigManager:
    """Handles application configuration loading and access."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = defaults or {}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Populate config from environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                self._config[clean_key] = value

    def update(self, new_data: Dict[str, Any]) -> None:
        """Update current configuration with new data."""
        self._config.update(new_data)

    def all(self) -> Dict[str, Any]:
        """Return a copy of the configuration dictionary."""
        return self._config.copy()