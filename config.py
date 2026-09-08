import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration with provided fallback defaults."""
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

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists current configuration to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)

if __name__ == '__main__':
    # Example usage for demonstration
    default_settings = {"host": "localhost", "port": 8080}
    settings = load_config("settings.json", default_settings)
    print(f"Active configuration: {settings}")