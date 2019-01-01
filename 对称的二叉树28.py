class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.symmetrical(pRoot, pRoot)

    def symmetrical(self, pRoot1, pRoot2):
        # 遍历到没有节点了--一样
        if not pRoot1 and not pRoot2:
            return True
        # 有一个有节点还有一个没了--不对称
        if not pRoot1 or not pRoot2:
            return False
        # 左右节点的值不一样--不对称
        if pRoot1.val != pRoot2.val:
            return False
        return self.symmetrical(pRoot1.right, pRoot2.left) and self.symmetrical(pRoot1.left, pRoot2.right)