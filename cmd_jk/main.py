#!/usr/bin/env python
# coding:utf-8

'''
这是一个监控矿机运行状态的脚本，检测到算力异常自动重启矿机
'''
#1.要重启挖矿
#2.要启动新窗口，也就是执行后，监控程序要继续执行（或者可以重新启动一个监控程序）
#3.要做错误处理，并记录错误日志 http://www.jb51.net/article/88449.htm

import requests
import re
import os
import time
import logging

while True:
	try:
		url = 'https://www.f2pool.com/zec/t1b4jWWao8aGzjEd5PCkUCs54PsckRCjLbN'
		r = requests.get(url)
		sol_raw = re.findall('[>]'+'\d{1,3}'+'\s'+'[sol]', r.text)
		sol = re.findall('\d{1,3}',str(sol_raw))
		sol15 = int(sol[2])
		print('15min:',sol[2])
		#print(a)


		if sol15 < 1000:
			a=r"f2pool.bat"
			a= os.path.sep.join(a.split(r'/'))
			print(a)
			os.system(a)
		
		
	except Exception as e:
		logging.exception(e)
		logger = logging.getLogger("挖矿监控")
		logger.setLevel(logging.ERROR)
		# 建立一个filehandler来把日志记录在文件里，级别为ERROR以上
		fh = logging.FileHandler("wakuang.log")
		fh.setLevel(logging.ERROR)
		# 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
		ch = logging.StreamHandler()
		ch.setLevel(logging.ERROR)
		# 设置日志格式
		formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(e)s")
		ch.setFormatter(formatter)
		fh.setFormatter(formatter)
		#将相应的handler添加在logger对象中
		logger.addHandler(ch)
		logger.addHandler(fh)
		# 开始打日志
		logger.debug("debug message")
		logger.info("info message")
		logger.warn("warn message")
		logger.error("error message")
		logger.critical("critical message")

	time.sleep(6)
