#!/usr/bin/env python3
'''
This module contains the function max_delay
'''
import random
import asyncio


async def wait_random(max_delay=10):
    '''
    Returns a random float between 0 and wait_random
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
