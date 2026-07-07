#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def visit(root) -> tuple:
            if not root:
                return 0, 0
            left_rob, left_not_rob = visit(root.left)
            right_rob, right_not_rob = visit(root.right)

            rob = root.val + left_not_rob + right_not_rob
            not_rob = max(left_not_rob, left_rob) + max(right_not_rob, right_rob)
            return rob, not_rob
        return max(visit(root))
# @lc code=end

