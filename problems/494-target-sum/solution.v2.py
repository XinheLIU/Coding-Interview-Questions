#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (45.89%)
# Likes:    1895
# Dislikes: 85
# Total Accepted:    129.8K
# Total Submissions: 280.9K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
# 
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.  
# 
# 
# Example 1:
# 
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# 
# 
# Note:
# 
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# 
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # dp[i][j] is first i ele sum up to j
        if not nums:
            return 0
        dp = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0:2}
        for v in nums[1:]:
            tdict = {}
            for s in dp:
                tdict[s + v] = dp[s] + tdict.get(s + v, 0)
                tdict[s - v] = dp[s] + tdict.get(s - v, 0)
            dp = tdict
        return dp.get(S, 0)
# @lc code=end

