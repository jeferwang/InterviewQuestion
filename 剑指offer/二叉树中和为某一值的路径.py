# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        self.result = []
        self.root = root
        self.expectNumber = expectNumber
        if not root:
            return []
        self.Find2(root, [])
        return self.result

    def Find2(self, root, curr_list):
        curr_list2 = curr_list[:]
        curr_list2.append(root.val)
        if root.left:
            self.Find2(root.left, curr_list2)
        if root.right:
            self.Find2(root.right, curr_list2)
        # 走到端点的时候才计算路径
        if not root.left and not root.right and sum(curr_list2) == self.expectNumber:
            self.result.append(curr_list2)
