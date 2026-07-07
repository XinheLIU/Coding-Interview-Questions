# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def isTweakedIdentical(self, one, two):
    """
    input: TreeNode one, TreeNode two
    return: boolean
    """
    if not one and not two:
      return True
    elif not one or not two:
      return False
    if one.val != two.val:
      return False
    return (self.isTweakedIdentical(one.left, two.left) and self.isTweakedIdentical(one.right, two.right)) or \
            (self.isTweakedIdentical(one.right, two.left) and self.isTweakedIdentical(one.left, two.right))