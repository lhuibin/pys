#coding:utf-8

import os
import sys

Path = sys.argv[0]
if os.path.isdir(Path):
	bat = os.path.join(Path, 'f2pool.bat')
if os.path.isdir(bat):
	os.system(bat)