import os
import logging

# Standardized constants for system operations
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Custom exit codes for edge case management
EXIT_SUCCESS = 0
EXIT_INVALID_CONFIG = 10
EXIT_NETWORK_FAILURE = 11
EXIT_TIMEOUT_REACHED = 12

# Configuration constraints
MIN_BUFFER_SIZE = 1024
MAX_BUFFER_SIZE = 65536

def get_logger(name):
    """Configures a standard logger instance for the utility."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(LOG_LEVEL)
    return logger

# Singleton logger instance
logger = get_logger('python-utils-24')