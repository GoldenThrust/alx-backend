#!/usr/bin/env python3
""" Caching """

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ Caching for basic caching """

    def __init__(self):
        """ Initiliaze """
        super().__init__()

    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data[key]
