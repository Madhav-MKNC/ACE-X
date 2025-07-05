"""
agent_map.py

Represents spatial and relational map of agents and entities in the environment.
"""

from typing import Dict, Any, List

class AgentMap:
    """
    Maintains positions, relationships, and encounter history of entities.
    """

    def __init__(self):
        """
        Initialize empty agent map.
        """
        # mapping entity_id to attributes (location, last_seen, relations)
        self.entities: Dict[str, Dict[str, Any]] = {}

    def add_entity(self, entity_id: str, attributes: Dict[str, Any]) -> None:
        """
        Add or update an entity in the map.
        """
        self.entities[entity_id] = attributes

    def get_entity(self, entity_id: str) -> Dict[str, Any]:
        """
        Retrieve stored attributes for an entity.
        """
        return self.entities.get(entity_id, {})

    def list_entities(self) -> List[str]:
        """
        Return list of known entity IDs.
        """
        return list(self.entities.keys())

    def remove_entity(self, entity_id: str) -> None:
        """
        Remove an entity from the map.
        """
        if entity_id in self.entities:
            del self.entities[entity_id]
