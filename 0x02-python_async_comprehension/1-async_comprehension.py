#!/usr/bin/env python3
'''
This module contains the function async_comprehension
'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Returns a list of 10 numbers using async comprehension
    '''
    return [i async for i in async_generator()]
