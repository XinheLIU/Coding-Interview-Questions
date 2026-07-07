# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
'''
# If the middle is the one before: we need

class Solution(object):
  def middleNode(self, head):
    """
    input: ListNode head
    return: ListNode
    """
    if not head:
      return head
    self.next = head
    fast = slow = self
    while fast and fast.next:
      fast, slow = fast.next.next, slow.next
    return slow
'''   