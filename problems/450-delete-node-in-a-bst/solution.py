# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left or not root.right:
                return root.left if not root.right else root.right
            else:
                # find left most in the right
                leftmost = root.right
                while leftmost.left:
                    leftmost = leftmost.left
                # swap
                root.val = leftmost.val
                root.right = self.deleteNode(root.right, leftmost.val)
        return root