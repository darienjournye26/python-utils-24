import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with provided fallback defaults.
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

def get_env_config(prefix: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Overrides configuration keys with matching environment variables.
    """
    config = defaults.copy()
    for key in config.keys():
        env_key = f"{prefix}_{key.upper()}"
        value = os.getenv(env_key)
        if value is not None:
            config[key] = value
    return config