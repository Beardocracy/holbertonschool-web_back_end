#!/usr/bin/env python3
'''
Simple Helper Function
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Returns the index numbers of a range in a tuple
    '''
    return ((page - 1) * page_size, page_size * page)
