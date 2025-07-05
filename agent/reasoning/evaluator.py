"""
evaluator.py

Evaluates candidate actions or content using a scoring function or LLM-based evaluator.
"""

from typing import Any, Dict, List
from .llm_interface import LLMInterface

class Evaluator:
    """
    Provides methods to evaluate and score items.
    """

    def __init__(self, llm: LLMInterface, eval_prompt: str = None):
        """
        :param llm: LLMInterface instance for evaluation prompts.
        :param eval_prompt: optional custom prompt template.
        """
        self.llm = llm
        self.eval_prompt = eval_prompt or "Evaluate the following item and score it from 0 to 1:\n\n{item}"

    def score(self, item: str) -> float:
        """
        Score a single item by sending it to the LLM.
        Returns a float between 0.0 and 1.0.
        """
        prompt = self.eval_prompt.format(item=item)
        response = self.llm.generate(prompt)
        try:
            return float(response.strip())
        except ValueError:
            # TODO: handle parsing more robustly
            return 0.0

    def rank(self, items: List[str]) -> List[Dict[str, Any]]:
        """
        Evaluate and rank multiple items.
        Returns list of dicts with keys 'item' and 'score', sorted descending.
        """
        scored = [{"item": itm, "score": self.score(itm)} for itm in items]
        return sorted(scored, key=lambda x: x["score"], reverse=True)
