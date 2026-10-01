class UtilsError(Exception):
    """Base exception for python-utils-24 operations."""

class ConfigurationError(UtilsError):
    """Raised when configuration requirements are not met."""

class ValidationError(UtilsError):
    """Raised when input data fails validation checks."""

class ExecutionError(UtilsError):
    """Raised when a primary operation fails to complete."""

def raise_if_none(value, message: str = "Value cannot be None"): 
    """Utility for raising ValidationError on null inputs."""
    if value is None:
        raise ValidationError(message)

def format_exception(e: Exception) -> str:
    """Standardized formatting for caught exceptions."""
    return f"[{type(e).__name__}] {str(e)}"

def safe_execute(func, *args, **kwargs):
    """Decorator pattern for catching broad operation errors."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        formatted = format_exception(e)
        raise ExecutionError(f"Operation failed: {formatted}") from e