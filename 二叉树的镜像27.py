class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # 前序遍历所有节点，有子节点的就将左右子节点交换
        if not root:
            return
        if not root.right and not root.left:
            return root

        tmp = root.left
        root.left = root.right
        root.right = tmp

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        return root