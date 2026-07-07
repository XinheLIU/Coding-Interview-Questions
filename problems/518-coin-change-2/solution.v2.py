#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # knapsack problem
        if amount == 0: return 1
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        for c in range(len(coins) + 1): dp[0][c] = 1
        for a in range(1, amount + 1):
            for c in range(1, len(coins) + 1):
                dp[a][c] = (dp[a - coins[c-1]][c] if a >= coins[c-1] else 0) + dp[a][c-1]
        return dp[amount][len(coins)]
# @lc code=end

