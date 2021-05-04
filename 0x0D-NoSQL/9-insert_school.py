#!/usr/bin/env python3
''' insert school '''


def insert_school(mongo_collection, **kwargs):
    ''' insert new document in a collection '''
    return mongo_collection.insert_one(kwargs).inserted_id
