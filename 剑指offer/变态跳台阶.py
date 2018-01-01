# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        _ls = [1, 2]
        if number <= 2:
            return number
        for i in range(3, number + 1):
            _ls.append(sum(_ls)+1)
        return _ls[-1]
