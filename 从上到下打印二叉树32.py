'''
1.不分层打印
2.分层打印
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from collections import deque
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = deque()
        res = []
        queue.append(root)
        while queue:
            l=len(queue)
            for i in range(l):
                #先进的node打印；再将node左右节点加入队列
                node=queue.popleft()
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

#多行打印二叉树
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue=[pRoot]
        
        level=0
        res=[]
        while queue:
            next_queue=[]
            level_res=[]
            '''
            level_res:该层的所有节点
            next_queue:该层的所有节点的左右子节点
            '''
            for node in queue:
                level_res.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            res.append(level_res)
            queue=next_queue
        return res

#之字形打印二叉树
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue = [pRoot]
        i = 0
        level = 0
        res = []
        while queue:
            i += 1
            next_queue = []
            level_res = []
            '''
            level_res:该层的所有节点
            next_queue:该层的所有节点的左右子节点
            '''
            for node in queue:
                level_res.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if i % 2 == 0:
                res.append(level_res[::-1])
            else:
                res.append(level_res)
            queue = next_queue
        # print(res)
        return res