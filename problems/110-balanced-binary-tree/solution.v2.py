# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # return height or signal
    def helper(self, root: TreeNode) -> float:
        if not root:
            return 0
        l, r = self.helper(root.left), self.helper(root.right)
        if l == -1 or r == -1 or abs(l-r) > 1:
            return -1
        return max(l,r) + 1
        
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root) != -1