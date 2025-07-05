"""
mood_modulation.py

Adjusts agent mood based on affective state changes, external events, and personality traits.
Interfaces with AffectiveState and EmotionTraits to update mood over time.
"""

from typing import Dict
from .affective_state import AffectiveState
from .emotion_traits import EmotionTraits

class MoodModulation:
    """
    Computes mood adjustments based on changes in affective state and personality traits.
    """

    def __init__(self, state: AffectiveState, traits: EmotionTraits):
        """
        :param state: shared AffectiveState instance
        :param traits: EmotionTraits instance for personality influence
        """
        self.state = state
        self.traits = traits

    def apply_event(self, event_impact: Dict[str, float]) -> None:
        """
        Apply an external event's emotional impact to the affective state.
        Uses trait weights to scale the effect.
        :param event_impact: mapping of emotion dimensions to change amounts.
        """
        weighted_changes = {}
        for dim, delta in event_impact.items():
            weight = self.traits.get("optimism") if dim == "mood" else 1.0
            weighted_changes[dim] = delta * weight
        self.state.update(weighted_changes)

    def decay_mood(self) -> None:
        """
        Gradually decay mood towards neutral (0.0) based on trait openness.
        """
        current = self.state.get("mood")
        openness = self.traits.get("openness")
        decay_amount = (0.0 - current) * (0.1 * openness)
        self.state.update({"mood": decay_amount})

    def get_current_mood(self) -> float:
        """
        Retrieve the current mood value.
        """
        return self.state.get("mood")
