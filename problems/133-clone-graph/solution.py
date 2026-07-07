#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node, visited):
            if not node:
                return None
            if node in visited:
                return visited[node]
            node_ = Node(node.val, [])
            visited[node] = node_
            for n in node.neighbors:
                node_.neighbors.append(dfs(n, visited))
            return node_
        return dfs(node, {})
# @lc code=end
'''
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {node: Node(node.val, [])}
        q = deque([node])
        
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # make a copy
                    visited[neighbor]  = Node(neighbor.val, [])
                    q.append(neighbor)
                # copy edge
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
'''