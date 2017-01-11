#!/usr/bin/env python
# coding:utf-8

'''
这是一个监控矿机运行状态的脚本，检测到算力异常自动重启矿机
'''

import requests
import re

url = 'https://www.f2pool.com/zec/t1b4jWWao8aGzjEd5PCkUCs54PsckRCjLbN'
r = requests.get(url)
sol_raw = re.findall('[>]'+'\d{1,3}'+'\s'+'[sol]', r.text)
sol = re.findall('\d{1,3}',str(sol_raw))
print('15min:',sol[2])
