#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP in-place: reuse the input array to store subproblem results
        # dp[i] = maximum sum ending at index i
        # Transition: dp[i] = max(nums[i], dp[i-1] + nums[i])
        # Keep only positive prefix sums — if the previous sum is negative, drop it
        ret = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:  # Only extend if previous subarray sum was positive
                nums[i] += nums[i-1]
            ret = max(nums[i], ret)
        return ret
# @lc code=end

