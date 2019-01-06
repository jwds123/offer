class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        li = s.split(',')

        def DeserializeTree(li):
            if len(li) == 0:
                return None
            root = None
            val = li.pop(0)
            if val != '#':
                root = TreeNode(int(val))#str-->int
                root.left = DeserializeTree(li)
                root.right = DeserializeTree(li)
            return root

        return DeserializeTree(li)