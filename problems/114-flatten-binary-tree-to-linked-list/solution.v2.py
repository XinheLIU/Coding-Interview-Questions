# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # dfs 
        if not root:
            return None
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        temp, root.right, root.left = root.right, root.left, None
        while root.right:
            root = root.right
        root.right = temp
        
        
        '''
class Solution(object):
    def flatten(self, root):
        # non recursive #
        while root:
            if root.left:
                p = root.left
                while p.right:
                    p = p.right
                root.right, root.left, p.right = root.left, None, root.right
            root = root.right     
        
        '''
        