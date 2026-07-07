#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (42.23%)
# Likes:    2455
# Dislikes: 365
# Total Accepted:    280.2K
# Total Submissions: 663.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, tail):
        pre = tail
        # move nodes after cur to after prev one by one 
        while head is not tail:
            head.next, pre, head = pre, head, head.next
        return pre
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next
        new_head = self.reverse(head, cur)
        # head now is the thing before last
        head.next = self.reverseKGroup(cur, k)
        return new_head
# @lc code=end

'''
class Solution:
    def reverseKNodes(self, prev, k):
        prev, cur = prev, prev.next
        # move nodes after cur to after prev one by one 
        for _ in range(k-1):
            temp, cur.next = cur.next, cur.next.next
            temp.next, prev.next  = prev.next, temp
        return cur
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """ 
        self.next = head
        prev, cur = self, self.next
        i = 0
        while cur:
            i += 1
            if i % k == 0:
                prev = self.reverseKNodes(prev, k)
                cur  = prev.next
            else:
                cur = cur.next
        return self.next
 '''

