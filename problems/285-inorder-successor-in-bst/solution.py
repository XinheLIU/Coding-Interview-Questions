# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # iterative
        stack = []
        b = False
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if b:
                return root
            if root is p: b = True
            root = root.right
        return None