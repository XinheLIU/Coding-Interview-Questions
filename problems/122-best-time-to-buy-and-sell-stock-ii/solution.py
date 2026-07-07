#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                ret += prices[i] - prices[i-1]
        return ret
# @lc code=end
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        return sum([x - y if x > y else 0 for x, y in zip(prices[1:], prices[:-1])])
'''

