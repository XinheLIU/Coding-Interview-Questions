#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # Fibnacci Sequence update must know last two digits (knowing one number does not give unique state)
        # dp[i][j] is the longest Fib seuquence end with nums[i], nums[j]
        if not A: return 0
        n = len(A)
        dp = [[2 for _ in range(n)] for _ in range(n)]
        index = {v: k for k, v in enumerate(A)}
        ret = 0
        for i, v in enumerate(A):
            for j in range(i):
                k = index.get(v - A[j], None)
                if k is not None and k < j:
                    x = dp[j][i] = dp[k][j] + 1
                    ret = max(x, ret)
        return ret if ret >= 3 else 0        
# @lc code=end

