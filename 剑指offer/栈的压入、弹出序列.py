# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) != len(popV) or not pushV:
            return False
        _len = len(pushV)
        stack = []
        j = 0
        for i in range(_len):
            stack.append(pushV[i])
            while j < _len and stack[-1] == popV[j]:
                stack.pop()
                j += 1
        return not bool(len(stack))
