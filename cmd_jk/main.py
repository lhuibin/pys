#!/usr/bin/env python
# coding:utf-8

'''
这是一个监控矿机运行状态的脚本，检测到算力异常自动重启矿机
'''

import requests

url = 'https://www.f2pool.com/static/js/jquery-1.9.1.min.js?v=397754ba49e9e0cf4e7c190da78dda05'

r = requests.get(url, verify=False)

a = r.json()['data']