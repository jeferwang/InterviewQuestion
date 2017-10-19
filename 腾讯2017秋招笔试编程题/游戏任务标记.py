"""
游戏里面有很多各式各样的任务，其中有一种任务玩家只能做一次，这类任务一共有1024个，任务ID范围[1,1024]。请用32个unsigned int类型来记录着1024个任务是否已经完成。初始状态都是未完成。 输入两个参数，都是任务ID，需要设置第一个ID的任务为已经完成；并检查第二个ID的任务是否已经完成。 输出一个参数，如果第二个ID的任务已经完成输出1，如果未完成输出0。如果第一或第二个ID不在[1,1024]范围，则输出-1。
输入描述:
输入包括一行,两个整数表示人物ID.


输出描述:
输出是否完成

输入例子1:
1024 1024

输出例子1:
1
"""
import sys


def solve(id1, id2):
	flags = [0] * 32  # 定义32个unsigned int
	if id1 not in range(1, 1025) or id2 not in range(1, 1025):
		print(-1)
		return False
	id1 -= 1
	id2 -= 1
	# 计算idx和temp
	_idx = int(id1 / 32)
	_temp = id1 % 32
	# 设置第一个任务为已完成
	flags[_idx] |= 1 << _temp
	# 重新计算idx和temp
	_idx = int(id2 / 32)
	_temp = id2 % 32
	if flags[_idx] & (1 << _temp):
		print(1)
	else:
		print(0)
	return True


if __name__ == '__main__':
	input_ids = sys.stdin.readline().strip().split(' ')
	solve(int(input_ids[0]), int(input_ids[1]))
