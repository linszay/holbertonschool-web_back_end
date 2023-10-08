#!/usr/bin/env python3
"""Creating a new class & using Redis"""
import redis
import uuid
import typing


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
