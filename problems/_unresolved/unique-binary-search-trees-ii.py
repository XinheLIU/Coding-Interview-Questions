# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n): 
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n: return []
        memo = {}
        def node(val, left, right):
            root, root.left, root.right = TreeNode(val), left, right
            return root
        def trees(start, end):
            if (start, end) not in memo:
                memo[start, end] = [node(root, left, right)
                    for root in range(start, end + 1)
                    for left in trees(start, root - 1)
                    for right in trees(root + 1, end)] or [None]
            return memo[start, end]
        return trees(1, n)
        
"""
#
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        return self.dfs(1, n)
        
    def dfs(self, start, end):
        if start > end: return [None]
        res = []
        for rootval in range(start, end+1):
            LeftTree = self.dfs(start, rootval-1)
            RightTree = self.dfs(rootval + 1, end)
            for i in LeftTree:
                for j in RightTree:
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
"""