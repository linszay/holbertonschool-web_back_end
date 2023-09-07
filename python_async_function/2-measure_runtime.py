#!/usr/bin/env python3
"""func measures the total execution time for wait_n(n, max_delay)"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """returns total_time / n as a float"""
    start = time.time()
    await asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total = end - start
    return total / n
