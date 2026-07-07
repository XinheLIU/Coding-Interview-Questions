class Solution:
    def sortList(self, head: 'ListNode') -> 'ListNode':
        # merge sort
        if not head or not head.next: 
            return head
        l1, l2 = self.split(head)
        l1, l2 = self.sortList(l1), self.sortList(l2)
        return self.merge(l1,l2)
    
    def split(self,head):
        f = s = head
        while f.next and f.next.next:
            f, s = f.next.next, s.next
        next, s.next = s.next, None
        return head, next

    def merge(self, one, two):
        if not one: return two
        if not two: return one
        # smaller comes first
        if one.val > two.val:
            one, two = two, one   
        one.next = self.merge(one.next, two)
        return one