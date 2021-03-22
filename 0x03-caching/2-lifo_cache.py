#!/usr/bin/python3
'''
This module contains the class LIFOCache
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
                last_item = self.queue_list.pop(3)
                self.cache_data.pop(last_item)
                print("DISCARD: {}".format(last_item))

    def get(self, key):
        ''' Returns the value linked to key '''
        if key is None:
            return None
        return self.cache_data.get(key)
