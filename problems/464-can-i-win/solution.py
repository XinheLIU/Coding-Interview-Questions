#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal: return True
        # total sum
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal: return False
        def dfs(nums, desiredTotal, memo):
            key = str(nums)
            if key in memo:
                return memo[key]
            if nums[-1] >= desiredTotal:
                memo[key] = True
                return True
            for i in range(len(nums)):
                if not dfs(nums[:i] + nums[i+1:], desiredTotal - nums[i], memo):
                    memo[key] = True
                    return True
            memo[key] = False
            return False
        return dfs(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})
# @lc code=end

