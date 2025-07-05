"""
tool_manager.py

Registry and dispatcher for agent tools (Twitter, web search, etc.).
Manages tool initialization, invocation, and shutdown.
"""

from typing import Any, Dict, Callable

class ToolManager:
    """
    Maintains mapping of tool names to callable implementations.
    """

    def __init__(self):
        """
        Initialize empty tool registry.
        """
        self._tools: Dict[str, Callable[..., Any]] = {}

    def register(self, name: str, func: Callable[..., Any]) -> None:
        """
        Register a tool by name.
        :param name: Unique tool identifier.
        :param func: Callable implementing the tool.
        """
        self._tools[name] = func

    def invoke(self, name: str, *args, **kwargs) -> Any:
        """
        Invoke a registered tool.
        :param name: Tool name.
        :raises KeyError: if tool is not registered.
        """
        if name not in self._tools:
            raise KeyError(f"Tool '{name}' not found in registry.")
        return self._tools[name](*args, **kwargs)

    def list_tools(self) -> Dict[str, Callable[..., Any]]:
        """
        Return mapping of registered tools.
        """
        return dict(self._tools)

    def shutdown_all(self) -> None:
        """
        Call shutdown() on all tools that have it.
        """
        for tool in self._tools.values():
            shutdown_method = getattr(tool, "shutdown", None)
            if callable(shutdown_method):
                shutdown_method()
