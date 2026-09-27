import os
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def sanitize_environment(env_vars: list) -> Dict[str, str]:
    """Extract and validate requested environment variables."""
    sanitized = {}
    for key in env_vars:
        value = os.getenv(key)
        if value:
            sanitized[key] = value.strip()
    return sanitized

def ensure_directory(path: str) -> bool:
    """Verification of directory existence and creation."""
    try:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            logger.info(f"Directory created: {path}")
        return True
    except OSError as e:
        logger.error(f"Directory creation failed: {e}")
        return False

def format_data_dict(data: Dict[str, Any]) -> Dict[str, str]:
    """String conversion for dictionary values."""
    return {k: str(v) for k, v in data.items() if v is not None}

def get_safe_env(key: str, default: Optional[str] = None) -> str:
    """Environment lookup with fallback defaults."""
    return os.getenv(key, default or "")