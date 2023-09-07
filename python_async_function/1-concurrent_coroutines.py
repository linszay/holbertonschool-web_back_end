#!/usr/bin/env python3
"""wait_n that takes 2 int args & returns a list of all the delays"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
import random
import typing


async def wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """wait for random delay and returns it"""
    delays = []
    for _ in range(n):
        delay = random.uniform(0, max_delay)
        await asyncio.sleep(delay)
        delays.append(delay)
    return delays
