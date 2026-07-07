#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (40.49%)
# Likes:    543
# Dislikes: 123
# Total Accepted:    131.1K
# Total Submissions: 323.5K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Newton's Method
        if num < 2:
            return True
        
        x = num >> 1 
        while x * x > num:
            x = (x + num // x) >> 1
        return x * x == num 
# @lc code=end
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = l + ((r-l) >> 1)
            val = mid * mid 
            if val == num:
                return True
            elif val > num:
                r = mid - 1
            else:
                l = mid + 1
'''