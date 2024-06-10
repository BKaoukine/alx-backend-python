#!/usr/bin/env python3
"""The basics of async."""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Wait_n func will spawn wait_random n times with the specified max_delay.

    Args:
        n (int): number of spawns
        max_delay (int): num  of max delay

    Returns:
        list: list of delays
    """
    delays = []

    while (n > 0):
        numDelay = await task_wait_random(max_delay)
        delays.append(numDelay)
        n -= 1

    return delays
