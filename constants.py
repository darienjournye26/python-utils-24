"""General utility constants and typed constant registry."""

from enum import Enum
from typing import Any, Dict, Final, Optional


class Environment(str, Enum):
    """Supported runtime environment identifiers."""

    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


# Default application timeout in seconds
DEFAULT_TIMEOUT: Final[int] = 30

# Default max retry attempts for network operations
DEFAULT_MAX_RETRIES: Final[int] = 3

# Common HTTP status codes for convenient reference
HTTP_STATUS_OK: Final[int] = 200
HTTP_STATUS_BAD_REQUEST: Final[int] = 400
HTTP_STATUS_UNAUTHORIZED: Final[int] = 401
HTTP_STATUS_NOT_FOUND: Final[int] = 404
HTTP_STATUS_SERVER_ERROR: Final[int] = 500


class ConstantRegistry:
    """Type-safe dynamic registry for storing and retrieving runtime constants."""

    def __init__(self, initial_data: Optional[Dict[str, Any]] = None) -> None:
        """Initialize registry with optional dictionary of constant key-value pairs."""
        self._registry: Dict[str, Any] = {}
        if initial_data:
            for key, value in initial_data.items():
                self.register(key, value)

    def register(self, key: str, value: Any) -> None:
        """Register a new constant key-value pair. Prevents overwriting existing keys."""
        if key in self._registry:
            raise KeyError(f"Constant '{key}' is already defined and immutable.")
        self._registry[key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve constant value by key with optional default fallback."""
        return self._registry.get(key, default)

    def as_dict(self) -> Dict[str, Any]:
        """Return a shallow copy of registered constants."""
        return self._registry.copy()