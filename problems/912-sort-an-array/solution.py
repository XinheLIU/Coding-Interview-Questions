#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (63.92%)
# Likes:    547
# Dislikes: 305
# Total Accepted:    96.4K
# Total Submissions: 150.3K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order.
# 
# 
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
# 
# 
#

# @lc code=start
import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.helper(nums, 0, len(nums) - 1)
        return nums

    def helper(self, array, l, r):
        if l < r:
            pivot = self.partition(array, l, r)
            self.helper(array, l, pivot - 1)
            self.helper(array, pivot + 1, r)

    def partition(self, array, l, r):
        # find a pivot
        rand = random.randint(l,r)
        # swap the pivot to the right
        array[rand], array[r] = array[r], array[rand]
        i, pivot = l-1, array[r]
        # i is at the left of pivot
        for j in range(l,r):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        # put the pivot in place
        array[i+1], array[r] = array[r], array[i+1]
        return i+1 
# @lc code=end

