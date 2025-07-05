"""
ACE Layer Interfaces and Abstractions
Defines abstract base classes (ABCs) for each ACE layer to standardize their interfaces and enable flexible implementation or mocking.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List

class IAspirationalLayer(ABC):
    @abstractmethod
    def get_principles(self) -> List[str]:
        pass

class IGlobalStrategyLayer(ABC):
    @abstractmethod
    def formulate_strategy(self, world_state: Dict[str, Any]) -> str:
        pass
    @abstractmethod
    def get_current_strategy(self) -> str:
        pass

class IAgentModelLayer(ABC):
    @abstractmethod
    def get_identity(self) -> Dict[str, Any]:
        pass
    @abstractmethod
    def get_capabilities(self) -> list:
        pass
    @abstractmethod
    def get_telemetry(self) -> Dict[str, Any]:
        pass

class IExecutiveFunctionLayer(ABC):
    @abstractmethod
    def generate_plan(self, strategy: str, context: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        pass
    @abstractmethod
    def get_current_plan(self) -> List[Dict[str, Any]]:
        pass

class ICognitiveControlLayer(ABC):
    @abstractmethod
    def select_task(self, plan: List[Dict[str, Any]]) -> Dict[str, Any]:
        pass
    @abstractmethod
    def get_emotion_state(self) -> Dict[str, Any]:
        pass

class ITaskProsecutionLayer(ABC):
    @abstractmethod
    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        pass
    @abstractmethod
    def get_last_result(self) -> Dict[str, Any]:
        pass
