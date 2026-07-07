#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (71.77%)
# Likes:    1307
# Dislikes: 92
# Total Accepted:    271.5K
# Total Submissions: 376.3K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an array of integers A sorted in non-decreasing order, return an array
# of the squares of each number, also in sorted non-decreasing order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# 
# 
# 
# Example 2:
# 
# 
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
# 
# 
# 
#

# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n, i = len(A), 0
        while i < n and A[i] < 0:
            i += 1
        j = i - 1
        ret = []
        while j >= 0 and i < n:
            x, y = A[i] ** 2, A[j] ** 2
            if x < y:
                ret.append(x)
                i += 1
            else:
                ret.append(y)
                j -= 1
        
        if j >= 0:
            ret.extend([x ** 2 for x in A[:j+1][::-1]])
        if i < n:
            ret.extend([x ** 2 for x in A[i:]])

        return ret

# @lc code=end

