#!/usr/bin/env python3
from typing import List, Union
'''
This module contains a type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and returns their
sum as a float.
'''


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum: float = 0
    for a in mxd_lst:
        sum = sum + float(a)
    return sum
