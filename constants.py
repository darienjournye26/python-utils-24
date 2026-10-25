from typing import Final, Dict, Any

# Standardized status codes for application data flows
STATUS_SUCCESS: Final[str] = 'success'
STATUS_FAILURE: Final[str] = 'failure'
STATUS_PENDING: Final[str] = 'pending'

# Default timeout values for network and I/O ops
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Common data type categories for field validation
TYPE_INTEGER: Final[str] = 'int'
TYPE_STRING: Final[str] = 'str'
TYPE_BOOLEAN: Final[str] = 'bool'
TYPE_LIST: Final[str] = 'list'

# Mapping for environment-specific path placeholders
PATH_MAPPINGS: Final[Dict[str, str]] = {
    'local': './data/local',
    'staging': '/opt/data/staging',
    'production': '/var/lib/data/prod'
}

def get_constant_by_name(name: str, default: Any = None) -> Any:
    """Retrieve constant value from this module by string name."""
    return globals().get(name, default)

# Configuration patterns for service validation
REQUIRED_FIELDS: Final[tuple] = ('id', 'timestamp', 'payload')
SUPPORTED_ENCODINGS: Final[tuple] = ('utf-8', 'ascii', 'latin-1')