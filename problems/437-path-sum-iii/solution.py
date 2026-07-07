#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node, prev_sum, sum, m):
            if not node: return 0
            m[prev_sum] += 1
            cur_sum = prev_sum + node.val
            target = cur_sum - sum
            ret = m[target]
            ret += dfs(node.left, cur_sum, sum, m) + dfs(node.right, cur_sum, sum, m)
            m[prev_sum] -= 1
            return ret
        return dfs(root, 0, sum, collections.defaultdict(int))

# @lc code=end
'''
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        else:
            return self.DFS(root, sum, 0)+self.pathSum(root.left, sum)+self.pathSum(root.right, sum)

    def DFS(self, root, su, tmp):
        if None==root:
            return 0
        else:
            flag=0
            if su==tmp+root.val:
                flag=1
            return flag+self.DFS(root.left, su, tmp+root.val)+self.DFS(root.right, su, tmp+root.val)
'''