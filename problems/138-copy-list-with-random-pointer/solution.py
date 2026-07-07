"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        dic = {}
        new_head = Node(head.val, None, None)
        dic[head] = new_head
        p, q = head, new_head
        while p:
            q.random = p.random
            if p.next:
                q.next = Node(p.next.val,None,None)
                dic[p.next] = q.next
            else:
                q.next = None
            p, q = p.next, q.next
        
        p = new_head
        while p:
            if p.random:
                p.random = dic[p.random]
            else:
                p.random = None
            p = p.next
        return new_head