# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack2.append(node)

    def pop(self):
        if (len(self.stack1) == 0):
            if (len(self.stack2) == 0):
                return None
            else:
                # 把2中的全部移入1中
                self.stack1 = self.stack2[::-1]
                self.stack2 = []
        return self.stack1.pop()


if __name__ == '__main__':
    s = Solution()
    demo=["PSH1","PSH2","PSH3","POP","POP","PSH4","POP","PSH5","POP","POP"]
    for d in demo:
        if('PSH' in d):
            val=d.split('PSH')[1]
            s.push(val)
            print('PHSH了',val)
        else:
            print(s.pop())
