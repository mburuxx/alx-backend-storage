#!/usr/bin/env python3
"""
Module implementing an expiring web cache and tracker.
"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
"""Redis storage instance
"""


def data_cacher(method: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator to cache the result of the URL fetching function
    and track the number of accesses to each URL.
    """
    @wraps(method)
    def invoker(url: str) -> str:
        """ Wrapper function to cache data and count URL accesses. """
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    return requests.get(url).text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(get_page(url))
