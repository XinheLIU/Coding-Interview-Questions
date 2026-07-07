rclass Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        self.next = head
        prev = self 
        for _ in range(1,m):
            prev = prev.next
        cur = prev.next
        # move nodes after cur to after prev one by one 
        for _ in range(n-m):
            temp, cur.next = cur.next, cur.next.next
            temp.next, prev.next  = prev.next, temp
        return self.next