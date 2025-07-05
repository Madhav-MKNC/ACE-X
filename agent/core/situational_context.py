"""
situational_context.py

Captures current situational context for the agent: environment, recent events, trending topics.
"""

from typing import Dict, Any

class SituationalContext:
    """
    Stores and updates the agent's situational context.
    """

    def __init__(self):
        """
        Initialize empty context.
        """
        self.context: Dict[str, Any] = {}

    def update(self, key: str, value: Any) -> None:
        """
        Update or add a context entry.
        """
        self.context[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a context value.
        """
        return self.context.get(key, default)

    def remove(self, key: str) -> None:
        """
        Remove a context entry.
        """
        if key in self.context:
            del self.context[key]

    def as_dict(self) -> Dict[str, Any]:
        """
        Return full context dictionary.
        """
        return dict(self.context)
