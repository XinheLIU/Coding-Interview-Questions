#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.50%)
# Likes:    7738
# Dislikes: 565
# Total Accepted:    1M
# Total Submissions: 3.4M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """ Manacher's Algo"""
        ### pre-processing
        ### list is iterable
        def preProcess(s):
            if not s:
                return ['^', '$']
            T = ['^']
            for c in s:
                T +=  ['#', c]
            T += ['#', '$']
            return T
     
        T = preProcess(s)
        P = [0] * len(T)
        center, right = 0, 0
        for i in range(1, len(T) - 1):
            i_mirror = 2 * center - i
            if right > i:
                P[i] = min(right - i, P[i_mirror])
            else:
                P[i] = 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > right:
                center, right = i, i + P[i]

        max_i = 0
        for i in range(1, len(T) - 1):
            if P[i] > P[max_i]:
                max_i = i
        start = (max_i - 1 - P[max_i]) // 2
        return s[start : start + P[max_i]]  
# @lc code=end
'''
  def longestPalindrome(self, s: str) -> str:
        #dynamic programming - Overtime 
        left, right, lgth = 0,0,0
        size = len(s)
        # dp[i][j] indicates s[i:j] is palidrome
        dp = np.array( [[ False ] * size] * size )
        for i in range(size):
            for j in range(i):
                dp[j][i] = (s[i] == s[j] and (dp[j+1][i-1] or i - j < 2))
                if(dp[j][i] and lgth < i - j + 1):
                    left = j
                    right = i
                    lgth = i - j + 1
            dp[i][i] = True
        return(s[left:right+1])
'''
