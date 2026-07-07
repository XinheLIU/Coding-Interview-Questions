#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left to right
        if not nums: return []
        n = len(nums)
        ret = [1] * n
        for i in range(1, n):
            ret[i] = nums[i-1] * ret[i-1]
        # right to left
        r = 1
        for i in range(n-1, -1, -1):
            ret[i] *= r
            r *= nums[i]
        return ret
# @lc code=end

