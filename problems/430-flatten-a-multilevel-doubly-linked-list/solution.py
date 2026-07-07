#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        dummy_head = Node(None, None, head, None)
        self.flatten_dfs(dummy_head, head)
        dummy_head.next.prev = None
        return dummy_head.next

    def flatten_dfs(self, prev, cur):
        if not cur:
            return prev
        
        cur.prev = prev
        prev.next = cur
        
        temp_next = cur.next
        tail = self.flatten_dfs(cur, cur.child)
        cur.child = None
        return self.flatten_dfs(tail, temp_next)
        
# @lc code=end

