#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
            if c == "(":
                stack.append(0)
            else:
                # there is a match
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack.pop()
# @lc code=end

