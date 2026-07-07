# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object): 
  def deleteNodes(self, head, indices):
    """
    input: ListNode head, int[] indices
    return: ListNode
    """
    dummy, i = ListNode(None), 0 # pre-node
    dummy.next = head
    pre = dummy
    while pre.next:
      # delete pre.next
      if i in indices:
        pre.next = pre.next.next
      else:
        pre = pre.next
      i += 1
    return dummy.next