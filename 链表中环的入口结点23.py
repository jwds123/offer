class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        slow=pHead.next
        fast=slow.next
        while fast != slow and fast.next:
            slow=slow.next
            fast=fast.next.next
        #表明有环。证明详情见有道笔记
        if slow==fast:
            fast=pHead
            while (fast!=slow):
                fast=fast.next
                slow=slow.next
            return fast
        return None