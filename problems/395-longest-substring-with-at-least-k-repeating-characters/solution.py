#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (41.47%)
# Likes:    1571
# Dislikes: 124
# Total Accepted:    83.7K
# Total Submissions: 201.5K
# Testcase Example:  '"aaabb"\n3'
#
# 
# Find the length of the longest substring T of a given string (consists of
# lowercase letters only) such that every character in T appears no less than k
# times.
# 
# 
# Example 1:
# 
# Input:
# s = "aaabb", k = 3
# 
# Output:
# 3
# 
# The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# 
# 
# Example 2:
# 
# Input:
# s = "ababbc", k = 2
# 
# Output:
# 5
# 
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
# repeated 3 times.
# 
# 
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # use set
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
# @lc code=end
'''
def longestSubstring(self, s: str, k: int) -> int:
    # use bit mask - time excceed
    res, left = 0, 0 
    while left + k <= len(s):
        mask, max_ind, map = 0, left,[0] * 26
        for j in range(left,len(s)):
            t =  ord(s[j]) - ord('a')
            map[t] += 1
            if map[t] < k:
                mask |= (1 << t)
            else:
                mask &= (~(1 << t))
            if mask == 0:
                res = max(res,j - left + 1)
                max_ind = j
        left += max_ind + 1
    returnlass Solution:
'''
