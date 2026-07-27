#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Fabonacci
        x, y = 0, 1
        for _ in range(n):
            x, y = y, x + y
        return y
# @lc code=end
