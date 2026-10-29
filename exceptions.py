class UtilsError(Exception):
    """Base exception for python-utils-24 package."""
    pass

class ConfigurationError(UtilsError):
    """Raised when configuration validation fails."""
    pass

class ProcessingError(UtilsError):
    """Raised when data processing encounters an issue."""
    pass

def raise_if_none(value, name="value"):
    """Ensures a variable is not None, raises ProcessingError if it is."""
    if value is None:
        raise ProcessingError(f"{name} cannot be None")
    return value

def validate_condition(condition: bool, message: str):
    """Checks a condition and raises UtilsError if False."""
    if not condition:
        raise UtilsError(message)

def safe_execute(func, *args, **kwargs):
    """Wrapper to catch exceptions and return None on failure."""
    try:
        return func(*args, **kwargs)
    except Exception:
        return None