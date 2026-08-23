#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        l, r = 0, len(nums) - 1
            pass
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid
        if target <= nums[l]:
            return l
        elif target <= nums[r]:
            return r
        return len(nums)
# @lc code=end

