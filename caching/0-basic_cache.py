#!/usr/bin/env python3
"""class inherits and is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class inherits from the base caching system"""
    def put(self, key, item):
        """sets self.cache_data to item for key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """returns the value for key or none"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
