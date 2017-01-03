#coding:utf-8

import re

# 正则表达式匹配
NUMBER = re.compile(r'[0-9]')
LOWER_CASE = re.compile(r'[a-z]')
UPPER_CASE = re.compile(r'[A-Z]')
OTHERS = re.compile(r'[^0-9a-zA-Z]')

# 定义一个管理密码强度的类

class Strength:
	def __init__(self, valid, strength, message):
		self.valid = valid
		self.strength = strength
		self.message = message

	# 检测密码是否为常用密码，对比常用密码库
	