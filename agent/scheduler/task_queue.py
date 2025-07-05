"""
task_queue.py

Manages scheduling and execution queue of tasks with retry and trigger capabilities.
"""

import asyncio
from typing import Any, Dict, List, Callable, Awaitable

class TaskQueue:
    """
    Async task queue that holds tasks and dispatches them on demand.
    """

    def __init__(self):
        """
        Initialize empty task queue.
        """
        self._queue: asyncio.Queue = asyncio.Queue()
        self._running = False

    async def add_task(self, task: Dict[str, Any]) -> None:
        """
        Add a task descriptor to the queue.
        """
        await self._queue.put(task)

    async def run(self, handler: Callable[[Dict[str, Any]], Awaitable[Any]]) -> None:
        """
        Continuously run tasks by invoking handler for each queued task.
        """
        if self._running:
            return
        self._running = True
        while self._running:
            task = await self._queue.get()
            try:
                await handler(task)
            except Exception:
                # TODO: add error handling or retry logic
                pass
            finally:
                self._queue.task_done()

    def stop(self) -> None:
        """
        Stop processing tasks.
        """
        self._running = False
