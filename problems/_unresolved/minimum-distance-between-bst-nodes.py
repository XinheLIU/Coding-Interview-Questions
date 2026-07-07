# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('inf')
        self.helper(root,-1,-1)
        return self.res
    
    def helper(self, root, low, high):
        if not root:
            return
        if low != -1:
            self.res = min(self.res, root.val - low)
        if high != -1:
            self.res = min(self.res, high - root.val)
        self.helper(root.left, low, root.val)
        self.helper(root.right, root.val, high)


# same as question 530
'''
class Solution(object):
    def getMinimumDifference(self, root):
        nums = self.inorder(root)
        return min(nums[i+1]-nums[i] for i in range(len(nums)-1))
        
    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []
'''