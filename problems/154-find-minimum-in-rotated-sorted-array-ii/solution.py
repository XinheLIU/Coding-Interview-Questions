#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (41.61%)
# Likes:    1161
# Dislikes: 242
# Total Accepted:    211.9K
# Total Submissions: 509K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array sorted in ascring order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
# 
# Example 1:
# 
# 
# Input: [1,3,5]
# Output: 1
# 
# Example 2:
# 
# 
# Input: [2,2,2,0,1]
# Output: 0
# 
# Note:
# 
# 
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
# 
# 
#

# @lc code=l
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # key: compare mid and l 
        n = len(nums)
        if n == 0:
            return -1
        l, r = 0, n - 1
        while l + 1 < r:
            mid = l + ((r - l) >> 1) 
            if nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return min(nums[l],nums[r])
# @lc code=r
'''
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # key: compare mid and l 
        len_t = len(nums)
        if len_t == 0:
            return -1
        l, r = 0, len_t - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return min(nums[l],nums[r])
'''