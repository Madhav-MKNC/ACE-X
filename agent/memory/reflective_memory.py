"""
reflective_memory.py

Reflective memory stores lessons learned and higher-order generalizations from past experiences.
Supports logging evaluations, retrieving insights, and clearing reflective entries.
"""

from typing import Any, Dict, List, Optional

class ReflectiveMemory:
    """
    Manages reflective memory entries for self-analysis and meta-reasoning.
    """

    def __init__(self):
        """
        Initialize the reflective memory store.
        """
        self._entries: List[Dict[str, Any]] = []

    def add_insight(self, insight: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Add a new reflective insight.
        :param insight: Description of the lesson learned.
        :param metadata: Optional additional context.
        """
        entry = {
            "insight": insight,
            "metadata": metadata or {}
        }
        self._entries.append(entry)

    def query_insights(self, keyword: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Query reflective entries by keyword.
        :param keyword: Search term.
        :param limit: Maximum number of entries to return.
        """
        matches = [e for e in self._entries
                   if keyword.lower() in e["insight"].lower()
                   or any(keyword.lower() in str(v).lower() for v in e["metadata"].values())]
        return matches[:limit]

    def get_all(self) -> List[Dict[str, Any]]:
        """
        Return all reflective entries.
        """
        return list(self._entries)

    def clear(self) -> None:
        """
        Clear all reflective memory entries.
        """
        self._entries.clear()
