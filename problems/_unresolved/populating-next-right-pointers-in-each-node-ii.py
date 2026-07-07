# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        first, p = None, None # first in the next level 
        while root:
            if not first:
                first = root.left if root.left else root.right
            if root.left:
                if p:
                    p.next = root.left
                p = root.left
            if root.right:
                if p:
                    p.next = root.right
                p = root.right
            # to right or to the next level
            if root.next:
                root = root.next
            else:
                root, p, first = first, None, None

'''
# recursive: right but not constant space
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        # subtree might be broken, find by looking same level as root
        p = root.next
        while(p):
            if p.left:
                p = p.left
                break
            if p.right:
                p = p.right
                break
            p = p.next
        if root.right:
            root.right.next = p
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = p
        self.connect(root.right)
        self.connect(root.left)   
'''