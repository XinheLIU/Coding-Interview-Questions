#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (44.23%)
# Likes:    729
# Dislikes: 1194
# Total Accepted:    231.4K
# Total Submissions: 522.3K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s: return s
        vowels = set('aeiou'.upper() + 'aeiou')
        ss = list(s)
        l, r = 0, len(ss) - 1
        while l < r:
            if ss[l] not in vowels:
                l += 1
            elif ss[r] not in vowels:
                r -= 1
            else:
                ss[l], ss[r] = ss[r], ss[l]
                l += 1
                r -= 1
        return ''.join(ss)
# @lc code=end

