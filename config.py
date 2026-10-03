import json
import os
from typing import Any, Dict

def load_config(file_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from JSON file, merging with defaults.
    Returns the merged configuration dictionary.
    """
    config = defaults.copy()

    if not os.path.exists(file_path):
        return config

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            config.update(data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

if __name__ == '__main__':
    # Example usage for python-utils-24
    default_settings = {
        'host': '127.0.0.1',
        'port': 8080,
        'debug': False
    }
    
    current_config = load_config('settings.json', default_settings)
    print(f"Loaded configuration: {current_config}")