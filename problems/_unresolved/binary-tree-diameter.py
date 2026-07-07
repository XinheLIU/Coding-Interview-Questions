"""
Given a binary tree in which each node contains an integer number. The diameter is defined as the longest distance from one leaf node to another leaf node. The distance is the number of nodes on the path.

If there does not exist any such paths, return 0.

Examples

    5

  /    \

2      11

     /    \

    6     14

The diameter of this tree is 4 (2 → 5 → 11 → 14)

How is the binary tree represented?

We use the level order traversal sequence with a special symbol "#" denoting the null node.

For Example:

The sequence [1, 2, 3, #, #, 4] represents the following binary tree:

    1

  /   \

 2     3

      /

    4

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    # we need the max depth some from left and sum sub tree
    def diameter(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # we need the maximum depth
        if not root or (not root.left and not root.right):
            return 0
        self.res = 0
        self.maxDepth(root)
        return self.res
        
    def maxDepth(self, root):
        if not root:
          return 0
        l, r = self.maxDepth(root.left), self.maxDepth(root.right)
        if root.left and root.right:
          self.res = max(self.res, l + r + 1)
        return max(l,r) + 1 