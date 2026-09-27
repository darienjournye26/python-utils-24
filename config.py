import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with defaults."""
    
    def __init__(self, default_config: Dict[str, Any]):
        self.defaults = default_config

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads config from file or returns defaults if missing."""
        if not os.path.exists(filepath):
            return self.defaults
        
        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
            
            # Merge user config over defaults
            config = self.defaults.copy()
            config.update(user_config)
            return config
        except (json.JSONDecodeError, IOError):
            return self.defaults

def get_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Functional wrapper for config loading."""
    loader = ConfigLoader(defaults)
    return loader.load(filepath)