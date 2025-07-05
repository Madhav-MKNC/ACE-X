"""
meta_governor.py

Meta-cognitive governance: oversees self-reflection, critique, and self-improvement logic.
"""

from typing import Any, Dict, List
from ..reasoning.llm_interface import LLMInterface
from ..memory.reflective_memory import ReflectiveMemory

class MetaGovernor:
    """
    Performs higher-order evaluation of agent behavior and self-updates.
    """

    def __init__(self,
                 llm: LLMInterface,
                 reflective_memory: ReflectiveMemory):
        """
        :param llm: LLMInterface for generating critiques and rewrites.
        :param reflective_memory: ReflectiveMemory instance for storing insights.
        """
        self.llm = llm
        self.reflective = reflective_memory

    def critique(self, action_summary: str, outcome_summary: str) -> str:
        """
        Generate a critique of an action against its outcome.
        :param action_summary: description of the action taken.
        :param outcome_summary: description of the outcome.
        :return: critique text.
        """
        prompt = (
            "Critique the following action vs outcome:\n\n"
            f"Action: {action_summary}\nOutcome: {outcome_summary}\n\n"
            "Provide constructive feedback."
        )
        return self.llm.generate(prompt)

    def add_insight(self, insight: str, metadata: Dict[str, Any] = None) -> None:
        """
        Log a new reflective insight.
        """
        self.reflective.add_insight(insight, metadata)

    def self_improve(self, critique_text: str) -> None:
        """
        Use critique to propose improvements to strategies or goals.
        :param critique_text: text from critique() method.
        """
        # TODO: implement self-rewriting based on critique
        pass

    def review_reflections(self, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve recent reflective insights for reporting or act planning.
        """
        return self.reflective.query_insights("", limit)
