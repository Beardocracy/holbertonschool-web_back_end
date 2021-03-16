#!/usr/bin/env python3
'''
This module contains the function measure_time
'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Meaures the total execution time for wait_n
    '''
    timer_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    timer_end = time.time()
    return timer_end - timer_start
