"""
affective_state.py

Tracks the agent's current affective state including mood, frustration, and other emotional indicators.
"""

from typing import Dict, Any

class AffectiveState:
    """
    Manages dynamic affective state variables for the agent.
    """

    def __init__(self, initial_state: Dict[str, float] = None):
        """
        Initialize the affective state with optional initial values.
        :param initial_state: mapping of emotion dimensions to initial values.
        """
        # Default dimensions: mood [-1.0, 1.0], frustration [0.0, 1.0], energy [0.0, 1.0]
        defaults = {"mood": 0.0, "frustration": 0.0, "energy": 1.0}
        self.state: Dict[str, float] = initial_state.copy() if initial_state else defaults.copy()

    def update(self, changes: Dict[str, float]) -> None:
        """
        Apply additive changes to affective dimensions.
        Clamps values within their valid ranges.
        :param changes: mapping of emotion dimension to change amount.
        """
        for dim, delta in changes.items():
            if dim not in self.state:
                continue
            new_val = self.state[dim] + delta
            # clamp ranges
            if dim == "mood":
                self.state[dim] = max(-1.0, min(1.0, new_val))
            else:
                self.state[dim] = max(0.0, min(1.0, new_val))

    def get(self, dimension: str) -> float:
        """
        Retrieve the current value of an affective dimension.
        :param dimension: e.g. "mood", "frustration", "energy".
        :return: current numeric value.
        """
        return self.state.get(dimension, 0.0)

    def to_dict(self) -> Dict[str, float]:
        """
        Return a copy of the current affective state.
        """
        return self.state.copy()
