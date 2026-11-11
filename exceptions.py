class UtilsError(Exception):
    """Base exception for python-utils-24 package."""
    pass

class ValidationError(UtilsError):
    """Raised when input data fails validation requirements."""
    pass

class DataProcessingError(UtilsError):
    """Raised when data transformation logic fails."""
    pass

def validate_not_none(value, name: str):
    """Ensures value is not None, raising ValidationError otherwise."""
    if value is None:
        raise ValidationError(f"Argument '{name}' cannot be None")
    return value

def safe_process(func, data):
    """Wraps function execution with error normalization."""
    try:
        return func(data)
    except Exception as e:
        if isinstance(e, UtilsError):
            raise
        raise DataProcessingError(f"Failed to process data: {e}") from e