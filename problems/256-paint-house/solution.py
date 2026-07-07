class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        dp = costs
        for i in range(1, len(dp)):
            for j in range(3):
                dp[i][j] += min(dp[i-1][(j+1) % 3], dp[i-1][(j+2) % 3])
        return min(dp[-1])