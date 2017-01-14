#!/usr/bin/env python
# coding:utf-8

'''
这是一个监控矿机运行状态的脚本，检测到算力异常自动重启矿机
'''
#1.要重启挖矿
#2.要启动新窗口，也就是执行后，监控程序要继续执行（或者可以重新启动一个监控程序）
#3.要做错误处理，并记录错误日志

import requests
import re
import os
import time

while True:
	url = 'https://www.f2pool.com/zec/t1b4jWWao8aGzjEd5PCkUCs54PsckRCjLbN'
	r = requests.get(url)
	sol_raw = re.findall('[>]'+'\d{1,3}'+'\s'+'[sol]', r.text)
	sol = re.findall('\d{1,3}',str(sol_raw))
	sol15 = int(sol[2])
	print('15min:',sol[2])


	if sol15 < 100:
		a=r"f2pool.bat"
		a= os.path.sep.join(a.split(r'/'))
		print a
		os.system(a)
	
	time.sleep(600)