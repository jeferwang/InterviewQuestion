# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            headNode=pHead1
            pHead1=pHead1.next
        else:
            headNode=pHead2
            pHead2=pHead2.next
        ptrNode=headNode

        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                ptrNode.next=pHead1
                pHead1=pHead1.next if pHead1.next else None
            else:
                ptrNode.next=pHead2
                pHead2=pHead2.next if pHead2.next else None
            ptrNode=ptrNode.next
        ptrNode.next=pHead1 if pHead1 else pHead2
        return headNode