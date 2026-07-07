#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canReach = 0
        for i, jump in enumerate(nums):
            if i > canReach:
                return False
            canReach = max(canReach, i + jump)
            if canReach >= n - 1:
                return True
# @lc code=end