#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
         # dp[i][j] meaning use first i nums to sum up to j
         n, s = len(nums), sum(nums)
         if s % 2 == 1: return False
         s //= 2
         dp = [[False] * (s + 1) for _ in range(n+1)]
         for i in range(n+1): dp[i][0] = True
         for i in range(1, n + 1):
             for j in range(1, s + 1):
                dp[i][j] = dp[i-1][j] or (dp[i-1][j - nums[i-1]] if j >= nums[i-1] else False)
         return dp[-1][-1]
# @lc code=end
'''
class Solution:
        def canPartition(self, nums: List[int]) -> bool:
            n = len(nums)
            s = sum(nums)
            if s % 2 != 0: return False
            s //= 2
            dp = [False for _ in range(s + 1)]
            dp[0] = True
            for i in range(n):
                for j in range(s, nums[i] - 1, -1):
                    dp[j] |= dp[j - nums[i]]# dp[i][j] is nums[:i] can pick sum up to j
            return dp[s]
'''