# -*- coding:utf-8 -*-
import functools


class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        numbers = list(map(str, numbers))
        key = functools.cmp_to_key(lambda a, b: int(a + b) - int(b + a))
        numbers.sort(key=key)
        return ''.join(numbers)


if __name__ == '__main__':
    s = Solution()
    print(s.PrintMinNumber([3, 32, 321]))  # 321323
    print(s.PrintMinNumber([4, 10, 81]))  # 10481
