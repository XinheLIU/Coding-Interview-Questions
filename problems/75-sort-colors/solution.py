#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, i, p2 = 0, 0, len(nums) - 1
        # nums[:p0] = 1, nums[p0:i] = 2, nums[p2] = 2
        while i <= p2:
            if nums[i] == 0 and p0 != i:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1
# @lc code=end

