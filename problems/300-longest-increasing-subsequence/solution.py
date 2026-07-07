#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1 for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end

'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        # not true LIS, but length should be the same
        d_LIS = [nums[0]]
        for n in nums:
            if n < d_LIS[0]:
                d_LIS[0] = n
            elif n > d_LIS[-1]:
                d_LIS.append(n)
            else:
                pos = bisect.bisect_left(d_LIS, n)
                d_LIS[pos] = n
        return len(d_LIS)
'''
