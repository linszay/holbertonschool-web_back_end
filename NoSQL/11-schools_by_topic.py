#!/usr/bin/env python3
"""func returns the list of schools with a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """func returns the list of schools with a specific topic"""
    if mongo_collection:
        return mongo_collection.find({"topics": topic})
    else:
        return []
