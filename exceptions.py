"""Custom exception classes for python-utils-24 package."""

from typing import Optional

class PythonUtilsError(Exception):
    """Base exception class for all errors raised by this utility library."""
    def __init__(self, message: str, original_exception: Optional[Exception] = None) -> None:
        super().__init__(message)
        self.message = message
        self.original_exception = original_exception

class ValidationError(PythonUtilsError):
    """Raised when an input or parameter validation check fails."""
    pass

class ConfigurationError(PythonUtilsError):
    """Raised when application setup or configuration is invalid."""
    pass

class ProcessingError(PythonUtilsError):
    """Raised when a background or file processing operation fails."""
    pass

class ResourceNotFoundError(PythonUtilsError):
    """Raised when a specified file, directory, or key is not found."""
    pass
