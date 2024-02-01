#!/usr/bin/env python3
""" LFU Caching """

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
        
        if key in self.cache_data:
            self.cache_data[key] = item
            self.access_key[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_key = min(self.access_key, key=self.access_key.get)
                print(min_key)
                self.cache_data.pop(min_key)
                del self.access_key[min_key]
                print("DISCARD: {}".format(min_key))
            self.cache_data[key] = item
            self.access_key[key] = 1
            

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.access_key[key] += 1

        return self.cache_data[key]
