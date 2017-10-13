"""
输入整数A
整数A属于[1,5000]
从A的2进制到A-1进制,求每一个数的每一位的和的平均值
"""

import sys
import math


def getSum(num):
	_radix = range(2, num)
	_sum = 0
	for r in _radix:
		n = num
		while n:
			_sum += n % r
			n = int(n / r)
	_gcd = math.gcd(_sum, len(_radix))
	return "{}/{}".format(int(_sum / _gcd), int(len(_radix) / _gcd))


if __name__ == '__main__':
	while True:
		_line = sys.stdin.readline().strip()
		if _line:
			print(getSum(int(_line)))
		else:
			break
