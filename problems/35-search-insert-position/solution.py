#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0: return -1
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target: return mid
            if nums[mid] > target:
                r = mid -1
            elif nums[mid] < target:
                l = mid + 1
        return l

# @lc code=end
