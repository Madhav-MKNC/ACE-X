"""
Dialogue Manager: Handles conversation flow, dialogue state, and message routing for the agent.
Supports multi-turn interactions and persona-aware responses.
"""
from typing import List, Dict, Any

class DialogueManager:
    def __init__(self):
        self.dialogue_history = []  # List of (sender, message) tuples
        self.state = {}

    def receive_message(self, sender: str, message: str):
        """Add a message to the dialogue history."""
        self.dialogue_history.append((sender, message))

    def get_history(self, limit: int = 10) -> List[tuple]:
        """Return the most recent dialogue turns."""
        return self.dialogue_history[-limit:]

    def generate_response(self, context: Dict[str, Any] = None) -> str:
        """
        Generate a response based on dialogue history and optional context.
        :param context: Optional context (persona, emotion, etc.)
        :return: Response string
        """
        if not self.dialogue_history:
            return "Hello! How can I help you today?"
        last_sender, last_message = self.dialogue_history[-1]
        # Placeholder: echo last message with persona-aware prefix
        persona = context.get('persona', 'Agent') if context else 'Agent'
        return f"{persona}: I received your message: '{last_message}'"

    def clear_history(self):
        """Clear the dialogue history."""
        self.dialogue_history.clear()

    def __repr__(self):
        return f"<DialogueManager: {len(self.dialogue_history)} turns>"
