import json
import os
from typing import Any, Dict

def load_config(config_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    """
    config = defaults.copy()

    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, 'r') as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

if __name__ == '__main__':
    # Example usage for configuration management
    default_settings = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    
    app_config = load_config('settings.json', default_settings)
    print(f"Loaded configuration: {app_config}")