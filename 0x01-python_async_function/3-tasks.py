#!/usr/bin/env python3
"""The basics of async."""

import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Task_wait_random that takes an integer max_delay.

    and returns a asyncio.Task..
    Args:
        max_delay (int): num  of max delay

    Returns:
        Object: aysncio task object
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
