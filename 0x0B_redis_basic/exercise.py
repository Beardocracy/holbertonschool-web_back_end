#!/usr/bin/env python3
''' Redis '''
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


class Cache:
    ''' Cache class '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

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
