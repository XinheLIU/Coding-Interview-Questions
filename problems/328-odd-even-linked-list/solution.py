# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd, even = head, head.next
        while even and even.next:
            temp = odd.next
            odd.next = even.next
            even.next = even.next.next
            odd.next.next = temp
            odd, even = odd.next, even.next
        return head