#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ret = 0
        start = 0
        for i in range(len(nums)):
            if i and nums[i] <= nums[i-1]:
                start = i
            ret = max(ret, i - start + 1)
        return ret
# @lc code=end

