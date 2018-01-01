# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        _ls_fib = [1, 1]
        if 0 == n:
            return 0
        if 0 < n <= 2:
            return _ls_fib[n - 1]
        for i in range(3, n + 1):
            _ls_fib.append(_ls_fib[-1] + _ls_fib[-2])
        return _ls_fib[-1]


if __name__ == '__main__':
    s = Solution()
    fib = s.Fibonacci(5)
    # 1 1 2 3 5 8 13
    print(fib)
