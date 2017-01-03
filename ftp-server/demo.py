'''def is_regular(input):
	reverse = input[::-1]
	regular = ''.join(['qwertyuio','asdfghjkl','zxcvbnm'])
	a = input in regular
	b = reverse in regular
	return a, b

print is_regular('qwert')
print is_regular('trew')
'''

def is_by_step(input):
	delta = ord(input[1])- ord(input[0])

	for i in range(2, len(input)):
		print i
		if ord(input[i]) - ord(input[i-1]) != delta:
			return False

	return True, delta

print is_by_step('a')