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
	
	header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()

	def __init__(self, available_trains, options):
	
		''' 查询到的火车班次集合

		:param available_trains: 一个列表，包含可获得的火车班次，每个火车班次是一个字典
		:param option: 查询选项，比如高铁，动车，等等。。。
		'''
		self.available_trains = available_trains
		self.options = options

	def _get_duration(self, raw_train):
		duration = raw_train['queryLeftNewDTO'].get('lishi').replace(':','小时') + '分'
		if duration.startswith('00'):
			return duration[4:]
		if duration.startswith('0'):
			return duration[1:]
		return duration

	@property
	def trains(self):
		for raw_train in self.available_trains:
			train_no = raw_train['queryLeftNewDTO']['station_train_code']
			initial = train_no[0].lower()
			if not self.options or initial in self.options:
				train = [
					train_no,        
					'\n'.join([Fore.GREEN + raw_train['queryLeftNewDTO']['from_station_name'] + Fore.RESET,
								Fore.RED + raw_train['queryLeftNewDTO']['to_station_name'] + Fore.RESET]),
					'\n'.join([Fore.GREEN + raw_train['queryLeftNewDTO']['start_time'] + Fore.RESET,
								Fore.RED + raw_train['queryLeftNewDTO']['arrive_time'] + Fore.RESET]),
					self._get_duration(raw_train),
					raw_train['queryLeftNewDTO']['zy_num'],
					raw_train['queryLeftNewDTO']['ze_num'],
					raw_train['queryLeftNewDTO']['rw_num'],
					raw_train['queryLeftNewDTO']['yw_num'],
					raw_train['queryLeftNewDTO']['yz_num'],
					raw_train['queryLeftNewDTO']['wz_num'],
				]
				yield train



	def pretty_print(self):
	
		pt = PrettyTable()
		pt._set_field_names(self.header)
		for train in self.trains:
			pt.add_row(train)

		print(pt)


def cli():

	arguments = docopt(__doc__)
	from_station = stations.get(arguments['<from>'])
	to_station = stations.get(arguments['<to>'])
	date = arguments['<date>']

	url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_station, to_station)

	# 获取参数
	options = ''.join([key for key, value in arguments.items() if value is True])




	# 添加verify=False参数不验证证书
	r = requests.get(url, verify=False)
	available_trains = r.json()['data']

	TrainsCollection(available_trains, options).pretty_print()
	#TrainsCollection(available_trains, options)


if __name__ == "__main__":
	cli()

