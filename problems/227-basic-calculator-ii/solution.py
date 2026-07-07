#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = collections.deque()
        operand = 0
        sign = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                operand = (operand) * 10 + int(c)
            if (not c.isdigit() and not c.isspace()) or i == len(s)-1:
                if sign == '+':
                    stack.append(operand)
                if sign == "-":
                    stack.append(-operand)
                if sign == "*":
                    stack.append(stack.pop() * operand)
                if sign == "/":
                    t = stack.pop()
                    if t // operand < 0 and t % operand != 0:
                        stack.append(t // operand + 1)
                    else:
                        stack.append(t // operand)
                    operand = 0
                sign = c
                operand = 0
        return sum(stack)
# @lc code=end

