# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def insertionSort(self, head):
    """
    input: ListNode head
    return: ListNode
    """
    if not head:
      return head
    sorted = head
    head = head.next
    sorted.next = None
    while head:
      cur = head
      head = head.next
      if cur.val < sorted.val:
        # insert before head
        cur.next = sorted
        sorted = cur
      else:
        search = sorted
        # search the node pre to insert pos
        while search.next and cur.val > search.next.val:
          search = search.next
        cur.next = search.next
        search.next = cur
    return sorted