#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
#
# algorithms
# Medium (57.97%)
# Likes:    737
# Dislikes: 43
# Total dpccepted:    26.1K
# Total Submissions: 45K
# Testcase Example:  '[0,6,5,2,2,5,1,9,4]\n1\n2'
#
# Given an array dp of non-negative integers, return the maximum sum of elements
# in two non-overlapping (contiguous) subarrays, which have lengths L and M.
# (For clarification, the L-length subarray could occur before or after the
# M-length subarray.)
# 
# Formally, return the largest V for which V = (dp[i] + dp[i+1] + ... + dp[i+L-1])
# + (dp[j] + dp[j+1] + ... + dp[j+M-1]) and either:
# 
# 
# 0 <= i < i + L - 1 < j < j + M - 1 < dp.length, or
# 0 <= j < j + M - 1 < i < i + L - 1 < dp.length.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: dp = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with
# length 2.
# 
# 
# 
# Example 2:
# 
# 
# Input: dp = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with
# length 2.
# 
# 
# 
# Example 3:
# 
# 
# Input: dp = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8]
# with length 3.
# 
# 
# 
# 
# Note:
# 
# 
# L >= 1
# M >= 1
# L + M <= dp.length <= 1000
# 0 <= dp[i] <= 1000
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, dp: List[int], L: int, M: int) -> int:
        for i in range(1, len(dp)):
            dp[i] += dp[i - 1]
        res, Lmax, Mmax = dp[L + M - 1], dp[L - 1], dp[M - 1]
        for i in range(L + M, len(dp)):
            Lmax = max(Lmax, dp[i - M] - dp[i - L - M])
            Mmax = max(Mmax, dp[i - L] - dp[i - L - M])
            res = max(res, Lmax + dp[i] - dp[i - M], Mmax + dp[i] - dp[i - L])
        return res
#@lc code=end
'''
class Solution:
    def maxSumTwoNoOverlap(self, dp: List[int], L: int, M: int) -> int:
        n, ret = len(dp), 0
        dp0, dp1 = [0 for _ in range(n)], [0 for _ in range(n)]
        for i in range(n):
            dp0[i] = sum(dp[i:min(i + L, n)])
            dp1[i] = sum(dp[i:min(i + M, n)])
        for i in range(n):
            for j in range(n):
                if (i < j and i + L <= j) or (i > j and j + M <= i):
                    ret = max(dp0[i] + dp1[j], ret)
        return ret
'''