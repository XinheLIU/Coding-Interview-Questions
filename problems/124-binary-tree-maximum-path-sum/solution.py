#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(root):
            nonlocal max_sum 
            if not root:
                return 0
            max_l, max_r = max(max_gain(root.left), 0), max(max_gain(root.right),0)
            max_sum = max(max_sum, root.val + max_l + max_r)
            return root.val + max(max_l, max_r)
        max_sum = float('-inf')
        max_gain(root)
        return max_sum
# @lc code=end

