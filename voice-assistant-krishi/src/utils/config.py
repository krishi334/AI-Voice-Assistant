# Configuration settings for the voice assistant

import os
import yaml

def load_config(config_file='config/settings.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_env_variable(var_name):
    return os.getenv(var_name)

# Load configuration settings
config = load_config()