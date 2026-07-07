#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums: return None
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < nums[mid-1]:
                r = mid
            elif nums[mid] < nums[mid+1]:
                l = mid
            else:
                return mid
        if nums[r] > nums[l]:
            return r
        else:
            return l
# @lc code=end

