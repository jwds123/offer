#o6
'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 根据前序遍历与中序遍历返回二叉树
    def reConstructBinaryTree1(self, pre, tin):
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None
        root=TreeNode(pre[0])
        i=tin.index(pre[0])
        root.left=self.reConstructBinaryTree1(pre[1:i+1],tin[:i])
        root.right=self.reConstructBinaryTree1(pre[i+1:],tin[i+1:])
    
        return root
    # 根据后序遍历与中序遍历返回二叉树
    def reConstructBinaryTree2(self, post, tin):
        if not post and not tin:
            return None
        if set(post) != set(tin):
            return None
        root=TreeNode(post[-1])
        i=tin.index(post[-1])
        root.left= self.reConstructBinaryTree2(post[0:i], tin[:i])
        root.right = self.reConstructBinaryTree2(post[i:-1], tin[i + 1:])
        return root

    # 根据先序遍历与后序遍历返回二叉树
    def reConstructBinaryTree3(self, pre, post):
        if not post and not pre:
            return None
        if set(post) != set(pre):
            return None
        if pre[0]!=post[-1]:
            return None
        root = TreeNode(pre[0])
        if len(pre)>1:
            i=post.index(pre[1])
            root.left = self.reConstructBinaryTree3(pre[1:i+2],post[:i+1])
            root.right = self.reConstructBinaryTree3(pre[i+2:],post[i+1:-1])
        return root

# 按层序遍历输出树中某一层的值
def PrintNodeAtLevel(treeNode, depth):
    '''
    depth为0就直接输出根节点；
    递归输出某层的左子树与右子树的值
    '''
    if not treeNode or depth < 0:
        return 0
    if depth == 0:
        print(treeNode.val)
        return 1
    PrintNodeAtLevel(treeNode.left, depth-1)
    PrintNodeAtLevel(treeNode.right, depth-1)

# 已知树的深度按层遍历输出树的值
def PrintNodeByLevel(treeNode, depth):
    for level in range(depth):
        PrintNodeAtLevel(treeNode, level)


def main():
    sol=Solution()
    pre = [5, 3, 2, 1, 4, 7, 6, 8]
    tin = [1,2,3,4,5,6,7,8]
    post = [1, 2, 4, 3, 6, 8, 7, 5]
    newTree = sol.reConstructBinaryTree1(pre, tin)
    newTree2 = sol.reConstructBinaryTree2(post, tin)
    newTree3 = sol.reConstructBinaryTree3(pre, post)
    PrintNodeAtLevel(newTree3, 3)

if __name__ == '__main__':
    main()
