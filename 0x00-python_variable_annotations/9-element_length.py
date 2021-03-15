#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
'''
This module contains a type-annotated function element_length
that takes an interable and returns a list.
'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Returns a list from any iterable
    '''
    return [(i, len(i)) for i in lst]
