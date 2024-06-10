#!/usr/bin/env python3
"""The basics of async."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time func will measures the total execution time for wait_n.

    Args:
        n (int): number of spawns
        max_delay (int): num  of max delay

    Returns:
        float: runtime of the wait_n
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    runtime = end_time - start_time

    return(runtime/n)
