# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def searchByIndex(self, head, index):
      if head is None or index < 0:
        return None
      for _ in range(index):
        head = head.next
        if not head:
          return None
      return head
    
  def deleteNode(self, head, index):
    """
    input: ListNode head, int index, int value
    return: ListNode
    """
    dummy = ListNode(None)
    dummy.next = head
    delete_place = self.searchByIndex(dummy, index)
    if not delete_place or not delete_place.next:
      return dummy.next
    delete_place.next = delete_place.next.next
    return dummy.next