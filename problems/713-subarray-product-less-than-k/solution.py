#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        ret = 0
        l = 0
        prod = 1
        for r, v in enumerate(nums):
            prod *= v
            while prod >= k:
                prod /= nums[l]
                l += 1
            ret += (r - l + 1)
        return ret
# @lc code=end

