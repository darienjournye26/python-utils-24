import os
from typing import Final

# Application path configurations
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
DATA_DIR: Final[str] = os.path.join(BASE_DIR, 'data')
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Default operation timeouts
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Supported file extensions
ALLOWED_EXTENSIONS: Final[set[str]] = {'.json', '.csv', '.yaml', '.txt'}

# System environment keys
ENV_VAR_PREFIX: Final[str] = 'PYUTILS_'
AUTH_TOKEN_KEY: Final[str] = f'{ENV_VAR_PREFIX}AUTH_TOKEN'

# Formatting defaults
DATE_FORMAT: Final[str] = '%Y-%m-%d %H:%M:%S'
ENCODING: Final[str] = 'utf-8'

def get_config_path(filename: str) -> str:
    """Construct full path for config files."""
    return os.path.join(BASE_DIR, 'configs', filename)