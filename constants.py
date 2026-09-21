import typing

# Configuration settings for data processing utilities
DEFAULT_ENCODING: str = 'utf-8'
CHUNK_SIZE: int = 1024 * 64  # 64KB buffer size

# Supported file extensions for general data handling
SUPPORTED_FORMATS: typing.Tuple[str, ...] = ('.json', '.csv', '.yaml', '.txt')

# Standard timeout values in seconds
NETWORK_TIMEOUT: int = 30
OPERATION_RETRY_LIMIT: int = 3

# Path constants for environment mapping
LOG_DIR: str = './logs'
TEMP_DIR: str = './tmp'

def get_buffer_size(multiplier: int = 1) -> int:
    """Return scaled buffer size for memory allocation."""
    return CHUNK_SIZE * multiplier

def is_supported(filename: str) -> bool:
    """Check if the file format is allowed."""
    return filename.lower().endswith(SUPPORTED_FORMATS)

# Mapping for environment-specific execution modes
ENV_MODES: typing.Dict[str, str] = {
    'dev': 'development',
    'prod': 'production',
    'test': 'testing'
}