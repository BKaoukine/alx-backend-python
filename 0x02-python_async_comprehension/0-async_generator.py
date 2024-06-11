#!/usr/bin/env python3
"""Async Generator.

Yields:
    Iterator: Random float from 0 to 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """Async_generatorCoroutine function will loop 10 times.

    each time asynchronously. wait 1 second.
    then yield a random number between 0 and 10.

    Returns:
        AsyncGenerator[float,None]: Iterator that holds random floats

    Yields:
        Iterator[AsyncGenerator[float,None]]: random floats between 0-10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
