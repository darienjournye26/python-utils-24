from typing import Final, Dict, Any

# Application configuration constants
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# System path settings
BASE_DIRECTORY: Final[str] = "/opt/python-utils-24/data"
LOG_FILE: Final[str] = f"{BASE_DIRECTORY}/app.log"

# Environment mapping definitions
ENV_MAP: Final[Dict[str, str]] = {
    "dev": "development",
    "stg": "staging",
    "prd": "production"
}

def get_timeout_settings() -> Dict[str, Any]:
    """
    Returns a dictionary containing system default timeout configurations.

    Returns:
        Dict[str, Any]: Mapping of timeout parameter names to values.
    """
    return {
        "connection": DEFAULT_TIMEOUT,
        "read": DEFAULT_TIMEOUT * 2,
        "write": DEFAULT_TIMEOUT * 2
    }

# Operational status codes
STATUS_SUCCESS: Final[int] = 0
STATUS_ERROR: Final[int] = 1
STATUS_WARNING: Final[int] = 2