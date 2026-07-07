# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        return [str(root.val) + "->" + val for val in self.binaryTreePaths(root.left)] + \
                [str(root.val) + "->" + val for val in self.binaryTreePaths(root.right)]

'''
class Solution(object):
  def binaryTreePaths(self, root):
    """
    input: TreeNode root
    return: string[]
    """
    if not root:
      return []
    self.res = []
    self.helper(root, "")
    return self.res
    
  def helper(self, root, out):
    if not root.left and not root.right:
      self.res.append(out + str(root.val) )
      return
    if root.left:
      self.helper(root.left, out + str(root.val) + "->" )
    if root.right:
       self.helper(root.right, out + str(root.val) + "->")

'''