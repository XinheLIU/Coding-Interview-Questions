#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            ret = 0
            while n > 0:
                n, digit = divmod(n, 10)
                ret += digit ** 2
            return ret
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = get_next(n)
        return n == 1
# @lc code=end

