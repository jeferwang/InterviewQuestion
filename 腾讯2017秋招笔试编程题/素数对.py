"""
给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。
如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10,分别为(5,5),(3,7)）
输入描述:
输入包括一个整数n,(3 ≤ n < 1000)


输出描述:
输出对数

输入例子1:
10

输出例子1:
2
"""
import sys


class Solve:
	def __init__(self, num):
		"""
		实例化的时候设置num为实例属性
		:param num:
		"""
		self.num = num
		self.gen_prime_number()
	
	def gen_prime_number(self):
		"""
		获取num之下的所有素数列表
		:return:
		"""
		prime_list = []
		for i in range(2, self.num):
			if self.is_prime(i):
				prime_list.append(i)
		self.prime_list = prime_list
	
	def is_prime(self, num):
		"""
		判断num是不是素数
		:param num:
		:return:
		"""
		for i in range(2, num):
			if not num % i:
				return False
		return True
	
	def compute(self):
		"""
		计算素数对
		"""
		prime_list = filter(lambda x: x <= self.num/2, self.prime_list)
		_count = 0
		for i in prime_list:
			if self.num - i in self.prime_list:
				_count += 1
		print(_count)


if __name__ == '__main__':
	raw_number = int(sys.stdin.readline().strip())
	solve = Solve(raw_number)
	solve.compute()
