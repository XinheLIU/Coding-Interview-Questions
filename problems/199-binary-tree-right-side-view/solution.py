#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(root, ret, depth):
            if not root:
                return
            ret.setdefault(depth, root.val)
            dfs(root.right, ret, depth + 1)
            dfs(root.left, ret, depth + 1)
        ret = {}
        dfs(root, ret, 0)
        return ret.values()
        
# @lc code=end

