#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (47.44%)
# Likes:    2841
# Dislikes: 90
# Total Accepted:    162.2K
# Total Submissions: 341.6K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
# 
# 
# Example:
# 
# 
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0 
        buy, sell = [0] * n, [0] * n
        # max profit for one more buy than sell 
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        # max profit for equal buy and sell
        sell[1] = max(0, prices[1] - prices[0])
        for i in range(2,n):
            # do nothing or buy a new stock
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            # do nothing or sell
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        return sell[n-1]
# @lc code=end
'''
# O(1) Space solution  
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
'''