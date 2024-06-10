#!/usr/bin/env python3
"""The basics of async."""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait_n func will spawn wait_random n times with the specified max_delay.

    Args:
        n (int): number of spawns
        max_delay (int): num  of max delay

    Returns:
        list: list of delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
