# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            result = self.isSubTree(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def isSubTree(self, root1, root2):
        if root2 == None:
            return True
        if root1 == None:
            return False
        if root1.val != root2.val:
            return False
        return self.isSubTree(root1.left, root2.left) and self.isSubTree(root1.right, root2.right)
