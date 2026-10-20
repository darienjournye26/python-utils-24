import os
from typing import Dict, Any, Optional

class ConfigManager:
    """Handles application configuration loading and access."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = defaults or {}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Load configuration values from environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                self._config[clean_key] = value

    def update(self, new_settings: Dict[str, Any]) -> None:
        """Update configuration with new dictionary data."""
        self._config.update(new_settings)

    @property
    def all(self) -> Dict[str, Any]:
        """Return a copy of the entire configuration."""
        return self._config.copy()