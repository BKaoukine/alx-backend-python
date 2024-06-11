#!/usr/bin/env python3
"""Async Generator.

Yields:
    Iterator: Random float from 0 to 10
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async_comprehension Coroutine function will loop 10 times.

    each time asynchronously. wait 1 second.
    then yield a random number between 0 and 10.

    Returns:
        AsyncGenerator[float,None]: Iterator that holds random floats

    Yields:
        Iterator[AsyncGenerator[float,None]]: random floats between 0-10
    """
    lista = async_generator()

    return [item async for item in lista]
