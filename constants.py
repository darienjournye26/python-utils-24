from typing import Final, Dict, Any

# Configuration constants for the utility suite
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Path settings for file system operations
DEFAULT_LOG_DIR: Final[str] = "/var/log/python-utils-24"
DEFAULT_CONFIG_PATH: Final[str] = "./config.yaml"

# Standardized error messages
ERROR_TIMEOUT: Final[str] = "operation timed out after {} seconds"
ERROR_CONNECTION: Final[str] = "failed to establish remote connection"

# Supported environment configurations
SUPPORTED_ENVS: Final[list[str]] = ["development", "staging", "production"]

def get_default_config() -> Dict[str, Any]:
    """Return the base configuration dictionary.

    Returns:
        Dict[str, Any]: Default application settings mapping.
    """
    return {
        "timeout": DEFAULT_TIMEOUT,
        "retries": MAX_RETRIES,
        "log_dir": DEFAULT_LOG_DIR
    }