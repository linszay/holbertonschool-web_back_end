#!/usr/bin/env python3
"""class inherits and is a caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class inherits from the base caching system"""
    def __init__(self):
        """calling parent constructor"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """LRU algorithm - discard least recently used item"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """find the least recently used item, print and delete"""
            lru_key = self.usage_order.pop(0)
            print(f"DISCARD: {lru_key}")
            del self.cache_data[lru_key]
        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """move recently used key to the end so LRU is at the front"""
        if key is not None and key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
