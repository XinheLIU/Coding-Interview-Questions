#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (74.06%)
# Likes:    1275
# Dislikes: 77
# Total Accepted:    252.5K
# Total Submissions: 337K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
# 
# 
# 
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        def iseven(num):
            return num % 2 == 0
        l, r = 0, len(A) - 1
        while l < r:
            m, n = A[l], A[r]
            if not iseven(m) and iseven(n):
                 A[l], A[r] = n, m
            elif not iseven(m):
                r -= 1
            elif iseven(n):
                l += 1
            else:
                l += 1
                r -= 1
        return A
# @lc code=end

