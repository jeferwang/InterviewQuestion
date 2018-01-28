# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k==0 or  len(tinput)==0 or k > len(tinput):
            return []
        start = 0
        end = len(tinput) - 1
        index = self.Partition(tinput, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
            else:
                start = index + 1
            index = self.Partition(tinput, start, end)
        res = tinput[:k]
        res.sort()
        return res

    def Partition(self, ls, start, end):
        flag = ls[end]
        small = start - 1
        for idx in range(start, end):
            if ls[idx] < flag:
                small += 1
                if small != idx:
                    self.swap(ls, small, idx)
        small += 1
        self.swap(ls, small, end)
        return small

    def swap(self, ls, a, b):
        tmp = ls[a]
        ls[a] = ls[b]
        ls[b] = tmp


if __name__ == '__main__':
    d = [4, 5, 1, 6, 2, 7, 3, 8]
    s = Solution()
    res = s.GetLeastNumbers_Solution(d, 0)
    print(res)
