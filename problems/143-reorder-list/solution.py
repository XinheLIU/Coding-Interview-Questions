# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: 'ListNode') -> 'None':
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        head1, head2 = head, slow.next
        # split
        slow.next = None
        # reverse
        cur, pre = head2, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        # merge
        cur1, cur2 = head1, pre
        while cur2:
            nex1, nex2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = nex1
            cur1, cur2 = nex1, nex2
