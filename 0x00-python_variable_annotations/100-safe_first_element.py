#!/usr/bin/env python3
from typing import Sequence, Any, Union
'''
This module contains a type-annotated function safe_first_element
that returns the first element of any sequence and returns the
first element safely.
'''


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Safely returns first element of a sequence
    '''
    if lst:
        return lst[0]
    else:
        return None
