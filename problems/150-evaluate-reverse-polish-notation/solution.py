#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
import operator as ops
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        map = {"+": ops.add, "-":ops.sub, "*":ops.mul, "/":ops.truediv}
        for s in tokens:
            if s in map:
                r = stack.pop()
                l = stack.pop()
                stack.append(int(map[s](l, r)))
            else:
                stack.append(int(s))
        return stack.pop()
# @lc code=end

