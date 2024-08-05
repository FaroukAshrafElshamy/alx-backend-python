#!/usr/bin/env python3

""" Create a measure_time function with integers n and max_delay """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ A Function that return the total running time of the function """

    a: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    b: float = time.perf_counter()
    total_time = b - a
    return total_time/n
