#!/usr/bin/env python3
from typing import List
'''
This module contains a type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float
'''


def sum_list(input_list: List[float]) -> float:
    '''
    Adds a list of floats
    '''
    sum: float = 0
    for a in range(len(input_list)):
        sum = sum + input_list[a]
    return sum
