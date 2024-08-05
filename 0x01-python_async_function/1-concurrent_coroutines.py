#!/usr/bin/env python3

""" Async concept """
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Async function """
    output = []
    for _ in range(n):
        output.append(await wait_random(max_delay))
    return output
