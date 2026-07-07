#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#
# https://leetcode.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (51.58%)
# Likes:    514
# Dislikes: 154
# Total Accepted:    52.4K
# Total Submissions: 101.5K
# Testcase Example:  '["23:59","00:00"]'
#
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the
# minimum minutes difference between any two time points in the list. 
# 
# Example 1:
# 
# Input: ["23:59","00:00"]
# Output: 1
# 
# 
# 
# Note:
# 
# The number of time points in the given list is at least 2 and won't exceed
# 20000.
# The input time is legal and ranges from 00:00 to 23:59.
# 
# 
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        new_t = []
        for time in timePoints:
            temp_t = time.split(":")
            new_t.append(int(temp_t[0]) * 60 + int(temp_t[1]))
        new_t = sorted(new_t)
        min_t = 10000000
        for i in range(len(new_t)-1):
            if(abs(new_t[i] - new_t[i+1]) < min_t):
                min_t = abs(new_t[i] - new_t[i+1])
        if(len(new_t) > 1 and (24*60 - new_t[-1] + new_t[0]) < min_t):
            min_t = 24*60 - new_t[-1] + new_t[0]
        return min_t
        
# @lc code=end

