"""
self_critic.py

Analyzes agent decisions and behaviors to provide critical feedback and identify improvement opportunities.
"""

from typing import Dict, Any, List
from ..memory.reflective_memory import ReflectiveMemory
from ..reasoning.llm_interface import LLMInterface

class SelfCritic:
    """
    Generates critiques for past actions and outcomes to guide self-improvement.
    """

    def __init__(self, llm: LLMInterface, reflective_memory: ReflectiveMemory):
        """
        :param llm: LLMInterface for critique generation.
        :param reflective_memory: ReflectiveMemory to store criticism insights.
        """
        self.llm = llm
        self.reflective = reflective_memory

    def critique_action(self, action_summary: str, outcome_summary: str) -> str:
        """
        Use LLM to critique a specific action vs its outcome.
        """
        prompt = (
            "Please provide a critical analysis of the following action and outcome:\n"
            f"Action: {action_summary}\nOutcome: {outcome_summary}\n"
        )
        critique = self.llm.generate(prompt)
        self.reflective.add_insight(critique, {"type": "critique"})
        return critique

    def review_recent(self, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve recent reflective or critique entries.
        """
        return self.reflective.query_insights("", limit)
