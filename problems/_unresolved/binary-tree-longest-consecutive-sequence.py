# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive(self, root):
        # Write your code here
        return self.helper(root, None, 0)
    
    def helper(self, root, parent, len):
        if root is None:
            return len

        if parent != None and root.val == parent.val + 1:
            len += 1
        else:
            len = 1
        return max(len, max(self.helper(root.left, root, len), \
                            self.helper(root.right, root, len)))