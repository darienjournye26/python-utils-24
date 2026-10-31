import os
from typing import Dict, Any, Optional

class ConfigLoader:
    """Handles loading and retrieval of application configuration settings."""

    def __init__(self, env_prefix: str = "APP_") -> None:
        self.env_prefix: str = env_prefix
        self._settings: Dict[str, Any] = {}

    def load_from_env(self) -> None:
        """Loads environment variables into the settings dictionary."""
        for key, value in os.environ.items():
            if key.startswith(self.env_prefix):
                clean_key: str = key[len(self.env_prefix):].lower()
                self._settings[clean_key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a setting by key with an optional default value."""
        return self._settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Manually updates a setting value in the configuration."""
        self._settings[key] = value

def get_default_config() -> ConfigLoader:
    """Factory function to return a pre-configured loader instance."""
    loader = ConfigLoader()
    loader.load_from_env()
    return loader