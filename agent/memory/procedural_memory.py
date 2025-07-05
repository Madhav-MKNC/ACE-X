"""
procedural_memory.py

Procedural memory stores skills or methods for tasks the agent can perform.
Supports registering procedures and invoking them by name with parameters.
"""

from typing import Any, Callable, Dict, List, Optional

class ProceduralMemory:
    """
    Manages procedural memory of named operations or skills.
    """

    def __init__(self):
        """
        Initialize the procedural memory registry.
        """
        self._procedures: Dict[str, Callable[..., Any]] = {}

    def register(self, name: str, func: Callable[..., Any]) -> None:
        """
        Register a procedure by name.
        :param name: Unique identifier for the procedure.
        :param func: Callable implementing the procedure.
        """
        self._procedures[name] = func

    def execute(self, name: str, *args, **kwargs) -> Any:
        """
        Execute a registered procedure.
        :param name: Procedure name.
        :raises KeyError: if procedure not found.
        """
        if name not in self._procedures:
            raise KeyError(f"Procedure '{name}' not found in procedural memory.")
        return self._procedures[name](*args, **kwargs)

    def list_procedures(self) -> List[str]:
        """
        List all registered procedure names.
        """
        return list(self._procedures.keys())

    def unregister(self, name: str) -> None:
        """
        Remove a procedure from memory.
        """
        if name in self._procedures:
            del self._procedures[name]
