# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def insert(self, head, index, value):
    """
    input: ListNode head, int index, int value
    return: ListNode
    """
    def searchByIndex(head, index):
      if head is None or index < 0:
        return None
      for _ in range(index):
        head = head.next
        if not head:
          return None
      return head
    
    dummy = ListNode(None)
    dummy.next = head
    insert_place = searchByIndex(dummy, index)
    if insert_place is None:
      return dummy.next
    new_node = ListNode(value)
    new_node.next = insert_place.next
    insert_place.next = new_node
    return dummy.next