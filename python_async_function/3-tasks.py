#!/usr/bin/env python3
"""Write a function using the regular function syntax instead of async"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return asyncio.Task using type annotation & asyncio.create_task"""
    return asyncio.create_task(wait_random(max_delay))
