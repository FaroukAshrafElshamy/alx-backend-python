#!/usr/bin/env python3

""" Async concept """

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ doc """
    list = []

    for _ in range(n):
        list.append(await wait_random(max_delay))

    return list
