import os
import json
from typing import Any, Dict, Optional

class ConfigLoader:
    """A utility for loading configuration with fallbacks to defaults and environment variables."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self.defaults = defaults or {}
        self.config = self.defaults.copy()

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        """Merges dictionary data into the configuration."""
        self.config.update(data)

    def load_from_json(self, file_path: str) -> bool:
        """Loads and merges configuration from a JSON file. Returns True if successful."""
        if not os.path.exists(file_path):
            return False
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.load_from_dict(data)
                    return True
        except (json.JSONDecodeError, IOError):
            pass
        return False

    def get(self, key: str, default: Any = None) -> Any:
        """Gets a configuration value, falling back to environment variable or default."""
        # Environment variables take precedence if present
        env_key = key.upper()
        if env_key in os.environ:
            env_val = os.environ[env_key]
            if env_val.lower() == "true":
                return True
            if env_val.lower() == "false":
                return False
            try:
                return int(env_val)
            except ValueError:
                try:
                    return float(env_val)
                except ValueError:
                    return env_val

        return self.config.get(key, default)