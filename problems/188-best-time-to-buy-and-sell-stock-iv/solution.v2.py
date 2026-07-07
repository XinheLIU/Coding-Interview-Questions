class Solution(object):
    def maxProfitII(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price_diff = [x - y for x,y in zip(prices[1:], prices[:-1])]
        profit = 0
        for diff in price_diff:
            if diff > 0:
                profit += diff
        return profit 
    
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not len(prices):
            return 0
        n = len(prices)
        if k > n/2:
            return self.maxProfitII(prices)
        """
        * dp[i, j] represents the max profit up until prices[j] using at most i transactions. 
        * dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
        *          = max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))
        """
        dp = [[0 for i in prices] for j in range(k + 1)]
        for i in range(1,k+1):
            localmax = dp[i-1][0] - prices[0]  # the part about jj
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1], prices[j] + localmax)
                localmax = max(localmax, dp[i-1][j] - prices[j])
        return dp[k][n-1]