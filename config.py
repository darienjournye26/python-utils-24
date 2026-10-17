import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Loads application configuration with default fallback values and env overrides."""

    def __init__(
        self, 
        defaults: Optional[Dict[str, Any]] = None, 
        env_prefix: str = "APP_"
    ) -> None:
        self._defaults = defaults or {}
        self._config: Dict[str, Any] = self._defaults.copy()
        self._env_prefix = env_prefix

    def load_from_json(self, filepath: str) -> Dict[str, Any]:
        """Load settings from a JSON file, merging over defaults."""
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                file_data = json.load(f)
                self._config.update(file_data)
        return self._config

    def load_from_env(self) -> Dict[str, Any]:
        """Override current config with environment variables matching prefix."""
        for key, value in os.environ.items():
            if key.startswith(self._env_prefix):
                config_key = key[len(self._env_prefix):].lower()
                self._config[config_key] = value
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option with optional fallback."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a specific configuration key manually."""
        self._config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the current configuration dictionary."""
        return self._config.copy()
