#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (53.38%)
# Likes:    2224
# Dislikes: 189
# Total Accepted:    127.9K
# Total Submissions: 238.9K
# Testcase Example:  '"bbbab"'
#
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
# 
# Example 1:
# Input:
# 
# 
# "bbbab"
# 
# Output:
# 
# 
# 4
# 
# One possible longest palindromic subsequence is "bbbb".
# 
# 
# 
# Example 2:
# Input:
# 
# 
# "cbbd"
# 
# Output:
# 
# 
# 2
# 
# One possible longest palindromic subsequence is "bb".
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
# @lc code=end

