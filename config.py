import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with defaults.
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

def get_env_var(key: str, default: Any) -> Any:
    """
    Retrieves environment variable with fallback to default.
    """
    return os.environ.get(key, default)

if __name__ == '__main__':
    # Example usage for demonstration
    default_settings = {
        "host": "localhost",
        "port": 8080,
        "debug": False
    }
    settings = load_config("settings.json", default_settings)
    print(f"Loaded settings: {settings}")