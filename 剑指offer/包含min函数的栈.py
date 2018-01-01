# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minList = []

    def push(self, node):
        if not self.minList:
            self.minList.append(node)
        else:
            self.minList.append(min(self.minList[-1], node))
        self.stack.append(node)

    def pop(self):
        if not self.stack:
            return None
        self.minList.pop()
        return self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def min(self):
        if not self.minList:
            return None
        return self.minList[-1]
