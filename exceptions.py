from typing import Optional, Any

class BaseUtilsError(Exception):
    """Base exception class for python-utils-24 package."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when a configuration value is invalid."""
    def __init__(self, message: str, key: Optional[str] = None) -> None:
        super().__init__(message)
        self.key = key

class ProcessingError(BaseUtilsError):
    """Raised when data processing fails unexpectedly."""
    def __init__(self, message: str, payload: Any = None) -> None:
        super().__init__(message)
        self.payload = payload

class ValidationError(BaseUtilsError):
    """Raised when input validation fails."""
    def __init__(self, message: str, constraint: str) -> None:
        super().__init__(message)
        self.constraint = constraint

def raise_if_none(value: Any, name: str) -> None:
    """Check if value is None and raise error if so."""
    if value is None:
        raise ValidationError(f"Value '{name}' cannot be None", "non-null")