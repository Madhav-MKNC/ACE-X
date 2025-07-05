"""
Global Strategy Layer: Derives long-term strategic goals and behavioral guidelines from the agent's aspirations and current world state.
Integrates with the Aspirational Layer to formulate high-level strategies.
"""
from typing import List, Dict, Any

class GlobalStrategyLayer:
    def __init__(self, aspirational_layer):
        """
        Initialize the Global Strategy Layer.
        :param aspirational_layer: Instance of AspirationalLayer
        """
        self.aspirational_layer = aspirational_layer
        self.current_strategy = None
        self.strategy_history = []

    def formulate_strategy(self, world_state: Dict[str, Any]) -> str:
        """
        Generate a high-level strategy based on aspirations and world state.
        :param world_state: Dictionary representing the agent's perception of the world
        :return: A string describing the current global strategy
        """
        # Example: Use core principles to influence strategy
        principles = self.aspirational_layer.get_principles()
        # Placeholder logic: combine principles and world state summary
        summary = world_state.get('summary', 'No world state provided.')
        strategy = f"Act according to: {', '.join(principles[:2]) if principles else 'No principles'} | World: {summary}"
        self.current_strategy = strategy
        self.strategy_history.append(strategy)
        return strategy

    def get_current_strategy(self) -> str:
        """Return the most recent global strategy."""
        return self.current_strategy

    def get_strategy_history(self) -> List[str]:
        """Return the history of generated strategies."""
        return self.strategy_history

    def __repr__(self):
        return f"<GlobalStrategyLayer: {len(self.strategy_history)} strategies generated>"
