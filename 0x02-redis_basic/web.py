#!/usr/bin/env python3
"""
Module to implement get_page function with caching and access count tracking.
"""
import redis
import requests
from functools import wraps
from typing import Callable

# Initialize Redis client
redis_client = redis.Redis()

def cache_result(expire: int = 10) -> Callable:
    """
    Decorator to cache the result of a function for a specified expiration time.
    """
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(*args, **kwargs):
            url = args[0]
            cached_result = redis_client.get(url)
            if cached_result:
                return cached_result.decode('utf-8')

            result = method(*args, **kwargs)
            redis_client.setex(url, expire, result)
            return result
        return wrapper
    return decorator

def count_access(method: Callable) -> Callable:
    """
    Decorator to count the number of times a URL is accessed.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]
        redis_client.incr(f"count:{url}")
        return method(*args, **kwargs)
    return wrapper

@cache_result(expire=10)
@count_access
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a particular URL.
    """
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    # Example usage
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(f"URL accessed {redis_client.get(f'count:{url}').decode('utf-8')} times")
