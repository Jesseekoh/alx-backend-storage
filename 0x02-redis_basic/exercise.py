#!/usr/bin/env python3
"""exercise module"""
from typing import Union
from uuid import uuid4

import redis


class Cache:
    """Cache class declaration"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def Store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key (e.g. using uuid),
        store the input data in Redis using the
        random key and return the key."""
        key = str(uuid4())
        self._redis.mset({key: data})
