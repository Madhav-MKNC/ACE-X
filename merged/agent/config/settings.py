"""
Agent Configuration Settings
Centralized configuration for ACE-X agent, including file paths, API keys, and runtime options.
"""
import os

# Base directory for agent files (relative to this file)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Paths to important files
CONSTITUTION_PATH = os.path.join(BASE_DIR, 'data', 'config', 'constitution.txt')
LOG_DIR = os.path.join(BASE_DIR, 'data', 'logs')

# API keys and secrets (should be loaded from environment or secrets file in production)
TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY', 'your-key-here')
TWITTER_API_SECRET = os.environ.get('TWITTER_API_SECRET', 'your-secret-here')

# Agent runtime options
default_settings = {
    'heartbeat_interval': 60,  # seconds
    'max_daily_tweets': 10,
    'max_follow_per_day': 5,
    'log_level': 'INFO',
}

# Utility to load settings from environment or file (stub)
def load_settings():
    # In production, load from .env or config file
    return default_settings.copy()
