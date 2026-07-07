# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # we need the maximum depth 
        self.res = 0
        self.hashTable = {}
        self.maxDepth(root)
        return self.res
        
    def maxDepth(self, root):
        if not root:
            return 0
        if root in self.hashTable:
            return self.hashTable(root)
        l, r = self.maxDepth(root.left), self.maxDepth(root.right)
        self.res = max(self.res, l + r)
        self.hashTable[root] = max(l,r) + 1 
        return max(l,r) + 1 