# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        if head is None:
            return True
        # find the (first) mid point of linked list
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        cur, prev = slow.next, None
        # reverse the other half
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        # start to compare
        p1, p2 = prev, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        # p1 should move the the end
        return p1 is None