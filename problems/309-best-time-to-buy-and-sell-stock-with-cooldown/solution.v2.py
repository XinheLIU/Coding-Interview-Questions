class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        buy[i] means before day i what is the maxProfit for any sequence end with buy.

        sell[i] means before day i what is the maxProfit for any sequence end with sell.

        rest[i] means before day i what is the maxProfit for any sequence end with rest.
        """
        n = len(prices)
        if n <= 1:
            return 0 
        buy, sell = [0] * n, [0] * n
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], - prices[1])
        sell[1] = max(0, prices[1] - prices[0])
        for i in range(2,n):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        return sell[n-1]
        
        
        # O(1) solution  
		def maxProfit(self, prices):
        	if len(prices) < 2:
        	    return 0
        	sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        	for price in prices:
        	    prev_buy = buy
        	    buy = max(prev_sell - price, prev_buy)
        	    prev_sell = sell
       	        sell = max(prev_buy + price, prev_sell)
        	return sell	