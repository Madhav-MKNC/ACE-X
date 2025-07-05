"""
interfaces.py

Defines interfaces for ACE framework layers to interact with external components.
Includes abstract definitions for each ACE layer.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List

class AspirationalInterface(ABC):
    @abstractmethod
    def load_constitution(self) -> None: ...
    @abstractmethod
    def evaluate_principles(self, context: Dict[str, Any]) -> Dict[str, float]: ...

class GlobalStrategyInterface(ABC):
    @abstractmethod
    def formulate(self, world_state: Dict[str, Any], trends: List[str]) -> Dict[str, Any]: ...

class AgentModelInterface(ABC):
    @abstractmethod
    def update_capabilities(self, updates: Dict[str, bool]) -> None: ...
    @abstractmethod
    def record_performance(self, action: str, success: bool) -> None: ...

class ExecutiveFunctionInterface(ABC):
    @abstractmethod
    def plan_daily(self, strategy_output: Dict[str, Any]) -> List[Dict[str, Any]]: ...
    @abstractmethod
    def plan_tweets(self, task: Dict[str, Any]) -> List[Dict[str, Any]]: ...

class CognitiveControlInterface(ABC):
    @abstractmethod
    def should_pause(self) -> bool: ...
    @abstractmethod
    def select_next_task(self, tasks: List[Dict[str, Any]]) -> Dict[str, Any]: ...

class TaskProsecutionInterface(ABC):
    @abstractmethod
    def execute_action(self, name: str, params: Dict[str, Any]) -> Any: ...
