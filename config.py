import json
import os
from typing import Any, Dict, Optional, Type


class ConfigError(Exception):
    """Base exception raised for configuration loading and validation errors."""
    pass


class ConfigManager:
    """Manages configuration settings with edge case validation and fallbacks."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._settings: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_file(self, filepath: str) -> None:
        """Loads JSON configuration file with robust error handling for bad inputs."""
        if not isinstance(filepath, str) or not filepath.strip():
            raise ConfigError("Filepath must be a non-empty string")

        if not os.path.exists(filepath):
            raise ConfigError(f"Configuration file not found: {filepath}")

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    raise ConfigError("Configuration root must be a JSON object")
                self._settings.update(data)
        except json.JSONDecodeError as err:
            raise ConfigError(f"Malformed JSON format in '{filepath}': {err}") from err
        except PermissionError as err:
            raise ConfigError(f"Permission denied reading '{filepath}': {err}") from err
        except OSError as err:
            raise ConfigError(f"I/O error reading '{filepath}': {err}") from err

    def get(self, key: str, default: Any = None, expected_type: Optional[Type] = None) -> Any:
        """Retrieves value with type coercion and env variable fallback."""
        if not isinstance(key, str) or not key.strip():
            raise ConfigError("Configuration key must be a non-empty string")

        env_key = key.upper().replace(".", "_")
        raw_val = os.getenv(env_key, self._settings.get(key, default))

        if raw_val is None:
            return None

        if expected_type is not None:
            try:
                if expected_type is bool and isinstance(raw_val, str):
                    return raw_val.strip().lower() in ("true", "1", "yes", "on")
                return expected_type(raw_val)
            except (ValueError, TypeError) as err:
                raise ConfigError(
                    f"Key '{key}' value '{raw_val}' cannot be converted to {expected_type.__name__}"
                ) from err

        return raw_val