#!/usr/bin/env python3
"""The basics of async."""

import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """Wait_Random function to wait on given delay.

    Args:
        max_delay (int, optional): delay of waiting. Defaults to 10.

    Returns:
        int or float: a random number between 0 and max_delay
    """
    min_delay = 0

    randomnumber = random.uniform(min_delay, max_delay)

    await asyncio.sleep(randomnumber)

    return randomnumber
