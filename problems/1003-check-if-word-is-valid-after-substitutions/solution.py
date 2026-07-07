#
# @lc app=leetcode id=1003 lang=python3
#
# [1003] Check If Word Is Valid After Substitutions
#

# @lc code=start
class Solution:
    def isValid(self, S: str) -> bool:
        stack = collections.deque()
        for c in S:
            if c != "c":
                stack.append(c)
            else:
                if not stack or stack.pop() != "b":
                    return False
                if not stack or stack.pop() != "a":
                    return False
        return not stack
# @lc code=end

