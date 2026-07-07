 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:   
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        p, stack, ret = root,[],[]
        while p or len(stack):
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            k -= 1
            if not k:
                return p.val
            p = p.right

 '''
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]
'''