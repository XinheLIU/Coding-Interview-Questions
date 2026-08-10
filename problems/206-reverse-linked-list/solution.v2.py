
# Approach 2: Recursive

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Recurse to the tail first, then flip links on the way back up.
        # new_head is the original tail and is passed through every frame unchanged.
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        # head.next is still the node ahead of us; point it back at head,
        # then cut head's forward link or the two nodes form a cycle.
        head.next.next = head
        head.next = None
        return new_head
# @lc code=end
