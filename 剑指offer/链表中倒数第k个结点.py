# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # 判断是否传入了空指针
        if not head or k==0:
            return  None
        # 定义两个指针同时指向头部
        ptr1=ptr2=head
        # 第二个指针先走k-1步
        for i in range(k-1):
            next=ptr2.next
            if not next:
                return None
            else:
                ptr2=next
        # 两个指针同时走，直到第二个指针到尾部
        while ptr2.next:
            ptr1=ptr1.next
            ptr2=ptr2.next
        # 返回当前指针1所指向的值
        return ptr1
