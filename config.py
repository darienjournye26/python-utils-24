import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}

def load_config(path: str) -> Dict[str, Any]:
    """
    Loads JSON configuration from file, merging with defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(path):
        return config

    try:
        with open(path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

class ConfigManager:
    """
    Configuration manager with persistence support.
    """
    def __init__(self, config_path: str = "config.json"):
        self.path = config_path
        self.settings = load_config(config_path)

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    def save(self) -> None:
        with open(self.path, "w") as f:
            json.dump(self.settings, f, indent=4)