# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # 边界条件
        if index <= 0:
            return 0
        uglyNumber = [1]  # 丑数数组
        u2 = u3 = u5 = 0
        while len(uglyNumber) < index:
            uglyMin = min(uglyNumber[u2] * 2, uglyNumber[u3] * 3, uglyNumber[u5] * 5)
            uglyNumber.append(uglyMin)
            while uglyNumber[u2] * 2 <= uglyNumber[-1]:
                u2 += 1
            while uglyNumber[u3] * 3 <= uglyNumber[-1]:
                u3 += 1
            while uglyNumber[u5] * 5 <= uglyNumber[-1]:
                u5 += 1
        ugly = uglyNumber[-1]
        return ugly
