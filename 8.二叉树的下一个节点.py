'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
'''
如果一个节点有右子树，那么下一个节点就是右子树的最左子节点；
该节点没有右子树
    如果该节点是其父节点的左子节点，则父节点是下一个节点
    如果不是的话就查找父节点（符合上一个情况），并返回满足左子节点的节点的父节点
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return
        if pNode.right:
            cur=pNode.right
            while cur.left:
                cur=cur.left
            return cur
        else:
            if not pNode.next:
                return
            elif pNode.next.left==pNode:
                return pNode.next
            elif pNode.next.next.left==pNode.next:
                return pNode.next.next
            else:
                return
