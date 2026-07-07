#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return 0
            l, r = helper(root.left), helper(root.right)
            if l != - 1 and r != -1 and abs(l-r) <= 1:
                return max(l, r) + 1
            return -1
        return helper(root) != -1
# @lc code=end

