# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        return self.IsSquenceOfBST(sequence)

    def IsSquenceOfBST(self, sequence):
        if not sequence:
            return True
        root = sequence.pop()
        _len = len(sequence)
        if not _len:
            return True
        _split = None
        for s in range(_len):
            if sequence[s] > root:
                _split = s
            if _split != None and sequence[s] < root:
                return False
        left = sequence[0:_split]
        right = sequence[_split:]
        return self.IsSquenceOfBST(left) and self.IsSquenceOfBST(right)
