"""
Constants for python-utils-24.

This module provides commonly used constants with type annotations.
It includes settings for general utilities like I/O, validation, and more.
Practical for use in other modules.
"""

from typing import Final, Dict, List, Tuple, Any

# File and encoding constants
DEFAULT_ENCODING: Final[str] = "utf-8"
"""Default text encoding for reading and writing files."""

MAX_FILE_SIZE: Final[int] = 10 * 1024 * 1024
"""Maximum allowed file size in bytes (10MB)."""

# Time and retry constants
DEFAULT_TIMEOUT: Final[float] = 10.0
"""Timeout in seconds for operations that may block."""

MAX_RETRIES: Final[int] = 5
"""Maximum number of retry attempts for failed operations."""

# Data format constants
SUPPORTED_FORMATS: Final[List[str]] = ["json", "yaml", "csv", "xml", "txt"]
"""List of data formats supported by parsing utilities."""

DEFAULT_DELIMITER: Final[str] = ","
"""Default delimiter for CSV like data."""

# Error and status constants
SUCCESS_CODE: Final[int] = 0
"""Code indicating successful operation."""

ERROR_CODES: Final[Dict[str, int]] = {
    "invalid_input": 400,
    "not_found": 404,
    "server_error": 500,
    "timeout": 408
}
"""Dictionary mapping error names to HTTP like status codes."""

# Version info
LIBRARY_VERSION: Final[Tuple[int, int, int]] = (2, 4, 0)
"""Semantic version of the library as tuple."""

# Mathematical constants for general use
GOLDEN_RATIO: Final[float] = 1.61803
"""Approximate golden ratio value."""

# Configuration keys
CONFIG_KEYS: Final[List[str]] = ["debug", "verbose", "output_format", "log_path"]
"""List of valid configuration keys."""

# Practical utility constants
EMPTY_DICT: Final[Dict[str, Any]] = {}
"""Empty dictionary constant for initialization."""

NULL_VALUE: Final[None] = None
"""Explicit null value constant."""

# Additional settings
LOG_FORMAT: Final[str] = "%(asctime)s - %(levelname)s - %(message)s"
"""Standard log format string."""

MAX_WORKERS: Final[int] = 4
"""Default number of worker threads for parallel processing."""

# End of constants definitions