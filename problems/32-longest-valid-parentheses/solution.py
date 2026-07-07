#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = collections.deque([-1])
        ret = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ret = max(ret, i - stack[-1])
        return ret
# @lc code=end
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if not n: return 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == "(":
                    dp[i] = (dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0) + 2
        return max(dp)
'''

