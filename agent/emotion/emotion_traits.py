"""
emotion_traits.py

Defines stable personality traits and their influence on emotional responses.
Traits include curiosity, assertiveness, openness, etc.
"""

from typing import Dict

class EmotionTraits:
    """
    Stores trait values affecting emotion dynamics.
    """

    def __init__(self, traits: Dict[str, float] = None):
        """
        Initialize with default or provided traits.
        Default traits range [0.0, 1.0].
        """
        defaults = {
            "curiosity": 0.5,
            "assertiveness": 0.5,
            "openness": 0.5,
            "empathy": 0.5,
            "optimism": 0.5
        }
        self.traits: Dict[str, float] = traits.copy() if traits else defaults.copy()

    def get(self, trait: str) -> float:
        """
        Get the value of a specific trait.
        """
        return self.traits.get(trait, 0.0)

    def set(self, trait: str, value: float) -> None:
        """
        Set a trait value, clamped between 0.0 and 1.0.
        """
        self.traits[trait] = max(0.0, min(1.0, value))

    def to_dict(self) -> Dict[str, float]:
        """
        Return a copy of trait values.
        """
        return self.traits.copy()
