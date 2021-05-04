#!/usr/bin/env python3
''' 8-all '''
import pymongo


def list_all(mongo_collection):
    ''' list all '''
    return mongo_collection.find()
