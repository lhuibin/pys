#coding:utf-8

def f(a):
	if a.startswith('0'):
		return a[1:]
	if a.startswith('00'):
		return a[4:]

	return a
print(f('00小时12分'))