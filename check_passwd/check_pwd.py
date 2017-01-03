#coding:utf-8

'''
检查密码强弱

'''

# 消息打印不出来???
# 编写测试环境

import re
import json

__all__ = ['password']

# 正则表达式匹配

NUMBER = re.compile(r'[0-9]')
LOWER_CASE = re.compile(r'[a-z]')
UPPER_CASE = re.compile(r'[A-Z]')
OTHERS = re.compile(r'[^0-9a-zA-Z]')

# 检测密码是否为常用密码，对比常用密码库

def load_common_password():
	words = []
	with open('10k_most_common.txt','rb') as f:
		for word in f.readlines():
			words.append(word.strip())
	return words

COMMON_WORDS = load_common_password()

# 定义一个管理密码强度的类

class Strength:

	def __init__(self, valid, strength, message):
		self.valid = valid
		self.strength = strength
		self.message = message
	# 以下三个函数名是否有特殊意义,得查询,这里不明白?
	def __repr__(self):
		return self.strength

	def __str__():
		return self.message

	def __bool__():
		return self.valid


# 程序的核心, 另外此处的静态方法需要复习,忘记了用途

class Password:	

	TERRIBLE = 0
	SIMPLE = 1
	MEDIUM = 2
	STRONG = 3



	# 定义有规则的密码
	
	@staticmethod
	def is_regular(input):
		reverse = input[::-1]
		regular = ''.join(['qwertyuio','asdfghjkl','zxcvbnm'])
		return input in regular or reverse in regular

	@staticmethod
	def is_by_step(input):
		delta = ord(input[1])- ord(input[0])

		for i in range(2, len(input)):
			if ord(input[i]) - ord(input[i-1]) != delta:
				return False
		return

	# 常见密码

	@staticmethod
	def is_common(input):
		return input in COMMON_WORDS
	# __call__ 方法 复习一下

	def __call__(self, input, min_length=6, min_types=3, level=STRONG):

		if len(input) < min_length:
			return Strength(False, 'terrible', '密码太短了')

		if self.is_regular(input) or self.is_by_step(input):
			return Strength(False, 'simple', '密码有规则')

		if self.is_common(input):
			return Strength(False, 'simple', '密码很常见')

		types = 0

		if NUMBER.search(input):
			types += 1

		if LOWER_CASE.search(input):
			types += 1

		if UPPER_CASE.search(input):
			types += 1

		if OTHERS.search(input):
			types += 1


		if types < 2:
			return Strength(level <= self.SIMPLE, 'simple', '密码太简单了')

		if types < min_types:
			return Strength(level <= self.MEDIUM, 'medium', '密码不错, 但还不够强')

		return Strength(True, 'strong', '完美的密码')

password = Password()