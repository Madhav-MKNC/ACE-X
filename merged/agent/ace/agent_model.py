"""
Agent Model Layer: Maintains the agent's self-understanding, including capabilities, identity, configuration, and telemetry.
Tracks agent's current state and exposes it for use by higher layers.
"""
from typing import Dict, Any

class AgentModelLayer:
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize the Agent Model Layer.
        :param config: Optional dictionary of agent configuration and capabilities
        """
        self.identity = {
            'name': 'ACE-X',
            'version': '1.0',
            'traits': ['curious', 'assertive'],
            'style': 'thoughtful',
        }
        self.capabilities = [
            'tweet', 'reply', 'quote', 'follow', 'observe', 'reflect', 'self-modify'
        ]
        self.config = config or {}
        self.telemetry = {
            'tweets_today': 0,
            'followers': 0,
            'rate_limit_remaining': 100,
        }

    def get_identity(self) -> Dict[str, Any]:
        """Return the agent's identity and traits."""
        return self.identity

    def get_capabilities(self) -> list:
        """Return the agent's list of capabilities."""
        return self.capabilities

    def get_telemetry(self) -> Dict[str, Any]:
        """Return current telemetry (performance, usage, etc)."""
        return self.telemetry

    def update_telemetry(self, key: str, value: Any):
        """Update a telemetry field."""
        self.telemetry[key] = value

    def __repr__(self):
        return f"<AgentModelLayer: {self.identity['name']} v{self.identity['version']}>"
