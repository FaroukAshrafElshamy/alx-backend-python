#!/usr/bin/env python3

"""function to_kv that takes a string k and an int OR float v as arguments"""

from typing import Union, List, Tuple


def to_kv(k: str, v: List[Union[int, float]]) -> Tuple[str, float]:
    """String to Tuple"""
    return (k, float(v**2))
