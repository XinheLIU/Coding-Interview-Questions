#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ret = 1
        def depth(root):
            nonlocal ret
            if not root: 
                return 0
            l, r = depth(root.left), depth(root.right)
            ret = max(ret, l + r + 1)
            return max(l, r) + 1
        depth(root)
        return ret - 1
# @lc code=end

