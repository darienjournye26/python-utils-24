import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Execute function with fallback for edge cases."""
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError, KeyError) as e:
        logger.error(f"Execution failed: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}")
        raise

def robust_int_conversion(value: Any, fallback: int = 0) -> int:
    """Convert input to integer with robust error handling."""
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return fallback

def validate_collection_input(data: Any, min_size: int = 1) -> bool:
    """Check if collection satisfies basic size constraints."""
    try:
        return len(data) >= min_size
    except (TypeError, AttributeError):
        return False

if __name__ == "__main__":
    # Example usage for verification
    assert robust_int_conversion("10.5") == 10
    assert robust_int_conversion(None, fallback=-1) == -1
    assert validate_collection_input([1, 2]) is True
    assert validate_collection_input(None) is False