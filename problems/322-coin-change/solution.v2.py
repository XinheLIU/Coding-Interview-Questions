class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # just like climbing stairs, we need the min steps
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:  # like step
                if coin <= i: 
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1