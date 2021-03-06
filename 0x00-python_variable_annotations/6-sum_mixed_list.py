#!/usr/bin/env python3
'''
This module contains a type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and returns their
sum as a float.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Adds a mixed list of ints and floats
    '''
    sum: float = 0
    for a in mxd_lst:
        sum = sum + float(a)
    return sum
