"""
heartbeat.py

Async heartbeat to trigger agent ticks at regular intervals.
"""

import asyncio
from typing import Callable, Awaitable, Optional

class Heartbeat:
    """
    Runs a periodic heartbeat to invoke a callback function on each tick.
    """

    def __init__(self, interval: float, callback: Callable[[], Awaitable[None]]):
        """
        :param interval: time between ticks in seconds.
        :param callback: async function to call on each tick.
        """
        self.interval = interval
        self.callback = callback
        self._task: Optional[asyncio.Task] = None
        self._running = False

    async def _run(self) -> None:
        """
        Internal loop that schedules callback periodically.
        """
        while self._running:
            try:
                await self.callback()
            except Exception:
                # TODO: add logging or error handling
                pass
            await asyncio.sleep(self.interval)

    def start(self) -> None:
        """
        Start the heartbeat loop.
        """
        if self._running:
            return
        self._running = True
        self._task = asyncio.create_task(self._run())

    def stop(self) -> None:
        """
        Stop the heartbeat loop.
        """
        self._running = False
        if self._task:
            self._task.cancel()
            self._task = None
