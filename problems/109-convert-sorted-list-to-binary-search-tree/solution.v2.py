# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        # find middle
        prev = fast = slow = head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        fast = slow.next
        prev.next = None
        root.left = self.sortedListToBST(head) if slow is not head else None
        root.right = self.sortedListToBST(fast)
        return root