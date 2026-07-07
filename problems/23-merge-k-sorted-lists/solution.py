# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        n = len(lists)
        if n == 0: return []
        while n > 1:
            k = (n + 1) // 2
            for i in range(n // 2):
                lists[i] = self.merge2Lists(lists[i], lists[i+k])
            n = k
        return lists[0] 
    
    def merge2Lists(self, l1, l2) -> 'ListNode':
        if not l1 or (l2 and l2.val < l1.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.merge2Lists(l1.next, l2)
        return l1