# config/config_parser.py
import yaml
import os
from pathlib import Path

class ConfigParser:
    def __init__(self, config_file="global_config.yaml"):
        # Resolve path relative to this file
        config_path = Path(__file__).parent / config_file
        
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found at {config_path}")
            
        with open(config_path, "r") as file:
            self._data = yaml.safe_load(file)

    def get_val(self, key_path, default=None):
        """
        Retrieves nested values using dot notation (e.g., 'browser_settings.headless')
        """
        keys = key_path.split('.')
        val = self._data
        try:
            for key in keys:
                val = val[key]
            return val
        except (KeyError, TypeError):
            return default

# Single instance to be used across the framework
config = ConfigParser()