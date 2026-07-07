#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        s = collections.deque([0])
        for c in S:
            if c == "(":
                s.append(0)
            else:
                v = s.pop()
                s[-1] += max(2 * v, 1)
        return s.pop()
# @lc code=end

