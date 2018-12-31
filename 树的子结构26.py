class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        # 空树不是任意一个树的子结构
        if pRoot1 and pRoot2:
            # 先寻找到和tree2根节点一样的tree1的节点，并判断子树结构是否一致
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HasTree2(pRoot1, pRoot2)
            # 结果False就再对左子树遍历
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            # 结果继续False就再对右子树遍历
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesTree1HasTree2(self, pRoot1, pRoot2):
        # pRoot2为空就可以返回True
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1HasTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HasTree2(pRoot1.right, pRoot2.right)
