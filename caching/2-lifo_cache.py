#!/usr/bin/env python3
"""class inherits and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class inherits from the base caching system"""
    def __init__(self):
        """calling parent constructor"""
        super().__init__()

    def put(self, key, item):
        """LIFO algorithm - discard last item in cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = None
            for i in reversed(self.cache_data):
                """loop to last item in cache, assign to i and break"""
                last_key = i
                break
            if last_key is not None:
                """print last key and delete from cache"""
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """returns the value for key or none"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
