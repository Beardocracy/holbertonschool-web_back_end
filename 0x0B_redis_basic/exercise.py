#!/usr/bin/env python3
''' Redis '''
import redis
from uuid import uuid4
from typing import Union


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
