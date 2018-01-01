# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        _ls=[1,2]
        if number<=2:
            return number
        for i in range(3,number+1):
            _ls.append(_ls[-1]+_ls[-2])
        return _ls[-1]