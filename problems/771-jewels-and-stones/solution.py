#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        s = set(J)
        jewels = list(filter(lambda c: c in s, S))
        return len(jewels)
# @lc code=end

