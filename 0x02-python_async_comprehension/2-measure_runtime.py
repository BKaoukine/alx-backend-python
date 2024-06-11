#!/usr/bin/env python3
"""Async Generator.

Yields:
    Iterator: Random float from 0 to 10
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime Coroutine function will loop 10 times.

    each time asynchronously. wait 1 second.
    then yield a random number between 0 and 10.

    Returns:
        AsyncGenerator[float,None]: Iterator that holds random floats

    Yields:
        Iterator[AsyncGenerator[float,None]]: random floats between 0-10
    """
    runtime = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - runtime
