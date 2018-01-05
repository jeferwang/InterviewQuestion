# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        root_ls = [root]
        result = []
        while root_ls:
            new_root_ls = []
            for r in root_ls:
                result.append(r.val)
                if r.left:
                    new_root_ls.append(r.left)
                if r.right:
                    new_root_ls.append(r.right)
            root_ls = new_root_ls
        return result
