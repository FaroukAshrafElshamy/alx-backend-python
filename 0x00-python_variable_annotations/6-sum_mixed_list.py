#!/usr/bin/env python3

""" type-annotated function sum_mixed_list """
from typing import List, Union


def sum_miced_list(mxd_lst: List[Union[int, float]]) -> float:
    """ A list mxd_lst of integers and floats and returns their sum"""
    return sum(mxd_lst)
