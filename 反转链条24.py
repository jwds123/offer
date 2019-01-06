class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return
        cur = None
        pre = None
        # 已经反转的前长度为k-1链条
        tmp = pHead
        while tmp:
            cur = tmp.next
            # tmp指向前一个。链表：只需要知道下一个就行
            tmp.next = pre
            pre = tmp
            tmp = cur
        return pre
