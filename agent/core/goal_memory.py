"""
goal_memory.py

Tracks short-term and long-term goals, progress, and completion status.
"""

from typing import Dict, List, Optional
import datetime

class GoalMemory:
    """
    Manages goals for the agent: creation, tracking, and retrieval.
    """

    def __init__(self):
        """
        Initialize goal storage.
        """
        self._goals: Dict[str, Dict] = {}

    def add_goal(self, goal_id: str, description: str, due: Optional[datetime.datetime] = None) -> None:
        """
        Add a new goal with optional due time.
        """
        self._goals[goal_id] = {
            "description": description,
            "created": datetime.datetime.utcnow(),
            "due": due,
            "completed": False,
            "completed_at": None
        }

    def complete_goal(self, goal_id: str) -> None:
        """
        Mark a goal as completed.
        """
        if goal_id in self._goals:
            self._goals[goal_id]["completed"] = True
            self._goals[goal_id]["completed_at"] = datetime.datetime.utcnow()

    def get_goal(self, goal_id: str) -> Optional[Dict]:
        """
        Retrieve goal details by ID.
        """
        return self._goals.get(goal_id)

    def list_goals(self, include_completed: bool = False) -> List[Dict]:
        """
        List all goals, optionally filtering out completed.
        """
        return [
            info for info in self._goals.values()
            if include_completed or not info["completed"]
        ]

    def remove_goal(self, goal_id: str) -> None:
        """
        Delete a goal from memory.
        """
        if goal_id in self._goals:
            del self._goals[goal_id]
