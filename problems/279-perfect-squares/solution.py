#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n):
        # Write your code here
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        for i in range(int(n**0.5)+1):
            temp = i * i
            if int((n - temp) ** 0.5 ) ** 2 + temp == n: 
                return 1 + (0 if temp == 0 else 1)
        return 3
'''
# TLE solution

    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(2, len(dp)):
            j = 1
            while j*j <=i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        return dp[n]
'''
# @lc code=end

