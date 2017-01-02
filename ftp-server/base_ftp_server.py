#!/usr/bin/env python3
# coding:utf-8
# 需要安装 pyftpdlib 模块

import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler,ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
# 读取用户配置文件
from config_ftp import *

def init_ftp_server():
	# 实例化虚拟用户 这是ftp验证首要条件
	authorizer = DummyAuthorizer()
    
	if enable_anonymous:
		#添加匿名用户
		authorizer.add_anonymous(anonymous_path)

	# 读取配置中用户并授权
	for user in user_list:
		name,passwd,permit,homedir=user
		try:
			authorizer.add_user(name,passwd,homedir,perm=permit)
		except:
			print("配置文件错误 请检查是否正确匹配了相应的用户名、密码、权限、路径")
			print(user)

	dtp_handler = ThrottledDTPHandler
	#上传下载速度
	dtp_handler.read_limit = max_download
	dtp_handler.write_limit = max_upload
	#初始化ftp服务器句柄
	handler = FTPHandler
	handler.authorizer = authorizer

	# 是否开启记录
	if enable_logging:
		logging.basicConfig(filename="pyftp.log", level=logging.INFO)

	#登录时显示的标题
	handler.banner = welcom_banner
	handler.masquerade_address = masquerade_address

	# 主动模式和被动模式
	handler.passive_ports = range(passive_ports[0], passive_ports[1])

	#监听ip 和端口
	address = (ip, port)
	server = FTPServer(address, handler)

	#最大连接数
	server.max_cons = max_cons
	server.max_cons_per_ip = max_pre_ip 

	# 开启服务
	server.serve_forever()


def ignor_octothrpe(text):
	#通过遍历每一行来 返回#后边的数据
	for x, item in enumerate(text):
		if item == '#':
			return text[:x]
		pass
	return text
def init_user_config():
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

if __name__ == '__main__':
	#用于保存授权用户登录
	user_list = []
	#从配置文件初始化用户
	init_user_config()
	init_ftp_server()




