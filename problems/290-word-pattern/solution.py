#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (37.00%)
# Likes:    1203
# Dislikes: 155
# Total Accepted:    196.2K
# Total Submissions: 529.8K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
# 
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if  len(words) != len(pattern):
            return False
        map = {}
        for i,c in enumerate(pattern):
            if c not in map:
                map[c] = words[i]
            else:
                if map[c] != words[i]:
                    return False
        num_p, num_w = len(map),len(set(map.values()))
        # if it is one-to-one
        return num_p == num_w
# @lc code=end

