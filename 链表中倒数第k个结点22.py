class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k <= 0 or head == None:
            return None
        First = head
        Second = None
        i= 0

        #指针1先走k-1步，这样指针1和2始终距离k-1步
        #当指针1走完时，指针2就走到了第n-(k-1)个节点

        #必须首先知道整个链条长度，如果低于k就返回空，所以指针1需要走完整个链条
        while i < k - 1:

            if not First.next:
                return None
            First = First.next
            i += 1

        Second = head
        while First.next:
            Second = Second.next
            First = First.next
            i += 1

        return Second
