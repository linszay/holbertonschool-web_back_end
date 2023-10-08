#!/usr/bin/env python3
"""Creating a new class & using Redis"""
import redis
import uuid


class Cache():
    """class stores an instance od redis client as private variable"""
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str) -> str:
        """takes a data arg and returns a string"""
        """generate a randodm string"""
        key = str(uuid.uuid4())
        """store the string data in redis"""
        self._redis.set(key, data)
        """return the key"""
        return key
