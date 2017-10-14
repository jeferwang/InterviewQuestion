"""
定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。

输入描述:

输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
  


输出描述:

对于每组数据，输出一个整数，代表最少需要删除的字符个数。

输入例子1:
abcda
google

输出例子1:
2
2


# 测试用的字符串
# zgtklhfzomzjckwmluvivvcmhjrwkuvcjrxojobpdedpamdshcwwsetfbacvonecrdvugeibglvhxuymjvoryqjwullvzglqazxrdmczyvbgakjagttrezmvrlptiwoqkrtxuroeqmryzsgokopxxdpbejmtwvpnaqrgqladdszhdwxfckmewhdvihgvacueqhvwvjxoitlpfrckxkuksaqzjpwgoldyhugsacflcdqhifldoaphgdbhaciixouavqxwlghadmfortqacbffqzocinvuqpjthgekunjsstukeiffjipzzabkuiueqnjgkuiojwbjzfynafnlcaryygqjfixaoeowhkxkbsnpsvnbxuywfxbnuoemxynbtgkqtjvzqikbafjnpbeirxxrohhnjqrbqqzercqcrcswojyylunuevtdhamlkzqnjrzibwckbkiygysuaxpjrgjmurrohkhvjpmwmmtpcszpihcntyivrjplhyrqftghglkvqeidyhtmrlcljngeyaefxnywpfsualufjwnffyqnpitgkkyrbwccqggycrvoocbwsdbftkigrkcbojuwwctknzzmvhbhbfzrqwzllulbabztqnznkqdyoqnrxhwavqhzyzvmmmphzxbikpharseywpfsqyybkynwbdrgfsaxduxojcdqcjuaywzbvdjgjqtoffasiuhvxcaockebkuxpiomqmtvsqhnyxfjceqevqvnapbk
# 答案516

"""

import sys


def maxlcp(strs):
	"""
	抄的别人的
	:param strs:
	:return:
	"""
	if strs is None or len(strs) == 0:
		return 0
	lens = len(strs)
	dp = [0] * lens
	dp[0] = 1 if strs[0] == strs[-1] else 0
	for i in range(lens):
		pre = dp[0]
		dp[0] = max(dp[0], 1 if strs[i] == strs[lens - 1] else 0)
		for j in range(1, lens):
			cur = dp[j]
			dp[j] = max(dp[j], dp[j - 1])
			if strs[i] == strs[lens - 1 - j]:
				dp[j] = max(dp[j], pre + 1)
			pre = cur
	return dp[lens - 1]


def lcp(_line):
	"""
	自己写的
	:param _line:
	:return:
	"""
	_len = len(_line)
	if _line is None or _len == 0:  # 处理特殊值
		return 0
	dp = [[0] * (_len + 1) for i in range(_len + 1)]  # 动态规划
	for i in range(_len):  # 遍历求字符串与逆序的最大公共子序列
		for j in range(_len):
			if _line[i] == _line[_len - 1 - j]:
				dp[i + 1][j + 1] = dp[i][j] + 1
			else:
				dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
	return dp[_len][_len]


if __name__ == '__main__':
	while True:
		_line = sys.stdin.readline().strip()
		if not _line:
			break
		_res = lcp(_line)
		print(len(_line) - _res)



# zgtklhfzomzjckwmluvivvcmhjrwkuvcjrxojobpdedpamdshcwwsetfbacvonecrdvugeibglvhxuymjvoryqjwullvzglqazxrdmczyvbgakjagttrezmvrlptiwoqkrtxuroeqmryzsgokopxxdpbejmtwvpnaqrgqladdszhdwxfckmewhdvihgvacueqhvwvjxoitlpfrckxkuksaqzjpwgoldyhugsacflcdqhifldoaphgdbhaciixouavqxwlghadmfortqacbffqzocinvuqpjthgekunjsstukeiffjipzzabkuiueqnjgkuiojwbjzfynafnlcaryygqjfixaoeowhkxkbsnpsvnbxuywfxbnuoemxynbtgkqtjvzqikbafjnpbeirxxrohhnjqrbqqzercqcrcswojyylunuevtdhamlkzqnjrzibwckbkiygysuaxpjrgjmurrohkhvjpmwmmtpcszpihcntyivrjplhyrqftghglkvqeidyhtmrlcljngeyaefxnywpfsualufjwnffyqnpitgkkyrbwccqggycrvoocbwsdbftkigrkcbojuwwctknzzmvhbhbfzrqwzllulbabztqnznkqdyoqnrxhwavqhzyzvmmmphzxbikpharseywpfsqyybkynwbdrgfsaxduxojcdqcjuaywzbvdjgjqtoffasiuhvxcaockebkuxpiomqmtvsqhnyxfjceqevqvnapbk