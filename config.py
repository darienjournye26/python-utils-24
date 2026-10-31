import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Manages application configuration with default fallbacks and environment overrides."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_file(self, filepath: Union[str, Path]) -> None:
        """Load JSON configuration file and merge with current settings."""
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"Configuration file not found: {filepath}")

        with path.open("r", encoding="utf-8") as file:
            user_config = json.load(file)
            self._merge_dicts(self._config, user_config)

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Override configuration values using environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self._config[config_key] = self._parse_env_value(value)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key with fallback default."""
        return self._config.get(key, default)

    def _merge_dicts(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        """Recursively merge dictionary source into target."""
        for key, value in source.items():
            if isinstance(value, dict) and key in target and isinstance(target[key], dict):
                self._merge_dicts(target[key], value)
            else:
                target[key] = value

    @staticmethod
    def _parse_env_value(value: str) -> Union[int, float, bool, str]:
        """Convert string environment variables to appropriate primitive types."""
        lowered = value.lower()
        if lowered in ("true", "yes", "1"):
            return True
        if lowered in ("false", "no", "0"):
            return False
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
