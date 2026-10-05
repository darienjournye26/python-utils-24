import json
import os
from typing import Any, Dict

class ConfigLoader:
    """A configuration loader supporting default values and environment overrides."""

    def __init__(self, defaults: Dict[str, Any], env_prefix: str = "APP_") -> None:
        self._defaults = defaults
        self._env_prefix = env_prefix
        self._config = defaults.copy()

    def load_from_file(self, filepath: str) -> None:
        """Loads configuration from a JSON file, merging with current values."""
        if not os.path.exists(filepath):
            return

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                file_config = json.load(f)
                if isinstance(file_config, dict):
                    self._config.update(file_config)
        except (json.JSONDecodeError, OSError) as err:
            raise ValueError(f"Failed to load config file: {err}") from err

    def load_from_env(self) -> None:
        """Overrides configuration values using environment variables."""
        for key, default_val in self._defaults.items():
            env_key = f"{self._env_prefix}{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                self._config[key] = self._cast_value(raw_val, type(default_val))

    def _cast_value(self, value: str, target_type: type) -> Any:
        """Casts string environment variables to matching default types."""
        if target_type is bool:
            return value.lower() in ("true", "1", "yes", "on")
        try:
            return target_type(value)
        except (ValueError, TypeError):
            return value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key."""
        return self._config.get(key, default)

    @property
    def data(self) -> Dict[str, Any]:
        """Returns the complete loaded configuration dictionary."""
        return self._config