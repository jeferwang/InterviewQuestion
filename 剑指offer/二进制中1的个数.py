# -*- coding:utf-8 -*-
# class Solution:
#     def NumberOf1(self, n):
#         # write code here
#         count = 0
#         if n < 0:
#             n = n & 0x7FFFFFFFffffff
#             count += 1
#         while n != 0:
#             count += n & 1
#             n = n >> 1
#         return count

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        count = 0
        while n != 0:
            count += 1
            n = 2**8-(n & (n - 1))
        return count


if __name__ == '__main__':
    s = Solution()
    c = s.NumberOf1(-10)
    print(c)
