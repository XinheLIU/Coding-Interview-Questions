#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (42.60%)
# Likes:    3105
# Dislikes: 143
# Total Accepted:    283.2K
# Total Submissions: 657K
# Testcase Example:  '[4,2,1,3]'
#
# Given the head of a linked list, return the list after sorting it in
# ascending order.
# 
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
# (i.e. constant space)?
# 
# 
# Example 1:
# 
# 
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5
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
    # merge sort
    def sortList(self, head: ListNode) -> ListNode:
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
    
    def merge(self, l1, l2):
        pre = ListNode(-1)
        cur = pre
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 is not None else l2
        return pre.next
# @lc code=end
'''
    def merge(self, one, two):
        if not one: return two
        if not two: return one
        # smaller comes first
        if one.val > two.val:
            one, two = two, one   
        one.next = self.merge(one.next, two)
        return one 
'''