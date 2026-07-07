# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # in cpp, use pointers, python using slice makes more sense
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        rootPos = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1+rootPos], inorder[:rootPos])
        root.right = self.buildTree(preorder[1+rootPos:], inorder[rootPos+1:])
        return root