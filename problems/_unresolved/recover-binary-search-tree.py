# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Morris Traversal
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # Set current to root of binary tree           
        cur, parent, first, second = root, None,TreeNode(None), TreeNode(None)
        while cur:
            if not cur.left:
                # visit
                if parent and parent.val > cur.val:
                    if not first.val:
                        first = parent
                    second = cur
                parent, cur = cur, cur.right
            else:
                # find predecessor : left most on the right
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    # connect the thread
                    pre.right, cur = cur, cur.left
                else:  # threding already exist
                    pre.right = None
                    # visit
                    if parent != TreeNode(None) and parent.val > cur.val:
                        if not first.val:
                            first = parent
                        second = cur
                    parent, cur = cur, cur.right
            # swap
        if first is not TreeNode(None) and second is not TreeNode(None):
            first.val, second.val = second.val, first.val