#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments"""
import asyncio
import random


async def async_generator():
    """loop and wait 1 sec then yield a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
