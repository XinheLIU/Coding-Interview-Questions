class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # since it is a BST, the lowest diff is between nodes next to each other
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
        
'''
class Solution(object):
    def getMinimumDifference(self, root):
        nums = self.inorder(root)
        return min(nums[i+1]-nums[i] for i in range(len(nums)-1))
        
    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []
'''