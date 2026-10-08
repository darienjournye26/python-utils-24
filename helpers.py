import os
import json
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file with error handling."""
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_json_file(data: Dict[str, Any], file_path: str) -> bool:
    """Writes a dictionary to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable or default value."""
    return os.environ.get(key, default or "")

def chunk_list(data: list, size: int):
    """Splits a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_path(path: str) -> str:
    """Cleans path strings for safe system operations."""
    return os.path.normpath(path.strip())
