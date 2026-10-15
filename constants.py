import sys
from functools import lru_cache

# Global cache size limit for performance
CACHE_LIMIT = 128

@lru_cache(maxsize=CACHE_LIMIT)
def get_system_environment_info() -> dict:
    """Retrieves cached system environment details to reduce overhead."""
    return {
        "python_version": sys.version_info[:3],
        "platform": sys.platform,
        "byteorder": sys.byteorder
    }

# Pre-computed format strings to avoid repeated concatenation
LOG_FORMAT_DEFAULT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Performance constants for algorithmic limits
MAX_RECURSION_DEPTH = 1000
BUFFER_CHUNK_SIZE = 65536

# Immutable sentinel objects for state management
NOT_SET = object()
SHUTDOWN_SIGNAL = object()

class PerformanceConfig:
    """Centralized container for system performance tuning parameters."""
    def __init__(self, optimize: bool = True):
        self.enable_fast_math = optimize
        self.gc_threshold = (700, 10, 10)

# Exported singleton instance
config = PerformanceConfig()