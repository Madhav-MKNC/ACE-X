"""
settings.py

Configuration loader for the ACE-X agent. Loads settings from environment variables and constants.
"""

import os
from .constants import (
    BASE_DIR,
    DATA_DIR,
    LOG_DIR,
    SNAPSHOT_DIR,
    MEMORY_STORE_DIR,
    CONSTITUTION_FILE,
    AGENT_TRAITS_FILE,
    DEFAULT_DB_FILE,
    SESSION_FILE,
    TWITTER_API_BASE,
    MASTODON_API_BASE,
    REDDIT_USER_AGENT,
)

class Settings:
    """
    Application settings for the ACE-X agent.
    """
    # Paths
    BASE_DIR = BASE_DIR
    DATA_DIR = DATA_DIR
    LOG_DIR = LOG_DIR
    SNAPSHOT_DIR = SNAPSHOT_DIR
    MEMORY_STORE_DIR = MEMORY_STORE_DIR

    # Files
    CONSTITUTION_FILE = CONSTITUTION_FILE
    AGENT_TRAITS_FILE = AGENT_TRAITS_FILE
    DATABASE_FILE = os.getenv("DATABASE_FILE", DEFAULT_DB_FILE)
    SESSION_FILE = os.getenv("SESSION_FILE", SESSION_FILE)

    # API Keys & Tokens from environment
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
    MASTODON_ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
    REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
    REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    IMAP_SERVER = os.getenv("IMAP_SERVER")
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    # API Endpoints
    TWITTER_API_BASE = TWITTER_API_BASE
    MASTODON_API_BASE = MASTODON_API_BASE
    REDDIT_USER_AGENT = REDDIT_USER_AGENT
