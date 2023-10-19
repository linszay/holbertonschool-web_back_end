#!/usr/bin/env python3
"""func changes all topics of a school doc based on the name"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school doc"""
    if mongo_collection:
        return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
        )
    else:
        return None
