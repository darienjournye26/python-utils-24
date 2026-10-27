class BaseUtilsError(Exception):
    """Base exception for the python-utils-24 package."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when settings are invalid or missing."""
    pass

class ValidationError(BaseUtilsError):
    """Raised when data validation fails."""
    pass

class ProcessingError(BaseUtilsError):
    """Raised during unexpected execution failures."""
    def __init__(self, message, original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception

class ResourceNotFoundError(BaseUtilsError):
    """Raised when a requested resource is missing."""
    pass

def handle_exception(e: Exception) -> None:
    """Standardized exception formatting for logs."""
    if isinstance(e, BaseUtilsError):
        print(f"[Utils Error] {e.__class__.__name__}: {e}")
    else:
        print(f"[Unexpected Error] {type(e).__name__}: {e}")