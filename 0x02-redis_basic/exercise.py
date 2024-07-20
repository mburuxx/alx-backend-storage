#!/usr/bin/env python3
"""
Module to create a Cache class and implement replay functionality.
"""
import redis
from uuid import uuid4
from typing import Callable, Optional, Union
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs & outputs for a particular method.
    """
    method_key = method.__qualname__
    inputs = method_key + ':inputs'
    outputs = method_key + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Wrapper function to log inputs and outputs. """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.
    """
    method_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Wrapper function to increment the call count. """
        self._redis.incr(method_key)
        return method(self, *args, **kwds)
    return wrapper


def replay(method: Callable):
    """
    Function to display the history of calls to a particular method.
    """
    method_key = method.__qualname__
    inputs = method_key + ":inputs"
    outputs = method_key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(method_key).decode("utf-8")
    print("{} was called {} times:".format(method_key, count))
    ListInput = redis.lrange(inputs, 0, -1)
    ListOutput = redis.lrange(outputs, 0, -1)
    allData = list(zip(ListInput, ListOutput))
    for key, data in allData:
        attr, data = key.decode("utf-8"), data.decode("utf-8")
        print("{}(*{}) -> {}".format(method_key, attr, data))


class Cache:
    """
    Cache class to store information in Redis.
    """

    def __init__(self):
        """ Create an instance of Cache. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return a new UUID.
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis.
        """
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, data: str) -> str:
        """ Convert bytes to string. """
        return data.decode('utf-8')

    def get_int(self, data: str) -> int:
        """ Convert bytes to integer. """
        return int(data)
