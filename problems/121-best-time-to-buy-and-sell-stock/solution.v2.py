class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not len(prices):
            return 0
        minp,profit = prices[0], 0
        for price in prices[1:]:
            minp = min(minp, price)
            profit = max(profit, price - minp)
        return profit