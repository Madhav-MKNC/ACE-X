"""
frustration_model.py

Models frustration accumulation based on failed actions and unmet expectations.
Provides methods to increase, decay, and threshold trigger impacts on cognitive control.
"""

from typing import Dict

class FrustrationModel:
    """
    Tracks and updates agent frustration over time.
    """

    def __init__(self,
                 decay_rate: float = 0.1,
                 threshold: float = 0.7):
        """
        :param decay_rate: amount to reduce frustration per decay cycle.
        :param threshold: level at which high frustration state is triggered.
        """
        self.frustration: float = 0.0
        self.decay_rate = decay_rate
        self.threshold = threshold

    def increase(self, amount: float) -> None:
        """
        Increase frustration by amount, clamped to [0.0, 1.0].
        """
        self.frustration = min(1.0, self.frustration + amount)

    def decay(self) -> None:
        """
        Decay frustration by decay_rate, not dropping below 0.0.
        """
        self.frustration = max(0.0, self.frustration - self.decay_rate)

    def is_high(self) -> bool:
        """
        Check if frustration has reached or exceeded threshold.
        """
        return self.frustration >= self.threshold

    def reset(self) -> None:
        """
        Reset frustration to baseline zero.
        """
        self.frustration = 0.0

    def to_dict(self) -> Dict[str, float]:
        """
        Return current frustration value and threshold.
        """
        return {"frustration": self.frustration, "threshold": self.threshold}
