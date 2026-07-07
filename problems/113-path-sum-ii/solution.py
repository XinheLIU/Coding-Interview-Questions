#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node, sum, out, ret):
            if not node: return
            out.append(node.val)
            if sum == node.val and not node.left and not node.right:
                ret.append(out[:])
            dfs(node.left, sum - node.val, out, ret)
            dfs(node.right, sum - node.val, out, ret)
            out.pop()
        ret = []
        dfs(root, sum, [], ret)
        return ret
# @lc code=end
'''
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        paths = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in paths]
'''
'''
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node, sum, out, ret):
            if not node: return
            if sum == node.val and not node.left and not node.right:
                ret.append(out[:] + [node.val])
            dfs(node.left, sum - node.val, out + [node.val], ret)
            dfs(node.right, sum - node.val, out + [node.val], ret)
        ret = []
        dfs(root, sum, [], ret)
        return ret
'''
