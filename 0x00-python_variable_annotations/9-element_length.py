#!/usr/bin/env python3

"""Annotate a function's parameters and return value."""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """take function parameters and return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
