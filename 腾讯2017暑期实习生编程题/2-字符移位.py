"""
时间限制：1秒
空间限制：32768K
小Q最近遇到了一个难题：把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。
你能帮帮小Q吗？


输入描述:

输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.



输出描述:

对于每组数据，输出移位后的字符串。

输入例子1:
AkleBiCeilD

输出例子1:
kleieilABCD
"""
import sys


def solve(_line):
	_line = list(_line)
	_len = len(_line)
	_count = 0
	_break_flag = False
	for i in range(_len):  # 由于输入数据格式标准,不再进行判断
		while True:
			_char = _line[i]
			_ord = ord(_char)
			_count += 1
			if _count == _len + 1:
				_break_flag = True
				break
			if _ord < 97:  # 小于97也就是大写字母,在Ascii表中,65-90是大写字母,97-122是小写字母
				for j in range(i, _len - 1):  # 该位置之后的字符依次向前移动
					_line[j] = _line[j + 1]
				_line[_len - 1] = _char
			else:
				break
		if _break_flag:
			break
	
	return ''.join(_line)


if __name__ == '__main__':
	while True:
		_line = sys.stdin.readline().strip()  # 接收输入
		if not _line:  # 如果无输入就结束
			break
		print(solve(_line))

"""
hxKLAGLLzPyTxsFsrUnnSKQBHdQQrOyaEYJRgiJbHIDXFcQkFmIhPNKIBfHxXDBdKAvgZiBLVwnlxJAHmttsSJkZhSmQneNVoKoIYZRjPqsrFFaaqZbyNyeRjVKVFrCGdfycidTqbyQcpAtdRGzzBAaKoqybWMOyhrCQdwcRwQQpQavTnAbjriVwxJOrTYJVGYSWzKYeNAGqBzkJLucabNYvyVFxAGKLfqHXNttaqZfncEdTroGMzZnDbvZBBaRbJvuYIvlWrKaaGrvtyxrsCUOqxdwCrmVEeDrLKZKFJVRmrLsmbmOGUJyfdZIrFhuSwJQGRTYMLxKQNMaCavatlQIRZmFQvyWgQTVENxUcPKQCaUQbjyfaNuwoNdTBNldgrtPUcQodqsuJOdDpUczJWCZaasDdEYJkvituMHrCmZQSlRjIefVisatIUtfxBeKnHPyvWUKzRliFsYWgeXogiEgXDbfxAybwFuqFyEvjfIHEPDPKqEiGUtZhdDIDBGKpvBFyqHeEEhAToAbqHEpIdIhIGBtWjGHiQRctZxQQYkfFoWUbqZyIcjRPQBilHrnqNBzFmoRUYCSrGkawJCcOrMceegISpIpSGVjbngWVMTYtGoAlQFPFyOFAxndJZNfKDTwFIxisKTjyjchidXpYgLfoBOLriuIAHmAbQwoHBgbdUYBHlDQGZJASsHszOEPthLVnYbNqWegmONexfdsTVYHgtDmlyugefOBsqmgNDBoxkkhVHfvrYooVOyxDJQJLjYSngksbTopoPJFsKQzHePLukXyYTYCeW
"""