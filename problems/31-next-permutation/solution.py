#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return
        i = len(nums) - 2
        # from last digit, find the first asceding one
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        # switch with the smallest one larger than nums[i]
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # reorder numbers after i digit
        nums[i+1:] = nums[i+1:][::-1]
# @lc code=end

