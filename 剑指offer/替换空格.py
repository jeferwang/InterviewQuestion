# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    @staticmethod
    def replaceSpace(s):
        s_list = list(s)
        s_len = len(s)
        space_num = 0
        for c in s_list:
            if ' ' == c:
                space_num += 1
        # 对原字符串扩容
        s_list = s_list + [''] * (space_num * 2)
        # 从后往前推
        i = len(s_list) - 1
        j = s_len - 1
        while i >= 0:
            if ' ' == s_list[j]:
                s_list[i] = '0'
                i-=1
                s_list[i] = '2'
                i-=1
                s_list[i] = '%'
                i-=1
            else:
                s_list[i] = s_list[j]
                i-=1
            j-=1
        return ''.join(s_list)


if __name__ == '__main__':
    Solution.replaceSpace(' Hello World ')
