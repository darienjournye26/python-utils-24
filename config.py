import os
import json
from typing import Any, Dict, Optional, Union


class ConfigManager:
    """Manages application configuration settings from environment variables and JSON files."""

    def __init__(self, config_file: Optional[str] = None) -> None:
        """Initialize the configuration manager with an optional JSON file path."""
        self._settings: Dict[str, Any] = {}
        if config_file and os.path.exists(config_file):
            self.load_from_json(config_file)

    def load_from_json(self, file_path: str) -> None:
        """Load configuration key-value pairs from a JSON file."""
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                self._settings.update(data)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key, checking environment first."""
        env_val = os.getenv(key.upper())
        if env_val is not None:
            return env_val
        return self._settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a local configuration key-value pair."""
        self._settings[key] = value

    def get_bool(self, key: str, default: bool = False) -> bool:
        """Retrieve a configuration value cast to a boolean."""
        val = self.get(key, default)
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.lower() in ("true", "1", "yes", "on")
        return bool(val)


def load_app_config(env_prefix: str = "APP_") -> Dict[str, str]:
    """Extract all environment variables starting with a given prefix."""
    result: Dict[str, str] = {}
    for key, value in os.environ.items():
        if key.startswith(env_prefix):
            clean_key = key[len(env_prefix):].lower()
            result[clean_key] = value
    return result
