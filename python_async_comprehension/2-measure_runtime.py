#!/usr/bin/env python3
"""coroutine will execute 4x in parallel using asyncio.gather"""
import typing
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures total runtime and returns it"""
    start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = time.time()
    return end - start
