"""
Task Prosecution Layer: Executes actions via APIs (e.g., Twitter), monitors results, and reports outcomes.
Acts as the interface between the agent's plans and the external world.
"""
from typing import Dict, Any

class TaskProsecutionLayer:
    def __init__(self, tool_interfaces=None):
        """
        Initialize the Task Prosecution Layer.
        :param tool_interfaces: Optional dictionary of tool interfaces (e.g., Twitter client)
        """
        self.tool_interfaces = tool_interfaces or {}
        self.last_result = None
        self.action_log = []

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a single task using the appropriate tool interface.
        :param task: Task dictionary (e.g., {'action': 'tweet', ...})
        :return: Result dictionary (success, details, etc.)
        """
        action = task.get('action')
        result = {'success': False, 'details': 'No interface for action.'}
        if action in self.tool_interfaces:
            try:
                # Call the tool interface's execute method
                result = self.tool_interfaces[action].execute(task)
            except Exception as e:
                result = {'success': False, 'details': str(e)}
        self.last_result = result
        self.action_log.append({'task': task, 'result': result})
        return result

    def get_last_result(self) -> Dict[str, Any]:
        """Return the result of the last executed task."""
        return self.last_result

    def get_action_log(self) -> list:
        """Return the log of all executed actions and their results."""
        return self.action_log

    def __repr__(self):
        return f"<TaskProsecutionLayer: {len(self.action_log)} actions executed>"
