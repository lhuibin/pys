#! python3
# coding:utf-8

'''命令行火车票查看器

Usage:
	tickets [-gdtkz] <from> <to> <date>

Options:
	-h,--help  现实帮助菜单
	-g         高铁
	-d 		   动车
	-t         特快
	-k 		   快速
	-z         直达

Example:
	tickets 北京 上海 2017-01-12
	tickets -dg 成都 南京 2017-6-12
'''

from docopt import docopt
from stations import stations
import requests
from colorama import init, Fore
from prettytable import PrettyTable

class TrainsCollection:
	
	#split 将字符串分割成列表
	header = '车次 车站 时间 历时 商务 特等 一等 二等 高级软卧 软卧 硬卧 软座 硬座 无座'.split()

	def __init__(self, available_trains, options):
	
		''' 查询到的火车班次集合

		:param available_trains: 一个列表，包含可获得的火车班次，每个火车班次是一个字典
		:param option: 查询选项，比如高铁，动车，等等。。。
		'''
		self.available_trains = available_trains
		self.options = options

	def _get_duration(self, raw_train):
		# 获取历时，把数据 'lishi':09:30 格式化为 9小时30分
		duration = raw_train['queryLeftNewDTO'].get('lishi').replace(':','小时') + '分'
		# 把 ‘00小时30分’ 格式化为 ‘30分’
		if duration.startswith('00'):
			return duration[4:]
		if duration.startswith('0'):
			return duration[1:]
		return duration

	@property
	def trains(self):
		# raw_train 一个车次的数据，是一个dict
		for raw_train in self.available_trains:
			# 获取车次
			train_no = raw_train['queryLeftNewDTO']['station_train_code']
			# 小写车次的第一个字母，可以作为判定车型的依据
			initial = train_no[0].lower()
			# 如果没有指定车型 或 该车次在制定的车型中，则处理添加此车次数据
			if not self.options or initial in self.options:
				#？？？？？？要添加所有座位类型，还没有添加完？？？？？？？
				# 构造车次信息 【车次 车站 时间 历时 商务 特等 一等 二等 高级软卧 软卧 硬卧 软座 硬座 无座】
				train = [
					train_no,        
					'\n'.join([Fore.GREEN + raw_train['queryLeftNewDTO']['from_station_name'] + Fore.RESET,
								Fore.RED + raw_train['queryLeftNewDTO']['to_station_name'] + Fore.RESET]),
					'\n'.join([Fore.GREEN + raw_train['queryLeftNewDTO']['start_time'] + Fore.RESET,
								Fore.RED + raw_train['queryLeftNewDTO']['arrive_time'] + Fore.RESET]),
					self._get_duration(raw_train),
					raw_train['queryLeftNewDTO']['swz_num'],
					raw_train['queryLeftNewDTO']['tz_num'],
					raw_train['queryLeftNewDTO']['zy_num'],
					raw_train['queryLeftNewDTO']['ze_num'],
					raw_train['queryLeftNewDTO']['gr_num'],
					raw_train['queryLeftNewDTO']['rw_num'],
					raw_train['queryLeftNewDTO']['yw_num'],
					raw_train['queryLeftNewDTO']['rz_num'],
					raw_train['queryLeftNewDTO']['yz_num'],
					raw_train['queryLeftNewDTO']['wz_num'],
				]
				# 是一个生成器，一次生成一班列车的数据
				yield train


	# 美化显示模块
	def pretty_print(self):
	
		pt = PrettyTable()
		pt._set_field_names(self.header)
		for train in self.trains:
			pt.add_row(train)

		print(pt)


def cli():
	# 通过docopt模块 获取输入参数 
	arguments = docopt(__doc__)
	from_station = stations.get(arguments['<from>'])
	to_station = stations.get(arguments['<to>'])
	date = arguments['<date>']

	# 构造请求数据的url
	url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_station, to_station)

	# 获取参数
	options = ''.join([key for key, value in arguments.items() if value is True])




	# 添加verify=False参数不验证证书
	r = requests.get(url, verify=False)
	available_trains = r.json()['data']

	# 实例化类 
	TrainsCollection(available_trains, options).pretty_print()



if __name__ == "__main__":
	cli()

