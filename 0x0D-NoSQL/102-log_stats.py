#!/usr/bin/env python3
''' log stats '''
from pymongo import MongoClient


if __name__ == '__main__':
    mc = MongoClient('mongodb://localhost:27017').logs.nginx
    print("{} logs".format(mc.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(mc.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(mc.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(mc.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(mc.count_documents({"method": "PATCH"})))
    d = "\tmethod DELETE: {}".format(mc.count_documents({"method": "DELETE"}))
    print(d)
    print("{} status check".format(mc.count_documents({"path": "/status"})))
    print("IPs:")
    ip_list = mc.aggregate([
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ])
    for ip in ip_list:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
