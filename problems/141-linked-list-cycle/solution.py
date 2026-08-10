#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Floyd's cycle detection: fast moves two steps per one of slow, so the
        # gap between them grows by exactly one each iteration. Inside a cycle of
        # length L that gap is taken mod L, so it eventually hits 0 — they meet.
        slow = fast = head
        while fast and fast.next:  # only fast can fall off; checking it covers both
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False
# @lc code=end
