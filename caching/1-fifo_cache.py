#!/usr/bin/env python3
"""class inherits and is a caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class inherits from the base caching system"""
    def __init__(self):
        """calling parent constructor"""
        super().__init__()

    def put(self, key, item):
        """FIFO algorithm - discard first item in cache"""
        if key is None and item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = None
            for i in self.cache_data:
                """loop to first item in cache, assign to i and break"""
                first_key = i
                break
            if first_key is not None:
                """print first item and delete from cache"""
                print(f"DISCARD: {first_key}")
                del self.self_cache[first_key]
        self.cache_data[key] = item

    def get(self, key):
        """returns the value for key or none"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
