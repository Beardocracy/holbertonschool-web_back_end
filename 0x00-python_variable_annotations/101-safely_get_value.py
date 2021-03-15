#!/usr/bin/env python3
from typing import Sequence, Any, Union, Mapping, TypeVar
'''
This module contains a type-annotated function safely_get_value
that returns the first element of a dict safely
'''

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''
    Returns first element of a dict
    '''
    if key in dct:
        return dct[key]
    else:
        return default
