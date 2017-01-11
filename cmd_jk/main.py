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
print(type(sol_raw))
print(type(sol_raw[3]))
# sol_raw shi zidian .yao zhuanhuan zifuchuan sol = re.findall('\d{1,3}',sol_raw)

print(sol_raw)
