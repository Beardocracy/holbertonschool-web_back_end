#!/usr/bin/env python3
'''
This module contains a type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Adds a list of floats and returns a float.
    '''
    sum: float = 0
    for a in range(len(input_list)):
        sum = sum + float(input_list[a])
    return sum
