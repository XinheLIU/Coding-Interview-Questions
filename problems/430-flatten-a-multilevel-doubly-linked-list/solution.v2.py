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
        cur = head
        while cur:
            if cur.child:
                cur.child = self.flatten(cur.child)
                next = cur.next
                last = cur.child
                while last.next:
                    last = last.next
                # link
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None
                last.next = next
                if next:
                    next.prev = last
            cur = cur.next       
        return head