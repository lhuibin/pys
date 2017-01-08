'''
此模块用于匹配车站于车站代码并返回一个词典

Usage: python3 parse_station.py > statins.py  可以生成stations.py的文件
'''

import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8994'

response = requests.get(url, verify=False)
# 正则表达式匹配出车站 车站代码 为一个dict [\u4e00-\u9fa5]：unicode中中文的编码为/u4e00-/u9fa5
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
pprint(dict(stations), indent=4)
