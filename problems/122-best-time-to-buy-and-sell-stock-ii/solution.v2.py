class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not len(prices):
            return 0
        price_diff = [x - y for x,y in zip(prices[1:], prices[:-1])]
        profit = 0
        for diff in price_diff:
            if diff > 0:
                profit += diff
        return profit