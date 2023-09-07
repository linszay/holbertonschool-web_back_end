#!/usr/bin/env python3
"""write a coroutine called async_comprehension that takes no arguments"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """collect 10 random numbers and return them as a list"""
    return [num async for num in async_generator()]
