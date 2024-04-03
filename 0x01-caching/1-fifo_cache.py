#!/usr/bin/env python3
"""
FIFO caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First-In-First-Out (FIFO) caching
    mechanism using an ordered dictionary.
    """
    def __init__(self):
        """
        Initialize the FIFO cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        """
        return self.cache_data.get(key, None)
