# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, ret):
            if not root:
                return -1 # height
            height = 1 + max(dfs(root.left, ret), dfs(root.right, ret))
            while height >= len(ret):
                ret.append([])
            ret[height].append(root.val)
            return height
        ret = []
        dfs(root, ret)
        return ret  