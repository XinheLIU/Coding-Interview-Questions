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