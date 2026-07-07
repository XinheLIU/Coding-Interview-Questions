#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = collections.deque()
        operand = 0
        ret = 0
        sign = 1
        for c in s:
            if c.isdigit():
                operand = (operand) * 10 + int(c)
            elif c == '+':
                ret += sign * operand
                sign = 1
                operand = 0
            elif c == "-":
                ret += sign * operand
                sign = -1
                operand = 0
            elif c == "(":
                stack.append(ret)
                stack.append(sign)
                sign = 1
                ret = 0
            elif c == ")":
                ret += sign * operand
                ret *= stack.pop() # sign
                ret += stack.pop() # num with in parenthesis
                operand = 0
        return ret + sign * operand
        
# @lc code=end

