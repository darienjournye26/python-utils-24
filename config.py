import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    Returns the resulting dictionary or defaults if the file is missing.
    """
    config = defaults.copy()
    
    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_data = json.load(f)
            if isinstance(user_data, dict):
                config.update(user_data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """
    Persists the configuration dictionary to a JSON file.
    """
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)