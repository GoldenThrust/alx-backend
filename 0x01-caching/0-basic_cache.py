#!/usr/bin/env python3
""" Basic Caching """

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Caching for basic caching"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key not in self.cache_data:
            return None

        return self.cache_data[key]
