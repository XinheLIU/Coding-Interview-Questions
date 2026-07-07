#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (45.16%)
# Likes:    2485
# Dislikes: 255
# Total Accepted:    476.9K
# Total Submissions: 1.1M
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#

# @lc code=start
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
        
# @lc code=end

