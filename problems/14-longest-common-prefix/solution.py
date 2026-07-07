#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.27%)
# Likes:    1814
# Dislikes: 1573
# Total Accepted:    598.8K
# Total Submissions: 1.7M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs): return ""
        ret = strs[0]
        for i in range(len(strs)):
            j = 0
            while j < len(ret) and j < len(strs[i]) and ret[j] == strs[i][j]:
                j += 1
            if j == 0:
                return ""
            else: 
                ret = ret[0:j]
        return ret 
# @lc code=end

