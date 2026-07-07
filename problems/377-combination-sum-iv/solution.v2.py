class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] is the # of solutions with target i
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(0, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dfs(nums, target, memo):
            if target < 0: return 0
            if target == 0: return 1
            if target in memo:
                return memo[target]
            ret= 0
            for num in nums:
                ret += dfs(nums, target - num, memo)
            memo[target] = ret
            return ret
        return dfs(nums, target, dict())
"""