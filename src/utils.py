import os
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

def load_config(path: str = "config.yaml") -> dict:
    """Load YAML configuration file"""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def getenv_int(key: str, default: int) -> int:
    """Get an environment variable as integer with fallback"""
    try:
        return int(os.getenv(key, default))
    except Exception:
        return default
