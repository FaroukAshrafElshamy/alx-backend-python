#!/usr/bin/env python3

"""Make a multiplier with nested functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A multiplier function"""
    def multiply(n: float) -> float:
        """Multiply a float by a multiplier"""
        return n * multiplier
    return multiply
