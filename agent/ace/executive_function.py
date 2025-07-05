"""
Executive Function Layer: Converts high-level strategies into concrete plans and allocates resources for execution.
Acts as the project manager, breaking down strategies into actionable tasks.
"""

from typing import List, Dict, Any

class ExecutiveFunctionLayer:
    def __init__(self, agent_model_layer):
        """
        Initialize the Executive Function Layer.
        :param agent_model_layer: Instance of AgentModelLayer
        """
        self.agent_model_layer = agent_model_layer
        self.current_plan = []
        self.plan_history = []

    def generate_plan(self, strategy: str, context: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Generate a list of actionable tasks from a high-level strategy.
        :param strategy: The current global strategy string
        :param context: Optional context (e.g., telemetry, world state)
        :return: List of task dictionaries
        """
        # Placeholder logic: break strategy into simple tasks
        tasks = []
        if 'tweet' in self.agent_model_layer.get_capabilities():
            tasks.append({'action': 'tweet', 'content': f"Thoughts on: {strategy}"})
        if 'follow' in self.agent_model_layer.get_capabilities():
            tasks.append({'action': 'follow', 'criteria': 'AI researchers'})
        self.current_plan = tasks
        self.plan_history.append(tasks)
        return tasks

    def get_current_plan(self) -> List[Dict[str, Any]]:
        """Return the current plan (list of tasks)."""
        return self.current_plan

    def get_plan_history(self) -> List[List[Dict[str, Any]]]:
        """Return the history of generated plans."""
        return self.plan_history

    def __repr__(self):
        return f"<ExecutiveFunctionLayer: {len(self.plan_history)} plans generated>"
