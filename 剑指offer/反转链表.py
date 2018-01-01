# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead:
            return None
        oldNode = tailNode = pHead
        nextNode = pHead.next
        oldNode.next = None
        while nextNode:
            currentNode = nextNode
            if nextNode.next:
                tailNode = nextNode.next
            nextNode = nextNode.next
            currentNode.next = oldNode
            oldNode = currentNode
        return tailNode
