"""Centralized constants for python-utils-24 library."""

from typing import Final

# Date & Time formats
DEFAULT_DATETIME_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"
ISO_DATETIME_FORMAT: Final[str] = "%Y-%m-%dT%H:%M:%S.%fZ"
DEFAULT_DATE_FORMAT: Final[str] = "%Y-%m-%d"

# Network & I/O Defaults
DEFAULT_TIMEOUT: Final[float] = 30.0  # seconds
DEFAULT_BUFFER_SIZE: Final[int] = 8192  # bytes
MAX_RETRIES: Final[int] = 3
RETRY_BACKOFF_FACTOR: Final[float] = 1.5

# Common Regular Expressions
EMAIL_REGEX: Final[str] = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
SLUG_REGEX: Final[str] = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"

# Data processing limits and encoding
MAX_BATCH_SIZE: Final[int] = 1000
DEFAULT_ENCODING: Final[str] = "utf-8"

# Environment variable keys
ENV_DEBUG_KEY: Final[str] = "UTILS_DEBUG"
ENV_CONFIG_PATH_KEY: Final[str] = "UTILS_CONFIG_PATH"
