# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        self.Solve1(pHead)
        self.Solve2(pHead)
        return self.Solve3(pHead)

    def Solve1(self, node):
        if not node:
            return False
        while node:
            cloneNode = RandomListNode(node.label)
            cloneNode.next = node.next
            cloneNode.random = None
            node.next = cloneNode
            node = cloneNode.next

    def Solve2(self, node):
        if not node:
            return False
        while node:
            cloneNode = node.next
            oldRandNode = node.random
            if oldRandNode:
                cloneNode.random = oldRandNode.next
            node = cloneNode.next

    def Solve3(self, pHead):
        pNode = pHead
        if pNode:
            cloneHead = cloneNode = pNode.next
            pNode.next = cloneNode.next
            pNode = pNode.next
        else:
            return None
        while pNode:
            cloneNode.next = pNode.next
            cloneNode = cloneNode.next
            pNode.next = cloneNode.next
            pNode = pNode.next
        return cloneHead
