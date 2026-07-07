#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for amt in range(amount+1):
            for coin in coins:
                if coin > amt:
                    continue
                dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        return dp[amount] if dp[amount] < float('inf') else -1
        
# @lc code=end

