# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSame(self, x, y):
        if not x and not y:
            return True
        if not x or not y:
            return False
        if x.val != y.val:
            return False
        return self.isSame(x.left, y.left) and self.isSame(x.right, y.right)
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.isSame(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)