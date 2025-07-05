"""
episodic_memory.py

Episodic memory stores a timeline of experiences (events) with timestamp and metadata.
Supports adding, querying, persisting events.
"""

import datetime
from typing import Any, Dict, List, Optional

class EpisodicMemory:
    """
    Manages episodic memory entries for the agent.
    """

    def __init__(self):
        """
        Initialize the episodic memory store.
        """
        self._events: List[Dict[str, Any]] = []

    def add_event(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Add a new event to memory.
        :param content: Description of the event.
        :param metadata: Optional additional data.
        """
        event = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "content": content,
            "metadata": metadata or {}
        }
        self._events.append(event)

    def query(self, keyword: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Query events containing a keyword in content or metadata.
        :param keyword: Search term.
        :param limit: Maximum number of events to return.
        :return: List of matching events.
        """
        matches = [e for e in self._events
                   if keyword.lower() in e["content"].lower()
                   or any(keyword.lower() in str(v).lower() for v in e["metadata"].values())]
        return matches[:limit]

    def get_recent(self, count: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve the most recent events.
        :param count: Number of events to return.
        """
        return self._events[-count:]

    def clear(self) -> None:
        """
        Clear all episodic memory events.
        """
        self._events.clear()

    def save_to_file(self, path: str) -> None:
        """
        Persist memory events to disk as JSON.
        TODO: implement file write (e.g., via infra.file_manager).
        """
        pass

    def load_from_file(self, path: str) -> None:
        """
        Load memory events from disk.
        TODO: implement file read and parsing.
        """
        pass
