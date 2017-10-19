"""
假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把该编码按字典序排序，形成一个数组如下： a, aa, aaa, aaaa, aaab, aaac, … …, b, ba, baa, baaa, baab, baac … …, yyyw, yyyx, yyyy 其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 编写一个函数，输入是任意一个编码，输出这个编码对应的Index.
输入描述:
输入一个待编码的字符串,字符串长度小于等于100.

输出描述:
输出这个编码的index

输入例子1:
baca

输出例子1:
16331
"""

import sys


def getInterval():
	"""
	计算间隔
	:return:
	"""
	interval = [1] * 5
	interval[3] = 25 * interval[4] + 1
	interval[2] = 25 * interval[3] + 1
	interval[1] = 25 * interval[2] + 1
	return interval


def solve(input_str):
	"""
	编码
	:param input_str: 输入字符串
	:return: 编码计算结果
	"""
	interval = getInterval()
	res = 0
	for i in range(len(input_str)):
		b = (ord(input_str[i]) - 97) * interval[i + 1] + 1
		res += b
	
	res -= 1
	return res


if __name__ == '__main__':
	while True:
		input_str = sys.stdin.readline().strip()
		if len(input_str) > 4 or not input_str:
			break
		else:
			print(solve(input_str))
