import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    Returns a dictionary containing the loaded configuration or defaults.
    """
    config = defaults.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                config.update(data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

if __name__ == '__main__':
    # Example usage for python-utils-24
    default_settings = {'host': 'localhost', 'port': 8080, 'debug': False}
    user_config = load_config('settings.json', default_settings)
    print(f'Active config: {user_config}')