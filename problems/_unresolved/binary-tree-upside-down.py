# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def reverse(self, root):
    """
    input: TreeNode root
    return: TreeNode
    """
    if not root:
      return root
    if not root.left and not root.right:
      return root
    left_tree = self.reverse(root.left)
    root.left.right = root
    root.left.left = root.right
    root.left, root.right = None, None
    return left_tree