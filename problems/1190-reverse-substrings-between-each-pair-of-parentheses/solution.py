#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = collections.deque()
        for i in range(len(s)):
            if s[i] == '(':
               stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                s = s[:j] + s[j:i][::-1] + s[i:]
        return "".join([c for c in s if c not in ('(', ')')])
# @lc code=end

