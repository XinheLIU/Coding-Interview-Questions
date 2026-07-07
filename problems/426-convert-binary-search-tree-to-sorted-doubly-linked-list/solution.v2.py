"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        pre, head = None, None
        def inorder(node):
            nonlocal pre, head
            if not node:
                return 
            inorder(node.left)
            if not head:
                head = node
            else:
                pre.right = node
                node.left = pre
            pre = node
            inorder(node.right)
        if not root: return None
        inorder(root)
        pre.right = head
        head.left = pre
        return head