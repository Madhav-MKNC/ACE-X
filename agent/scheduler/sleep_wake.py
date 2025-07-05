"""
sleep_wake.py

Manages agent sleep/wake cycles based on configurable schedule or external triggers.
"""

import asyncio
from datetime import datetime, time
from typing import Callable, Awaitable, Optional

class SleepWake:
    """
    Handles sleep-wake scheduling for the agent.
    """

    def __init__(self,
                 wake_time: time,
                 sleep_time: time,
                 on_wake: Callable[[], Awaitable[None]],
                 on_sleep: Callable[[], Awaitable[None]]):
        """
        :param wake_time: daily time to wake agent.
        :param sleep_time: daily time to put agent to sleep.
        :param on_wake: async callback when waking.
        :param on_sleep: async callback when sleeping.
        """
        self.wake_time = wake_time
        self.sleep_time = sleep_time
        self.on_wake = on_wake
        self.on_sleep = on_sleep
        self._task: Optional[asyncio.Task] = None
        self._running = False

    async def _run(self) -> None:
        """
        Internal loop checking current time against wake/sleep schedule.
        """
        while self._running:
            now = datetime.utcnow().time()
            if now >= self.wake_time and now < self.sleep_time:
                await self.on_wake()
            else:
                await self.on_sleep()
            # Sleep for a minute before next check
            await asyncio.sleep(60)

    def start(self) -> None:
        """
        Start the sleep-wake loop.
        """
        if self._running:
            return
        self._running = True
        self._task = asyncio.create_task(self._run())

    def stop(self) -> None:
        """
        Stop sleep-wake scheduling.
        """
        self._running = False
        if self._task:
            self._task.cancel()
            self._task = None
