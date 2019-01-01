class Solution:
    def __init__(self):
        self.data     = []#数据栈
        self.minIndex = []#最小值辅助栈
    def push(self, node):
        # 需要同时更新两个栈
        self.data.append(node)
        #1.min是空的2.新加入的元素小于min栈顶的值=>将新元素压入min中，否则就将min栈顶再压入
        if not self.minIndex or node<self.minIndex[-1]:
            self.minIndex.append(node)

    def pop(self):
        # 当data中弹出的是当前最小值是，辅助栈的栈顶元素也需要弹出
        if self.data[-1]==self.minIndex[-1]:
            self.minIndex.pop()
        self.data.pop()

    def top(self):
        # write code here
        return self.data[-1]
    def min(self):
        # write code here
        return self.minIndex[-1]
