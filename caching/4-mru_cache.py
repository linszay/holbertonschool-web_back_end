#!/usr/bin/env python3
"""Create a class MRUCache that inherits
from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class inherits from the base caching system"""
    def __init__(self):
        """calling parent constructor"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """MRU algorithm - discard most recently used item"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """find the most recently used item, print and delete"""
            mru_key = self.usage_order.pop(0)
            print(f"DISCARD: {mru_key}")
            del self.cache_data[mru_key]
        self.cache_data[key] = item
        self.usage_order.insert(0, key)

    def get(self, key):
        """move most used key to the front"""
        if key is not None and key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.insert(0, key)
            return self.cache_data[key]
        return None
