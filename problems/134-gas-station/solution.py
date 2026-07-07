#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, cur = 0, 0
        start = 0
        for i, g in enumerate(gas):
            total += g - cost[i]
            cur += g - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return start if total >= 0 else -1
        
# @lc code=end

