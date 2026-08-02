#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# Approach 2: Explicit DP with separate tracking variables

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm: explicit tracking of current and global maximum
        # cur_sum = max sum ending at current position
        # max_sum = global maximum across all positions
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            # Either extend the current subarray or start fresh from this element
            cur_sum = max(cur_sum + num, num)
            max_sum = max(cur_sum, max_sum)
        return max_sum
# @lc code=end
