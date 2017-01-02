#!/usr/bin/env python3
# coding:utf-8

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 实例化虚拟用户 这是ftp验证首要条件
authorizer = DummyAuthorizer()
# 添加用户权限和路径 参数分别是 用户名 密码 用户目录 权限
authorizer.add_user("user", "12345", "/home/", perm="elradfmw")
# 添加匿名用户 这个只要路径就行
authorizer.add_anonymous("/home/")
#初始化ftp服务器句柄
handler = FTPHandler
handler.authorizer = authorizer
#添加公网ip
handler.masquerade_address = '127.0.0.1'
#在2000到2333的打开被动端口 用于链接
handler.passive_ports = range(2000,2333)
#监听ip 和端口 这是本地的一个服务器
server = FTPServer(("127.0.0.1", 1900), handler)
# 开始服务
server.serve_forever()

'''读取配置文件的代码'''

def ignor_octothrpe(text):
	#通过遍历每一行来 返回#后边的数据
	for x, item in enumerate(text):
		if item == '#'
			return text[:x]
		pass
	return text


user_list=[]

f = open('baseftp.ini',encoding='utf-8')
# 读取每行的配置文件
while 1:
	line = f.readline()
	#通过返回字符的行数来判断该行是否为空
	if len(ignor_octothrpe(line))>3:
		user_list.append(line.split())
	# 读到最后跳出循环
	if not line:
		break

#验证的时候通过解包吧值解出来病动态添加到权限中去
for user in user_list:
	name,passwd,permit,homedir=user
	try:
		authorizer.add_user(name,passwd,homedir,perm=permit)
	except:
		print("配置文件错误 请检查是否正确匹配了相应的用户名、密码、权限、路径")
		print(user)


		