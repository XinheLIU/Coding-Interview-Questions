#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for v in nums:
            a ^= v
        return a
# @lc code=end

