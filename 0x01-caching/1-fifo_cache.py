#!/usr/bin/env python3
""" Caching """

BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
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
        if len(self.cache_data) > self.MAX_ITEMS:
            old_key = next(iter(self.cache_data))
            self.cache_data.pop(old_key)
            print('DISCARD: {}'.format(old_key))

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data[key]
