#!/usr/bin/env python3
""" Python function that changes all topics """


def update_topics(mongo_collection, name, topics):
    """
    change all topic
    """
    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
