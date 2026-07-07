# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return min(inorder(root), key = lambda x: abs(target - x))
'''
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        ret = root.val
        if root.left and root.val > target:
            l = self.closestValue(root.left, target)
            if abs(ret - target) > abs(l - target):
                ret = l
        if root.right and root.val < target:
            r = self.closestValue(root.right, target)
            if abs(ret - target) > abs(r - target):
                ret = r
        return ret
'''