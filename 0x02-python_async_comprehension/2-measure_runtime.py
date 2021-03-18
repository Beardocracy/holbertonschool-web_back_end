#!/usr/bin/env python3
'''
This module contains the function measure_runtime
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measures the runtime of async comprehension 4 times
    '''
    time_start = time.time()
    await asyncio.gather(*(
        async_comprehension() for i in range(4)
    ))
    time_end = time.time()
    return time_end - time_start
