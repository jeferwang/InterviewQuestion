# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if not numbers:
            return  False
        # 遍历下标
        for n in range(len(numbers)):
            # 值和下标不相等
            while numbers[n] != n:
                if numbers[numbers[n]] == numbers[n]:
                    # 找到了
                    duplication[0] = numbers[n]
                    return True
                temp = numbers[numbers[n]]
                numbers[numbers[n]] = numbers[n]
                numbers[n] = temp
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.duplicate([0, 1, 2, 3, 4, 5, 6, 6], [0]))
