#!/usr/bin/env python3
"""Creating a new class & using Redis"""
import redis
import uuid
import typing
from typing import Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts the number of calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """get the qualified method name"""
        key = method.__qualname__
        """increment the counter each time the method is called"""
        self._redis.incr(key)
        """call the method and return the result"""
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """storing the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """get qualified method name"""
        mname = method.__qualname__
        """create input/output lists by using f strings and append
        the key value(:input or :output) to the value of method name
        """
        input_key = f"{mname}:inputs"
        output_key = f"{mname}:outputs"
        """change input args to str"""
        input_str = str(args)
        """store input in the input list"""
        self._redis.rpush(input_key, input_str)
        """execute func to get the output"""
        output = method(self, *args, **kwargs)
        """store output in the output list"""
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable):
    """displays history of calls from a function"""
    def replay_function(cache_instance: Cache):
        """get qualified name"""
        thename = method.__qualname__
        """get the input/output keys from the func"""
        inputK = f"{thename}:inputs"
        outputK = f"{thename}:outputs"
        """get input/output lists from redis using lrange"""
        inputs = cache_instance._redis.lrange(inputK, 0, -1)
        outputs = cache_instance._redis.lrange(outputK, 0, -1)
        """print call history"""
        print(f"{thename} was called {len(inputs)} times:")
        for input_str, output_str in zip(inputs, outputs):
            input_args = eval(input_str)
            print(f"{thename}{input_args} -> {output_str}")
    return replay_function


class Cache():
    """class stores an instance of redis client as private variable"""
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """takes a data arg and returns a string"""
        """generate a randodm string"""
        key = str(uuid.uuid4())
        """store the string data in redis"""
        self._redis.set(key, data)
        """return the key"""
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
        -> typing.Union[str,
                        bytes,
                        int,
                        float,
                        None]:
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


"""example usage from task instructions"""
cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)(cache)
