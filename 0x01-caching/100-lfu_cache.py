#!/usr/bin/env python3
""" Caching """

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Caching for basic caching"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.access_key = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            min_key = min(self.access_key, key=self.access_key.get)
            self.cache_data.pop(min_key)
            self.access_key[key] += self.access_key[min_key] - 1
            del self.access_key[min_key]
            print("DISCARD: {}".format(min_key))

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        for i in self.access_key.keys():
            self.access_key[i] -= 1

        if key in self.access_key:
            self.access_key[key] += 1
        else:
            self.access_key[key] = 0

        return self.cache_data[key]
