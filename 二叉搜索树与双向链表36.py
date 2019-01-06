class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    定义两个辅助节点listHead(链表头节点)、listNode(链表尾节点)。事实上，二叉树只是换了种形式的链表；
    listHead用于记录链表的头节点，用于最后算法的返回；listNode用于定位当前需要更改指向的节点。
    '''
    def __init__(self):
        self.listHead = None
        self.listNode = None

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.Convert(pRootOfTree.left)
        if not self.listHead:
            self.listHead=self.listNode=pRootOfTree
        else:#二叉树改成双向的链条
            self.listNode.right=pRootOfTree
            pRootOfTree.left=self.listNode
            self.listNode=pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead

# 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return
        if set(pre)!=set(tin):
            return
        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i + 1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i + 1:], tin[i + 1:])
        return root
#打印双向链条
    def print_node(self,head):
        #先向右打印
        while head.right:
            print(head.val, end=" ")
            head = head.right
        print(head.val)
        #再向左打印
        while head:
            print(head.val, end=" ")
            head = head.left

def main():
    solution = Solution()
    preorder_seq = [4, 2, 1, 3, 6, 5, 7]
    middleorder_seq = [1, 2, 3, 4, 5, 6, 7]
    Treeroot=solution.reConstructBinaryTree(preorder_seq,middleorder_seq)
    head=solution.Convert(Treeroot)
    solution.print_node(head)

if __name__ == '__main__':
    main()



