"""
topic_graph.py

Maintains a graph of topics and their relationships based on trending data and interactions.
"""

from typing import Dict, List

class TopicGraph:
    """
    Represents topic nodes and weighted edges for semantic proximity and trend analysis.
    """

    def __init__(self):
        """
        Initialize empty topic graph.
        """
        # mapping topic to dict of {related_topic: weight}
        self.graph: Dict[str, Dict[str, float]] = {}

    def add_topic(self, topic: str) -> None:
        """
        Ensure a topic node exists.
        """
        self.graph.setdefault(topic, {})

    def add_edge(self, topic_a: str, topic_b: str, weight: float = 1.0) -> None:
        """
        Add or increase weight of edge between two topics.
        """
        self.add_topic(topic_a)
        self.add_topic(topic_b)
        current = self.graph[topic_a].get(topic_b, 0.0)
        self.graph[topic_a][topic_b] = current + weight

    def get_related(self, topic: str) -> Dict[str, float]:
        """
        Return related topics and their weights.
        """
        return self.graph.get(topic, {})

    def remove_topic(self, topic: str) -> None:
        """
        Remove a topic node and all edges to/from it.
        """
        self.graph.pop(topic, None)
        for neighbors in self.graph.values():
            neighbors.pop(topic, None)

    def trending_topics(self, min_weight: float = 1.0) -> List[str]:
        """
        Return list of topics whose total edge weight exceeds threshold.
        """
        return [
            topic
            for topic, edges in self.graph.items()
            if sum(edges.values()) >= min_weight
        ]
