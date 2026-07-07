# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
pre (root)  (left)  (right)
     1,      2,4,5,  3,6,7
post (left)  (right)  (root)
      4,5,2,  6,7,3,   1
'''

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre or not post:
            return None
        root = TreeNode(pre[0])
        if len(post) == 1:
            return root
        rightrootPos = pre.index(post[-2])
        root.left = self.constructFromPrePost(pre[1:rightrootPos], post[:rightrootPos - 1])
        root.right = self.constructFromPrePost(pre[rightrootPos:], post[rightrootPos - 1:-1])
        return root