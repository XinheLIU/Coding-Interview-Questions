#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums):
            return (-1,-1)
        return self.findFirst(nums, target), self.findLast(nums, target)
        
    def findFirst(self, nums, target):
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + ((r-l) >> 1)
            if nums[mid] >= target:
                r = mid
            else:
                l = mid
        if nums[l] == target: return l
        if nums[r] == target: return r
        return -1
    
    def findLast(self, nums, target):
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + ((r-l) >> 1)
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        if nums[r] == target: return r
        if nums[l] == target: return l
        return -1 
        
# @lc code=end

