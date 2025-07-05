"""
semantic_memory.py

Semantic memory stores facts, entities, and concepts in a structured form.
Supports adding, querying, persisting semantic triples or key-value facts.
"""

import json
from typing import Any, Dict, List, Optional, Tuple

class SemanticMemory:
    """
    Manages semantic facts for the agent.
    """

    def __init__(self):
        """
        Initialize the semantic memory store.
        """
        # store as mapping from subject to list of (predicate, object)
        self._store: Dict[str, List[Tuple[str, Any]]] = {}

    def add_fact(self, subject: str, predicate: str, obj: Any) -> None:
        """
        Add a semantic fact (subject, predicate, object).
        """
        facts = self._store.setdefault(subject, [])
        facts.append((predicate, obj))

    def query_subject(self, subject: str) -> List[Tuple[str, Any]]:
        """
        Retrieve all predicate-object pairs for a subject.
        """
        return self._store.get(subject, [])

    def query_predicate(self, predicate: str) -> List[Tuple[str, Any]]:
        """
        Retrieve all (subject, object) pairs matching a predicate.
        """
        results: List[Tuple[str, Any]] = []
        for subj, facts in self._store.items():
            for pred, obj in facts:
                if pred == predicate:
                    results.append((subj, obj))
        return results

    def query_object(self, obj_value: Any) -> List[Tuple[str, str]]:
        """
        Retrieve all (subject, predicate) pairs with the given object value.
        """
        results: List[Tuple[str, str]] = []
        for subj, facts in self._store.items():
            for pred, obj in facts:
                if obj == obj_value:
                    results.append((subj, pred))
        return results

    def clear(self) -> None:
        """
        Clear all semantic facts.
        """
        self._store.clear()

    def save_to_file(self, path: str) -> None:
        """
        Persist semantic memory to JSON file.
        TODO: implement using infra.file_manager.
        """
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self._store, f, indent=2)

    def load_from_file(self, path: str) -> None:
        """
        Load semantic memory from JSON file.
        TODO: implement using infra.file_manager.
        """
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Ensure correct types
        self._store = {str(k): [(pred, obj) for pred, obj in v] for k, v in data.items()}
