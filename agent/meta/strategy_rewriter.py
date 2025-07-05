"""
strategy_rewriter.py

Proposes modifications to the agent’s global strategy based on reflective insights and performance feedback.
"""

from typing import Dict, Any, List
from ..reasoning.llm_interface import LLMInterface
from ..memory.reflective_memory import ReflectiveMemory

class StrategyRewriter:
    """
    Uses reflective insights and historical strategy outcomes to adjust future planning.
    """

    def __init__(self,
                 llm: LLMInterface,
                 reflective_memory: ReflectiveMemory):
        """
        :param llm: LLMInterface for generating strategy rewrite suggestions.
        :param reflective_memory: ReflectiveMemory instance with past insights.
        """
        self.llm = llm
        self.reflective = reflective_memory

    def rewrite(self, current_strategy: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a revised strategy plan.
        :param current_strategy: existing global strategy dict.
        :return: modified strategy dict.
        """
        insights = self.reflective.get_all()
        prompt = (
            "Based on these reflective insights and the current strategy, suggest improvements:\n\n"
            f"Insights: {insights}\n"
            f"Current Strategy: {current_strategy}\n\n"
            "Provide a JSON-formatted revised strategy."
        )
        response = self.llm.generate(prompt)
        try:
            import json
            return json.loads(response)
        except Exception:
            return {"raw_rewrite": response}
