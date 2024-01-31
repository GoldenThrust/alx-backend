#!/usr/bin/env python3
""" Caching """


#!/usr/bin/env python3
""" Caching """

BaseCaching = __import__('base_caching').BaseCaching

class MRUCache(BaseCaching):
    """ Caching for basic caching """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.recent_key = None

    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data.pop(self.recent_key)
            print('DISCARD: {}'.format(self.recent_key))
        
        self.recent_key = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        
        self.recent_key = key
            
        return self.cache_data[key]
