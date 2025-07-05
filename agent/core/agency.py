"""
agency.py

Coordinates high-level decision making: integrates perception, planning, evaluation, and action execution.
"""

from typing import Any, Dict, List
from ..tools.tool_manager import ToolManager
from ..reasoning.evaluator import Evaluator
from ..reasoning.reasoning_chain import ReasoningChain

class Agency:
    """
    Central decision-making component that selects actions based on context and reasoning.
    """

    def __init__(self,
                 tools: ToolManager,
                 evaluator: Evaluator,
                 reasoning_chain: ReasoningChain):
        """
        :param tools: ToolManager with available action tools.
        :param evaluator: Evaluator instance for scoring actions.
        :param reasoning_chain: ReasoningChain for planning.
        """
        self.tools = tools
        self.evaluator = evaluator
        self.reasoning = reasoning_chain

    def propose_actions(self, context: Dict[str, Any]) -> List[str]:
        """
        Generate a list of possible actions based on context.
        TODO: define set of action templates or tool calls.
        """
        # Placeholder: list of dummy actions
        return ["tweet", "reply", "follow"]

    def select_action(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Use reasoning chain and evaluator to choose best action.
        :param context: current situational context.
        :return: dict with 'name' and 'params' for the tool.
        """
        actions = self.propose_actions(context)
        result = self.reasoning.react(str(context), actions)
        action_name = result.get("action")  # e.g., "tweet"
        # Placeholder for mapping name to tool parameters
        return {"name": action_name, "params": context}

    def execute(self, action: Dict[str, Any]) -> Any:
        """
        Invoke the selected tool with parameters.
        """
        name = action.get("name")
        params = action.get("params", {})
        return self.tools.invoke(name, **params)
