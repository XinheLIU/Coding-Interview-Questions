# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val) if root.left else TreeNode(val)
        else:
            root.right = self.insertIntoBST(root.right, val) if root.right else TreeNode(val)
        return root