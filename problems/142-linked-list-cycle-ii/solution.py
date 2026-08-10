#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Phase 1 — Floyd's detection (see #141).
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                break
        if not fast or not fast.next:
            return None  # fast ran off the end: no cycle

        # Phase 2 — locate the entry.
        # Let F be head-to-entry and a be entry-to-meeting-point. At the meeting,
        # slow has walked F + a and fast exactly twice that, and their difference
        # is a whole number of laps. That collapses to F == (lap length - a):
        # the distance from head to entry equals the distance from the meeting
        # point to entry. So advance both one step at a time and they collide there.
        slow = head
        while slow is not fast:
            slow, fast = slow.next, fast.next
        return fast
# @lc code=end
