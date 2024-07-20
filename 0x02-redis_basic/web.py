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
        count_key = f'count:{url}'
        result_key = f'result:{url}'

        # Increment count or set it to 0 if it doesn't exist
        if not redis_store.exists(count_key):
            redis_store.set(count_key, 0)
        redis_store.incr(count_key)

        result = redis_store.get(result_key)
        if result:
            return result.decode('utf-8')

        result = method(url)
        redis_store.setex(result_key, 10, result)
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
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = "http://google.com"
    print(get_page(url))
    print(get_page(url))

    # Check the count value
    count = redis_store.get(f'count:{url}')
    print(count.decode('utf-8'))
