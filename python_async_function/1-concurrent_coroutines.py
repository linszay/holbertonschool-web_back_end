#!/usr/bin/env python3
"""wait_n that takes 2 int args & returns a list of all the delays"""
import asyncio
import random
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """wait for random delay and returns it"""
    delays = []
    for _ in range(n):
        delay = random.uniform(0, max_delay)
        await asyncio.sleep(delay)
        delays.append(delay)
        """sorting the list"""
        for i in range(len(delays)):
            for j in range(len(delays) - i - 1):
                if delays[j] > delays[j + 1]:
                    delays[j], delays[j + 1] = delays[j + 1], delays[j]
    return delays
