"""
Cognitive Control Layer: Manages task selection, switching, and emotional/operational blocks.
Handles interruptions, frustration modeling, and decision arbitration.
"""

from typing import List, Dict, Any

class CognitiveControlLayer:
    def __init__(self, emotion_state: Dict[str, Any] = None):
        """
        Initialize the Cognitive Control Layer.
        :param emotion_state: Optional dictionary representing the agent's current emotional state
        """
        self.emotion_state = emotion_state or {'mood': 'neutral', 'frustration': 0}
        self.last_action = None
        self.frustration_threshold = 5

    def select_task(self, plan: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Select the next task to execute, considering emotional state and frustration.
        :param plan: List of planned tasks
        :return: The selected task dictionary
        """
        if not plan:
            return None
        # Example: If frustrated, skip to a different task
        if self.emotion_state.get('frustration', 0) > self.frustration_threshold:
            # Try to pick a different type of task
            for task in plan:
                if task['action'] != self.last_action:
                    self.last_action = task['action']
                    return task
        # Default: pick the first task
        self.last_action = plan[0]['action']
        return plan[0]

    def update_emotion(self, key: str, value: Any):
        """Update the agent's emotional state."""
        self.emotion_state[key] = value

    def get_emotion_state(self) -> Dict[str, Any]:
        """Return the current emotional state."""
        return self.emotion_state

    def __repr__(self):
        return f"<CognitiveControlLayer: mood={self.emotion_state.get('mood')}, frustration={self.emotion_state.get('frustration')}>"
