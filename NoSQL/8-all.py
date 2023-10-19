#!/usr/bin/env python3
"""func lists all documents in a collection"""


def list_all(mongo_collection):
    """func returns a list w all docs in a collection or an empty list"""
    if mongo_collection:
        return mongo_collection.find()
    else:
        return []
