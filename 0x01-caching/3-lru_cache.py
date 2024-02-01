#!/usr/bin/env python3
""" LRU Caching """

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Caching for LRU caching"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.access_count = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.access_count[key] = 0
        if len(self.cache_data) > self.MAX_ITEMS:
            min_key = min(self.access_count, key=self.access_count.get)
            self.cache_data.pop(min_key)
            self.access_count.pop(min_key)
            print("DISCARD: {}".format(min_key))

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        for k in self.access_count.keys():
            self.access_count[k] -= 1

        self.access_count[key] += 1

        return self.cache_data[key]
