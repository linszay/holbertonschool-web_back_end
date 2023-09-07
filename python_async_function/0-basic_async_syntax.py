#!/usr/bin/env python3
"""takes in an integer argument (max_delay, with a default value of 10) & waits for a random delay between 0 and max_delay"""
import asyncio
import random

async def wait_random(max_delay=10):
    """wait for random delay and returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
