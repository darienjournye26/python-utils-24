import os
from typing import Any, Dict, List, Optional, Union


class ConfigError(Exception):
    """Raised when there is an issue with the configuration."""

    pass


class Configuration:
    """Manages application configuration loaded from environment variables or dicts."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the Configuration with optional default values."""
        self._config: Dict[str, Any] = defaults or {}

    def get(
        self, key: str, default: Optional[Any] = None
    ) -> Union[Any, None]:
        """Retrieve a configuration value by key, with an optional default fallback.

        Args:
            key: The configuration key to retrieve.
            default: The fallback value if the key is not found.

        Returns:
            The configuration value or the default fallback.
        """
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value.

        Args:
            key: The configuration key to set.
            value: The value to associate with the key.
        """
        self._config[key] = value

    def load_from_env(self, keys: List[str]) -> None:
        """Load specified configuration keys from environment variables.

        Args:
            keys: A list of environment variable names to load.
        """
        for key in keys:
            if key in os.environ:
                self._config[key] = os.environ[key]
