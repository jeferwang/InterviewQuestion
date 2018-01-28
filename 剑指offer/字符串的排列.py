# -*- coding:utf-8 -*-
def swap(_ls, _a, _b):
    tmp = _ls[_a]
    _ls[_a] = _ls[_b]
    _ls[_b] = tmp
    return _ls


class Solution:
    def __init__(self):
        self.res = []

    def Permutation(self, ss):
        if ss != None and len(ss) > 0:
            self.PermutationHelp(list(ss), 0)
            self.res.sort()
        return self.res

    def PermutationHelp(self, sl, idx):
        if idx == len(sl) - 1:
            val = ''.join(sl)
            if val not in self.res:
                self.res.append(val)
        else:
            for j in range(idx, len(sl)):
                sl = swap(sl, idx, j)
                self.PermutationHelp(sl, idx + 1)
                sl = swap(sl, idx, j)
