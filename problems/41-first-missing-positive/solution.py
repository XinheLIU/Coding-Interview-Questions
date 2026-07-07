#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (30.02%)
# Likes:    2759
# Dislikes: 730
# Total Accepted:    293.5K
# Total Submissions: 949.6K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # put i at nums[i-1]
        n = len(nums)
        for i in range(n):
            v = nums[i]
            while v > 0 and v < n + 1 and nums[v - 1] != v:
                key = v - 1
                nums[i], nums[key] = nums[key], nums[i]
                v = nums[i]
        for i, v in enumerate(nums):
            if i + 1  != v: return i + 1
        return n + 1 
# @lc code=end

