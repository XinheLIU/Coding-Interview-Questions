# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):    
    def sumNumbers(self, root, sum = 0):
        if not root:
            return 0
        sum = sum * 10 + root.val
        if not root.left and not root.right:
            return sum
        else:
            return self.sumNumbers(root.left, sum) + self.sumNumbers(root.right, sum)