# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n <= 0:
            return 0
        ls_n = list(str(n))
        return self.NumberOf1(ls_n)

    def NumberOf1(self, ls):
        if not ls:
            return 0
        first = int(ls[0])
        length = len(ls)
        if length == 1 and first == 0:
            return 0
        if length == 1 and first > 0:
            return 1
        numFirst = 0
        if first > 1:
            numFirst = 10 ** (length - 1)
        elif first == 1:
            numFirst = int(''.join(ls[1:])) + 1
        numOther = first * (length - 1) * (10 ** (length - 2))
        numRec = self.NumberOf1(ls[1:])
        return numFirst + numOther + numRec


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution(21345))  # 18821
