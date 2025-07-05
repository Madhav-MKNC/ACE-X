"""
belief_model.py

Maintains belief graphs representing agent’s opinions, factual confidence, and trust relationships.
"""

from typing import Dict, Any, List

class BeliefModel:
    """
    Stores and updates beliefs with associated confidence scores.
    """

    def __init__(self):
        """
        Initialize empty belief graph.
        """
        # mapping concept to dict of {related_concept: confidence}
        self.beliefs: Dict[str, Dict[str, float]] = {}

    def add_belief(self, subject: str, predicate: str, confidence: float) -> None:
        """
        Add or update a belief edge with confidence in [0.0,1.0].
        """
        self.beliefs.setdefault(subject, {})[predicate] = max(0.0, min(1.0, confidence))

    def get_beliefs(self, subject: str) -> Dict[str, float]:
        """
        Retrieve all belief edges for a given subject.
        """
        return self.beliefs.get(subject, {})

    def query_belief(self, subject: str, predicate: str) -> float:
        """
        Get confidence of a specific belief; returns 0.0 if not found.
        """
        return self.beliefs.get(subject, {}).get(predicate, 0.0)

    def remove_belief(self, subject: str, predicate: str) -> None:
        """
        Remove a specific belief edge.
        """
        if subject in self.beliefs and predicate in self.beliefs[subject]:
            del self.beliefs[subject][predicate]
            if not self.beliefs[subject]:
                del self.beliefs[subject]
