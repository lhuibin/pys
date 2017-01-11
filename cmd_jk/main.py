#!/usr/bin/env python
# coding:utf-8

'''
这是一个监控矿机运行状态的脚本，检测到算力异常自动重启矿机
'''

import requests

url = 'https://www.f2pool.com/zec/t1b4jWWao8aGzjEd5PCkUCs54PsckRCjLbN'

r = requests.get(url)
print r.text
