#!/usr/bin/env python3
'''
This module contains the function task_wait_n
'''
import random
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    '''
    Runs task_wait_random n times and returns a sorted list of delay times.
    '''
    delay_list = []
    for i in range(n):

        delay_time = await task_wait_random(max_delay)

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
