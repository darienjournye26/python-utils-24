import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    Returns a dictionary with merged configuration values.
    """
    config = defaults.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(filepath: str, config: Dict[str, Any]) -> bool:
    """
    Persists configuration dictionary to a JSON file.
    Returns True if successful, False otherwise.
    """
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False