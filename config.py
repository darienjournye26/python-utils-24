import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration with fallback to default values."""
    config = defaults.copy()
    
    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            config.update(data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists configuration dictionary to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)

# Example usage:
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    settings = load_config('config.json', defaults)
    print(f'Active config: {settings}')