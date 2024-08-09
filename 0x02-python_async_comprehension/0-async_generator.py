#!/usr/bin/env python3
""" Async """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """ Async Function """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
