#!/usr/bin/python3
'''
This module contains the class MRUCache
'''
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
    MRU Caching system that inherits from BasicCache
    '''
    def __init__(self):
        ''' MRU Initialization '''
        self.stack_list = []
        super().__init__()

    def put(self, key, item):
        ''' Assign to the dictionary '''
        if key and item:
            if self.cache_data.get(key):
                self.stack_list.remove(key)
            if len(self.stack_list) >= self.MAX_ITEMS:
                last_item = self.stack_list.pop()
                self.cache_data.pop(last_item)
                print("DISCARD: {}".format(last_item))
            self.stack_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value linked to key '''
        if self.cache_data.get(key):
            self.stack_list.remove(key)
            self.stack_list.append(key)
        return self.cache_data.get(key)
