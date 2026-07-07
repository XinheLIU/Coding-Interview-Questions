# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # level order traversal
        ret = []
        if not root:
            return ret
        ret, q = [], deque([root])
        while len(q):
            m = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                m = max(m, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(m)
        return ret