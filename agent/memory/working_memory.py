"""
working_memory.py

Working memory provides short-term, temporary cache for current context and attention.
Supports add, retrieve, and clear operations with optional capacity limit.
"""

from collections import OrderedDict
from typing import Any, Optional

class WorkingMemory:
    """
    Manages short-term memory entries with optional capacity (LRU eviction).
    """

    def __init__(self, capacity: int = 50):
        """
        Initialize working memory with an optional capacity.
        :param capacity: max number of entries to store (LRU eviction if full).
        """
        self.capacity = capacity
        self._store: OrderedDict[str, Any] = OrderedDict()

    def add(self, key: str, value: Any) -> None:
        """
        Add or update a key-value entry in working memory.
        New entries are added to the end (most recent).
        If capacity exceeded, evict the oldest entry.
        """
        if key in self._store:
            self._store.move_to_end(key)
        self._store[key] = value
        if len(self._store) > self.capacity:
            self._store.popitem(last=False)

    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve value by key, updating recency.
        Returns None if key not found.
        """
        if key in self._store:
            self._store.move_to_end(key)
            return self._store[key]
        return None

    def clear(self) -> None:
        """
        Clear all entries from working memory.
        """
        self._store.clear()

    def items(self):
        """
        Return all key-value pairs in order from oldest to newest.
        """
        return list(self._store.items())
