import random
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        self.cloneNode(pHead)
        self.sibClone(pHead)
        return self.splitNode(pHead)

    # 复制节点在原节点之后
    def cloneNode(self,pHead):
        pNode = pHead  # 链表指针
        while pNode:
            pCloned = RandomListNode(pNode.label)  # 链条上的每个节点
            # pCloned.label = pNode.label
            pCloned.next = pNode.next
            pCloned.random = None
            pNode.next = pCloned
            pNode = pCloned.next
        #self.print_nodes(pHead)

    def sibClone(self,pHead):    # 复制random节点
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random:
                pCloned.random = pNode.random.next
            pNode = pCloned.next
        #self.print_nodes(pHead)

    def splitNode(self,pHead):
        # 将新旧链表分离
        pNode = pHead
        pClonedHead = None
        pClonedNode = None
        if pNode:
            pClonedHead = pClonedNode = pNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        #self.print_nodes(pClonedHead)

        return pClonedHead

    def construct_nodes(self,pHead):
        """
        构造一个简单的复杂链表
        :param pHead: list
        :return: Nodes
        """
        if not pHead:
            return RandomListNode
        move = head = RandomListNode(pHead.pop(0))
        nodes = [None, head]
        for v in pHead:
            tmp = RandomListNode(v)
            move.next = tmp
            nodes.append(tmp)
            move = move.next
        # print [node.val for node in nodes if node]
        move = head
        while move:
            # 设置other指针为随机结点
            move.random = random.choice(nodes)
            move = move.next
        return head

    def print_nodes(self,head):
        # 打印结点值，结点other的值，用来比较
        ret = []
        while head:
            tmp = [head.label]
            if head.random:
                tmp.append(head.random.label)
            ret.append(tmp)
            head = head.next
        print(ret)


if __name__ == '__main__':
    sol=Solution()
    link = sol.construct_nodes([1, 2, 3, 4, 5,6,9])
    sol.print_nodes(link)
    test = sol.Clone(link)  # 复制
    #sol.print_nodes(test)




