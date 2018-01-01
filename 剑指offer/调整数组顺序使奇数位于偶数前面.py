# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        if len(array) == 0:
            return array
        # 偶数指针和奇数指针
        ptr_o = ptr_j = 0
        while ptr_o < len(array) and ptr_j < len(array):
            if (array[ptr_o] % 2 == 1):
                # 如果是奇数则指针后移
                ptr_o += 1
            else:
                ptr_j = ptr_o
                while  ptr_j < len(array) and array[ptr_j] % 2 == 0:
                    ptr_j += 1
                if ptr_j == len(array):
                    break
                else:
                    temp = array[ptr_j]
                    while ptr_j >= ptr_o:
                        array[ptr_j] = array[ptr_j - 1]
                        ptr_j -= 1
                    array[ptr_o] = temp
                ptr_o += 1
        return array


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    s = Solution()
    print(s.reOrderArray(arr))
