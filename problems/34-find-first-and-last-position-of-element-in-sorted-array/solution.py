#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]

        def findFirst(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) >> 1
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l if l < len(nums) and nums[l] == target else -1

        def findLast(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) >> 1
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r if r >= 0 and nums[r] == target else -1

        return [findFirst(nums, target), findLast(nums, target)]

# @lc code=end
