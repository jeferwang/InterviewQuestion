# -*- coding:utf-8 -*-

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        result = numbers[0]
        count = 1
        for num in numbers[1:]:
            if count==0:
                result = num
                count = 1
            elif num == result:
                count += 1
            else:
                count-=1
        if self.check(numbers,result):
            return result
        return 0

    def check(self,numbers,num):
        count=0
        for n in numbers:
            if n==num:
                count+=1
        return count>(len(numbers)>>1)


if __name__ == '__main__':
    tst = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    s = Solution()
    res = s.MoreThanHalfNum_Solution(tst)
    print(res)
