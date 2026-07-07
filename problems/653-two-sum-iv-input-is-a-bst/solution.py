#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def helper(root, k, s):
            if not root:
                return False
            if k - root.val in s:
                return True
            s.add(root.val)
            return helper(root.left, k, s) or helper(root.right, k, s)
        return helper(root, k, set())
# @lc code=end

