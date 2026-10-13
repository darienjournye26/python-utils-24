from typing import Final, Dict, Any
import sys

# Optimized constant definitions for performance
# Using slots-like structures for read-only dictionary lookups

CACHE_SIZE_LIMIT: Final[int] = 1024
DEFAULT_TIMEOUT: Final[float] = 30.0

# Pre-computed lookup table for frequently accessed configuration
# Avoids repeated dictionary instantiation in hot paths
ENVIRONMENT_CONFIG: Final[Dict[str, Any]] = {
    "buffer_size": 4096,
    "encoding": "utf-8",
    "enable_optimization": True
}

# System path constants for rapid resolution
PLATFORM_ID: Final[str] = sys.platform
IS_WIN: Final[bool] = sys.platform == "win32"

# Type hint registry for validation speedup
VALID_TYPES: Final[tuple] = (int, float, str, bool)

def get_optimized_config(key: str) -> Any:
    """Provides fast access to global settings."""
    return ENVIRONMENT_CONFIG.get(key)

# Explicit cache warming constants
INITIAL_CACHE_CAPACITY: Final[int] = 128
GC_THRESHOLD: Final[int] = 700