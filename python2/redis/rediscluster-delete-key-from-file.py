#!/usr/bin/python
# -*- coding: UTF-8 -*-

u"""
    需要先安装rediscluster包
    pip install redis-py-cluster
    
    argv[1]：host1:port1, host2:port2, host3:port3, ....
    argv[2]：filename
"""

from rediscluster import StrictRedisCluster

import sys

if len(sys.argv) < 3:
    raise ValueError("参数太少了！%d" % len(sys.argv))

address_array = sys.argv[1].split(",")
filename = sys.argv[2]

if len(address_array) < 1:
    raise ValueError("参数格式不对了！")

startup_nodes = []
for address in address_array:
    address_str = address.split(":")
    host = address_str[0]
    port = address_str[1]
    startup_nodes.append({"host": host, "port": port})

rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# 删除redis的值
with open(filename, "r") as f:
    for s in f.readlines():
        s = s.strip()
        if s == "":
            continue
        print "delete: %s %s " % (str(rc.delete(s)), s)
