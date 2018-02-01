# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # 特殊条件检查
        if len(array) == 0:
            return 0
        # 初始值
        maxSum = curSum = array[0]
        # 循环求和
        for num in array[1:]:
            # 尝试加上当前值
            curSum += num
            # 取二者最大值
            maxSum = max(maxSum, curSum)
            # 如果加了之后是负的，就扔了吧，没什么卵用
            if curSum < 0:
                curSum = 0
        return maxSum
