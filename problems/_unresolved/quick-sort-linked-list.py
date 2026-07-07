# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def get_tail(self, node):
    while node.next:
      node = node.next
    return node
  
  def quickSort(self, head):
    """
    input: ListNode head
    return: ListNode
    """
    if head is None:
      return None
    tail = self.get_tail(head)
    head, tail = self.quick_sort(head, tail)
    tail.next = None
    return head

  def quick_sort(self, head, tail):
    """
    sort in place
    input: head node, tail node
    return: ListNode head, tail
    """
    if head is not tail:
      head_left, tail_left, head_ref, tail_ref, head_right, tail_right = self.partition(head, tail)
      if head_left is None:
        head = head_ref
      else:
        head_left, tail_left = self.quick_sort(head_left, tail_left)
        head = head_left
        tail_left.next = head_ref
      if head_right is None:
        tail = tail_ref
      else:
        head_right, tail_right = self.quick_sort(head_right, tail_right)
        tail_ref.next = head_right
        tail = tail_right
    return head, tail

  def partition(self, head, tail):
    reference = tail
    head_ref, tail_ref = reference, reference
    head_left, tail_left, head_right, tail_right = None, None, None, None
    dummy = ListNode(None)
    dummy.next = head
    node = dummy
    while node.next is not tail:
      node = node.next
      if node.val > reference.val:
        # put to the right
        if head_right is not None:
          tail_right.next = node
          tail_right = node
        else:
          head_right = node
          tail_right = node
      elif node.val < reference.val:
        # put to the left
        if head_left is not None:
          tail_left.next = node
          tail_left = node
        else:
          head_left = node
          tail_left = node
      else:
        # node into the refenrece part
        tail_ref.next = node
        tail_ref = node
    return head_left, tail_left, head_ref, tail_ref, head_right, tail_right