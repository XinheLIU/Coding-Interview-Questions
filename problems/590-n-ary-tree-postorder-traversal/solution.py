#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)
                
        return output[::-1] 
# @lc code=end
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        if not root:
            return ret
        for child in root.children:
            ret += self.postorder(child)
        ret.append(root.val)
        return ret
"""
