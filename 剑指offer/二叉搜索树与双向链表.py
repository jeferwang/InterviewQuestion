"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if self.IsSingleNode(pRootOfTree):
            return pRootOfTree
        if self.IsLastTree(pRootOfTree):
            return self.findHead(self.Solve(pRootOfTree))
        self.Solve(pRootOfTree)
        return self.findHead(pRootOfTree)

    def Solve(self, rootNode):
        if not rootNode:
            return None
        if self.IsSingleNode(rootNode):
            return rootNode
        if self.IsLastTree(rootNode):
            if rootNode.left:
                left = rootNode.left
                left.right = rootNode
            if rootNode.right:
                right = rootNode.right
                right.left = rootNode
            return rootNode
        else:
            leftResult = self.Solve(rootNode.left)
            rightResult = self.Solve(rootNode.right)
            leftTail = self.findTail(leftResult)
            rightHead = self.findHead(rightResult)
            if leftTail:
                rootNode.left = leftTail
                leftTail.right = rootNode
            else:
                rootNode.left = None
            if rightHead:
                rootNode.right = rightHead
                rightHead.left = rootNode
            else:
                rootNode.right = None
            return rootNode

    def IsLastTree(self, rootNode):
        if self.IsSingleNode(rootNode):
            return False
        if self.IsSingleNode(rootNode.left) and self.IsSingleNode(rootNode.right):
            return True
        return False

    def IsSingleNode(self, node):
        if not node or not (node.left or node.right):
            return True
        return False

    def findHead(self, someNode):
        if not someNode:
            return None
        while someNode.left:
            someNode = someNode.left
        return someNode

    def findTail(self, someNode):
        if not someNode:
            return None
        while someNode.right:
            someNode = someNode.right
        return someNode

"""


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        left = self.Convert(pRootOfTree.left)
        p = left
        while p and p.right:
            p = p.right
        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p
        right = self.Convert(pRootOfTree.right)
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right
        return left if left else pRootOfTree

