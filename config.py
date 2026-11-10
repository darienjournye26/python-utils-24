import os
from functools import lru_cache
from typing import Any, Dict

class ConfigManager:
    """Thread-safe configuration handler with memoization."""

    def __init__(self, env_prefix: str = "APP_"):
        self._prefix = env_prefix
        self._cache = {}

    @lru_cache(maxsize=128)
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Retrieve environment variable with caching for performance."""
        return os.environ.get(f"{self._prefix}{key.upper()}", default)

    def get_all(self, keys: list) -> Dict[str, Any]:
        """Batch fetch settings to reduce system call overhead."""
        return {k: self.get_setting(k) for k in keys}

    def clear_cache(self) -> None:
        """Reset internal LRU cache for environment changes."""
        self.get_setting.cache_clear()

# Initialize global configuration instance
settings = ConfigManager()

def get_config(key: str, default: Any = None) -> Any:
    """Module-level accessor for shared config settings."""
    return settings.get_setting(key, default)