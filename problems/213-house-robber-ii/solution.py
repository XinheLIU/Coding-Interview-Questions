#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob1(nums: List[int]) -> int:
            if not nums:
                return 0
            dp1, dp2 = nums[:], nums[:]
            dp1[0] = 0
            # two state
            for i in range(1, len(nums)):
                dp1[i] = max(dp1[i-1], dp2[i-1])
                dp2[i] = dp1[i-1] + nums[i]
            return(max(dp1[-1], dp2[-1]))
        
        return max(rob1(nums[:-1]), rob1(nums[1:]))
# @lc code=end

