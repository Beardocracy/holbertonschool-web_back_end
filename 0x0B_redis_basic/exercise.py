#!/usr/bin/env python3
''' Redis '''
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' count calls '''
    num = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' wrapper '''
        self._redis.incr(num)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' Call history '''
    outputs = method.__qualname__ + ":outputs"
    inputs = method.__qualname__ + ":inputs"
    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(inputs, str(args))
        output = method(self, *args)
        self._redis.rpush(outputs, str(output))
        return output
    return wrapper


def replay(method: Callable):
    ''' Displays the history of calls of a function '''
    r = redis.Redis()
    name = method.__qualname__
    inputs = r.lrange(name + ':inputs', 0, -1)
    outputs = r.lrange(name + ':outputs', 0, -1)
    print('{} was called {} times:'.format(name, len(outputs)))
    for ins, outs in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(name, ins.decode('utf-8'),
                                     outs.decode('utf-8')))


class Cache:
    ''' Cache class '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store method '''
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        ''' Get method '''
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, data: bytes) -> str:
        ''' Get str '''
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        ''' get int '''
        return int(self._redis.get(data))
