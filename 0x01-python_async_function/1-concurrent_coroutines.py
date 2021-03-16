#!/usr/bin/env python3
'''
This module contains the function wait_n
'''
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Runs wait_random n times and returns a sorted list of delay times.
    '''
    delay_list = []
    for i in range(n):

        delay_time = await wait_random(max_delay)

        if len(delay_list) == 0:
            delay_list.append(delay_time)
        else:
            for idx in range(len(delay_list)):
                if delay_time < delay_list[idx]:
                    delay_list.insert(idx, delay_time)
                    break
            if delay_time >= delay_list[len(delay_list) - 1]:
                delay_list.append(delay_time)

    return delay_list
