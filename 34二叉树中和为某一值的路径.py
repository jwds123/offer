from 重建二叉树 import *


class Solution(Traverse):
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.onePath = []
        self.PathArray = []

    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return self.PathArray
        # 对于每个节点，先加上它的值，同时将该节点加入onePath中
        expectNumber -= root.val
        self.onePath.append(root.val)
        # 如果该节点是叶子节点，同时该条路径==和，将该路径加入PathArray，同时将该叶子节点
        # 从onePath中剔除回到父节点（前序遍历）
        if expectNumber == 0 and not root.left and not root.right:
            self.PathArray.append(self.onePath[:])
        # 前序遍历：不需要判断root.left/right 为空：空就返回当前PathArray
        elif expectNumber > 0:
            self.FindPath(root.left, expectNumber)
            self.FindPath(root.right, expectNumber)

        self.onePath.pop()
        return self.PathArray

def main():
    sol=Solution()
    pre = [5, 3, 2, 1, 4, 7, 6, 8]
    tin = [1,2,3,4,5,6,7,8]
    post = [1, 2, 4, 3, 6, 8, 7, 5]
    newTree = sol.reConstructBinaryTree1(pre, tin)
    newTree2 = sol.reConstructBinaryTree2(post, tin)
    newTree3 = sol.reConstructBinaryTree3(pre, post)
    path=sol.FindPath(newTree,11)
    print(path)



if __name__ == '__main__':
    main()
