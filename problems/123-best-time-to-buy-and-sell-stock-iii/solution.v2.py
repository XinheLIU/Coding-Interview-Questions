class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        # do best time buy and sell stock I for two times from day 1 to i and from i to n
        first, second = [0 for i in prices], [0 for i in prices]
        i,minp = 1, prices[0]
        # first trade, left to right loop, 0 to i profit
        while i < len(prices):
            first[i] = max(first[i-1], prices[i] - minp)
            minp = min(minp, prices[i])
            i += 1
        print(first)
        # last trade, right to left loop, i to n profit
        maxp, i = prices[-1], len(prices) - 2
        while i >= 1:
            second[i] = max(second[i+1], maxp - prices[i])
            maxp = max(maxp, prices[i])
            i -= 1
        profit = 0
        print(second)
        for i in range(len(prices)):
            profit = max(profit, first[i] + second[i])
        return profit