"""
emotion_engine.py

Coordinates affective state updates, frustration tracking, and mood modulation in the agent.
"""

from typing import Dict
from ..emotion.affective_state import AffectiveState
from ..emotion.emotion_traits import EmotionTraits
from ..emotion.frustration_model import FrustrationModel
from ..emotion.mood_modulation import MoodModulation

class EmotionEngine:
    """
    Oversees the agent's emotional dynamics and interfaces with decision and expression systems.
    """

    def __init__(self,
                 initial_traits: Dict[str, float] = None):
        """
        :param initial_traits: optional initial personality traits.
        """
        self.state = AffectiveState()
        self.traits = EmotionTraits(initial_traits)
        self.frustration_model = FrustrationModel()
        self.modulator = MoodModulation(self.state, self.traits)

    def apply_event(self, impact: Dict[str, float]) -> None:
        """
        Apply an external event to the affective state and update frustration if needed.
        """
        self.modulator.apply_event(impact)
        # Map event impact to frustration increase
        if impact.get("mood", 0.0) < 0:
            self.frustration_model.increase(abs(impact["mood"]) * 0.5)

    def decay(self) -> None:
        """
        Gradually decay mood and frustration over time.
        """
        self.modulator.decay_mood()
        self.frustration_model.decay()

    def is_frustrated(self) -> bool:
        """
        Check if frustration is above threshold.
        """
        return self.frustration_model.is_high()

    def get_emotional_profile(self) -> Dict[str, float]:
        """
        Return a snapshot of current emotions and traits.
        """
        profile = self.state.to_dict()
        profile.update(self.traits.to_dict())
        profile["frustration"] = self.frustration_model.frustration
        return profile


class EmotionEngine0:
    def __init__(self):
        self.state = {
            "mood": "neutral",
            "valence": 0.0,  # -1 to +1
            "arousal": 0.0,
        }
        self.traits = {
            "sensitivity": 0.7,
            "resilience": 0.5,
            "empathy": 0.6,
        }

    def update(self, event_valence: float):
        delta = event_valence * self.traits["sensitivity"]
        self.state["valence"] += delta
        self.state["valence"] = max(-1.0, min(1.0, self.state["valence"]))
        self._recalculate_mood()

    def _recalculate_mood(self):
        v = self.state["valence"]
        if v > 0.5:
            self.state["mood"] = "elated"
        elif v > 0.1:
            self.state["mood"] = "positive"
        elif v < -0.5:
            self.state["mood"] = "distressed"
        elif v < -0.1:
            self.state["mood"] = "negative"
        else:
            self.state["mood"] = "neutral"

    def current_emotion(self):
        return self.state.copy()

