import math


def solve(ls, fd, start, end):
	"""
	递归进行二分查找
	:param ls: 数组
	:param fd: 待查元素
	:param start: 起始下标
	:param end: 结束下标
	:return: 递归调用或boolean
	"""
	flag = math.floor((start + end) / 2)
	if ls[flag] == find:
		return True
	if start >= end:
		return False
	return solve(ls, fd, start, flag - 1) if ls[flag] > find else solve(ls, fd, flag + 1, end)


if __name__ == '__main__':
	input_list = input().split(' ')
	find = input()
	try:
		input_list = [int(i) for i in input_list]
		find = int(find)
	except:
		print('输入的值有误')
		exit()
	input_list.sort()
	print(solve(input_list, find, 0, len(input_list) - 1))
