#!/usr/bin/env python3
from typing import Callable
'''
This module contains a type-annotated function make_multiplier that
takes a float multiplier as argument and returns a function that
multiplies a float by multiplier
'''


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Returns a function
    '''
    def fn(n: float) -> float:
        '''
        Returns n * the multiplier
        '''
        return multiplier * n
    return fn
