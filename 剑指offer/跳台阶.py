# -*- coding:utf-8 -*-
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number<=2:
            return number
        _ls=[1,2]
        for i in range(3,number+1):
            _ls.append(_ls[-1]+_ls[-2])
        return _ls[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(100))
