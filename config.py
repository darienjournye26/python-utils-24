import os
import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class ConfigError(Exception):
    """Custom exception raised for configuration errors."""
    pass


class ConfigManager:
    """Manages application configuration loading with edge case handling."""

    def __init__(self, default_config: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = default_config.copy() if default_config else {}

    def load_from_json(self, file_path: str) -> bool:
        """Loads configuration settings from a JSON file safely."""
        if not isinstance(file_path, (str, bytes, os.PathLike)):
            raise ConfigError(f"Invalid file path type: {type(file_path).__name__}")

        if not os.path.exists(file_path):
            logger.warning(f"Configuration file not found: {file_path}")
            return False

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    logger.warning(f"Configuration file is empty: {file_path}")
                    return False
                data = json.loads(content)
                if not isinstance(data, dict):
                    raise ConfigError(f"Root element in {file_path} must be a JSON object")
                self._config.update(data)
                return True
        except (OSError, PermissionError) as e:
            raise ConfigError(f"Unable to read file {file_path}: {e}") from e
        except json.JSONDecodeError as e:
            raise ConfigError(f"Invalid JSON syntax in {file_path}: {e}") from e

    def get(self, key: str, default: Any = None, cast_type: Optional[type] = None) -> Any:
        """Retrieves a configuration value with optional type casting and fallback."""
        value = self._config.get(key, default)
        if value is None or cast_type is None:
            return value

        try:
            return cast_type(value)
        except (ValueError, TypeError) as e:
            logger.warning(
                f"Failed to cast key '{key}' value '{value}' to {cast_type.__name__}: {e}"
            )
            return default
