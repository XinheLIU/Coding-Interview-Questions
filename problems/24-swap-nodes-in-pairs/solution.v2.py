#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Approach 2: Recursive

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Recursion carries the "node before the pair" implicitly: the caller
        # holds it, so each frame only has to swap its own two nodes and trust
        # the recursive call to return the already-swapped remainder.
        if not head or not head.next:
            return head  # fewer than two nodes left — nothing to swap
        first, second = head, head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        return second  # second is the new head of this pair
# @lc code=end
