
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Invariant: prev holds the already-reversed prefix, cur is the next node
        # to move onto it. Each step flips exactly one link.
        cur, prev = head, None
        while cur:
            # Tuple assignment evaluates the whole right side first, so cur.next
            # is read before it is overwritten — no temporary needed.
            cur.next, prev, cur = prev, cur, cur.next
        return prev  # cur ran off the end; prev is the original tail
# @lc code=end
