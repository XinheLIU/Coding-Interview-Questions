#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # dp[i][j] is first i ele sum up to j
        if not nums:
            return 0
        dp = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0:2}
        for v in nums[1:]:
            tdict = {}
            for s in dp:
                tdict[s + v] = dp[s] + tdict.get(s + v, 0)
                tdict[s - v] = dp[s] + tdict.get(s - v, 0)
            dp = tdict
        return dp.get(S, 0)
# @lc code=end
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = [{} for _ in range(len(nums))]
        def dfs(sum, nums, S, i):
            if i == len(nums):
                if sum == S:
                    return 1
                else:
                    return 0
            else:
                if sum in memo[i]:
                    return memo[i][sum]
                add = dfs(sum + nums[i], nums, S, i + 1)
                substract = dfs(sum - nums[i], nums, S, i + 1)
                memo[i][sum] = add + substract
                return memo[i][sum]
        return dfs(0, nums, S, 0)
'''

