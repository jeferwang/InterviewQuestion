"""
合并两个集合
"""
import sys


def solve(_ls1, _ls2):
	res = list(set(_ls1 + _ls2))
	res.sort()
	return res


if __name__ == '__main__':
	while True:
		_line1 = input()  # 输入的第一行为元素个数
		if not _line1:
			break
		_line2 = input().split(' ')  # 一个集合
		_line3 = input().split(' ')  # 另一个集合
		_solved = solve(_line2, _line3)
		print(' '.join(_solved))
