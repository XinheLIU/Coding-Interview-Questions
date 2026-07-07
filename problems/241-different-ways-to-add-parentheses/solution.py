#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
import operator
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        def dfs(input, memo):
            if input in memo:
                return memo[input]
            n = len(input)
            if not any([c in ops for c in input]):
                return [int(input)]
            ret = []
            for i in range(n):
                c = input[i]
                if c in ops:
                    temp = [ops[c](a, b)
                        for a in dfs(input[:i], memo)
                        for b in dfs(input[i+1:], memo) ]
                    ret += temp
                memo[input] = ret
            return ret
        return dfs(input, {})
        
# @lc code=end

