"""
constants.py

Application-level constants and default paths.
"""

import os

# Default file paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(DATA_DIR, "logs")
SNAPSHOT_DIR = os.path.join(DATA_DIR, "snapshots")
MEMORY_STORE_DIR = os.path.join(DATA_DIR, "memory", "store")

# Default filenames
CONSTITUTION_FILE = os.path.join(BASE_DIR, "data", "config", "constitution.txt")
AGENT_TRAITS_FILE = os.path.join(BASE_DIR, "data", "config", "agent_traits.json")

# Default settings
DEFAULT_DB_FILE = os.path.join(DATA_DIR, "agent.db")
SESSION_FILE = os.path.join(DATA_DIR, "session.json")

# API Endpoints
TWITTER_API_BASE = "https://api.twitter.com/2"
MASTODON_API_BASE = os.getenv("MASTODON_BASE_URL", "")
