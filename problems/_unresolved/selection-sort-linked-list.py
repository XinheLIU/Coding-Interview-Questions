# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def selectionSort(self, head):
    """
    input: ListNode head
    return: ListNode
    """
    # dummy node
    self.next = head
    tail = self
    while tail.next:
      prev, cur = tail, tail.next
      min_node, prev_min_node = cur, prev
      while cur:
        if cur.val < min_node.val:
          min_node, prev_min_node = cur, prev
        prev, cur = cur, cur.next
      prev_min_node.next = min_node.next
      next = tail.next
      tail.next = min_node
      min_node.next = next
      tail = tail.next
    return self.next