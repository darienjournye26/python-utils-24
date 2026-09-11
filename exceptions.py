class DataProcessingError(Exception):
    """Base exception for data handling operations."""
    pass

class ValidationError(DataProcessingError):
    """Raised when data fails schema or format validation."""
    pass

class TransformationError(DataProcessingError):
    """Raised when data transformation logic fails."""
    pass

def raise_if_none(data, key):
    """Validates existence of a key in data dictionary."""
    if data is None or key not in data:
        raise ValidationError(f"Missing required key: {key}")
    return data[key]

def safe_execute(func, *args, **kwargs):
    """
    Wrapper for handling data operations with standard error catching.
    """
    try:
        return func(*args, **kwargs)
    except (KeyError, TypeError, ValueError) as e:
        raise TransformationError(f"Operation failed: {str(e)}") from e

class DataHandlerMixin:
    """Mixin for standard error reporting in data classes."""
    def handle_exception(self, error: Exception):
        """Centralized error logging hook."""
        print(f"[ERROR] {self.__class__.__name__}: {error}")
        raise error