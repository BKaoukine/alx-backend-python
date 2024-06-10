#!/usr/bin/env python3
"""The basics of async."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n, max_delay):
    """measure_time func will measures the total execution time for wait_n.
    Args:
        n (int): number of spawns
        max_delay (int): num  of max delay

    Returns:
        float: runtime of the wait_n
    """
    
    await wait_n(n,max_delay)
    
    runtime = time.time
    
    return(runtime/n)
