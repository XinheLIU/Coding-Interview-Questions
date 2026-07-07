# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        Result = collections.namedtuple("Result", ("node", "dist"))  # sub tree and max dist    
        def helper(node):
            if not node:
                return Result(None, 0)
            l, r = helper(node.left), helper(node.right)
            if l.dist > r.dist:
                return Result(l.node, l.dist + 1)
            elif r.dist > l.dist:
                return Result(r.node, r.dist + 1)
            else:
                return Result(node, l.dist + 1)  #complete binary tree
        return helper(root).nod