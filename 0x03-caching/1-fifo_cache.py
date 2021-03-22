#!/usr/bin/python3
'''
This module contains the class FIFOCache
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    FIFO Caching system that inherits from BasicCache
    '''
    def __init__(self):
        ''' FIFO Initialization '''
        self.queue_list = []
        super().__init__()

    def put(self, key, item):
        ''' Assign to the dictionary '''
        if key and item:
            if self.cache_data.get(key):
                self.queue_list.remove(key)
            self.queue_list.append(key)
            self.cache_data[key] = item
            if len(self.queue_list) > self.MAX_ITEMS:
                top_item = self.queue_list.pop(0)
                self.cache_data.pop(top_item)
                print("DISCARD: {}".format(top_item))

    def get(self, key):
        ''' Returns the value linked to key '''
        if key is None:
            return None
        return self.cache_data.get(key)
