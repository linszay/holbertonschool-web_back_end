#!/usr/bin/env python3
"""Creating a new class & using Redis"""
import redis
import uuid
import typing
from typing import Optional, Callable


class Cache():
    """class stores an instance of redis client as private variable"""
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """takes a data arg and returns a string"""
        """generate a randodm string"""
        key = str(uuid.uuid4())
        """store the string data in redis"""
        self._redis.set(key, data)
        """return the key"""
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> typing.Union[str, bytes, int, float, None]:
        """takes key and optional callable arg fn"""
        """get data from regis"""
        data = self._redis.get(key)
        """if no data then return none"""
        if data is None:
            return None
        """callable is used to convert the data to desired format"""
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> typing.Union[str, None]:
        """method automatically paramertizes cache.get to str"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: int) -> typing.Union[int, None]:
        """method automatically paramertizes cache.get to int"""
        return self.get(key, fn=int)
