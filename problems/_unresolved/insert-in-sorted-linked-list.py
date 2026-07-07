# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def insert(self, head, value):
    """
    input: ListNode head, int value
    return: ListNode
    """
    new_node = ListNode(value) 
    if not head or value < head.val:
      new_node.next = head
      return new_node
    else:
      search = head
      while search.next and search.next.val < value:
        search = search.next
      #after search 
      new_node.next = search.next
      search.next = new_node
      return head