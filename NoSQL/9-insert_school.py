#!/usr/bin/env python3
"""func inserts a new doc in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """func inserts a new doc in a collection based on kwargs"""
    if mongo_collection:
        return mongo_collection.insert_one(kwargs).inserted_id
    else:
        return None
