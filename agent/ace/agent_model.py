"""
agent_model.py

Maintains the agent’s self‐model: capabilities, rate limits, performance metrics, and configuration.
"""

from typing import Dict, Any

class AgentModel:
    """
    Represents the agent's introspective self‐state.
    """

    def __init__(self,
                 capabilities: Dict[str, bool] = None,
                 rate_limits: Dict[str, Any] = None,
                 performance: Dict[str, float] = None):
        """
        :param capabilities: mapping of action name to availability.
        :param rate_limits: API or action rate‐limit settings.
        :param performance: prior success/failure metrics.
        """
        self.capabilities = capabilities.copy() if capabilities else {
            "tweet": True, "reply": True, "follow": True}
        self.rate_limits = rate_limits.copy() if rate_limits else {}
        self.performance = performance.copy() if performance else {}

    def update_capabilities(self, updates: Dict[str, bool]) -> None:
        """
        Enable or disable capabilities dynamically.
        """
        self.capabilities.update(updates)

    def record_performance(self, action: str, success: bool) -> None:
        """
        Log outcome metrics for an action.
        """
        self.performance.setdefault(action, {"success": 0, "failure": 0})
        if success:
            self.performance[action]["success"] += 1
        else:
            self.performance[action]["failure"] += 1

    def get_status(self) -> Dict[str, Any]:
        """
        Return a summary of capabilities, rate limits, and performance.
        """
        return {
            "capabilities": dict(self.capabilities),
            "rate_limits": dict(self.rate_limits),
            "performance": dict(self.performance)
        }
