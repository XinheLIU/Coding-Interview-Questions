class Solution:
    def numTrees(self, n: int) -> int:
        # Dynamic Programming : Catalan Number
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        # select 1 node as root, leaves the rest i-1 nodes cut into left and right (different cuts at j)
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i] =  dp[i] + dp[j] * dp[i-1-j]
        return dp[n]