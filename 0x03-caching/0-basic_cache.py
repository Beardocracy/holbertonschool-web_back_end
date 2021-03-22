#!/usr/bin/python3
'''
This module contains the class BasicCache
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    Caching system that inherits from BasicCache
    '''
    def put(self, key, item):
        ''' Assign to the dictionary '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value linked to key '''
        if key is None:
            return None
        return self.cache_data.get(key)
