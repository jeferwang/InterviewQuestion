# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # 0次方
        if exponent==0:
            return 1
        flag=1
        # 负次方
        if exponent<0:
            flag=-1
        # 处理次方
        res=1
        for i in range(flag*exponent):
            res=res*base
        return res if flag==1 else 1/res
