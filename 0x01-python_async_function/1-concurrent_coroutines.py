#!/usr/bin/env python3
"""The basics of async."""

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Wait_n func will spawn wait_random n times with the specified max_delay.

    Args:
        n (int): number of spawns
        max_delay (int): num  of max delay

    Returns:
        list: list of delays
    """
    delays = []

    while (n > 0):
        numDelay = await wait_random(max_delay)
        delays.append(numDelay)
        n -= 1

    
    return delays
