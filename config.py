import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    Returns the merged dictionary.
    """
    config = defaults.copy()
    
    if not os.path.exists(path):
        return config

    try:
        with open(path, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(path: str, config: Dict[str, Any]) -> None:
    """
    Saves a configuration dictionary to a JSON file.
    """
    with open(path, 'w') as f:
        json.dump(config, f, indent=4)

# Example usage:
if __name__ == '__main__':
    defaults = {'debug': False, 'port': 8080, 'host': 'localhost'}
    current_config = load_config('config.json', defaults)
    print(f"Active configuration: {current_config}")