#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Invariant: prev sits immediately before the pair being swapped, so
        # prev -> first -> second becomes prev -> second -> first.
        # The dummy head turns the first pair into an interior case like the rest.
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:  # a lone final node stays put
            first, second = prev.next, prev.next.next
            # Order matters: first must adopt second's successor before second
            # points back at first, or the tail of the list is dropped.
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first  # first is now the tail of the swapped pair
        return dummy.next
# @lc code=end
